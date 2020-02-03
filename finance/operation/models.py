from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator
from django.db import models, IntegrityError
from category.models import Category


class Operation(models.Model):
    from_category = models.ForeignKey(Category, related_name='from_category',
                                      on_delete=models.CASCADE)
    to_category = models.ForeignKey(Category, related_name='to_category',
                                    on_delete=models.CASCADE)
    value = models.FloatField(MinValueValidator(0))
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_operation'

    @staticmethod
    def create(from_category, to_category, value, date):

        if date:
            operation = Operation(from_category=from_category,
                                  to_category=to_category,
                                  value=value,
                                  date=date)
        else:
            operation = Operation(from_category=from_category,
                                  to_category=to_category,
                                  value=value)

        try:
            operation.save()
            return operation
        except IntegrityError:
            return None

    @staticmethod
    def get_user_operation(user_id):
        try:
            operation_list = Operation.objects.filter(
                from_category__user_id=user_id)
            return list(operation_list)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_user_income(user_id):
        try:
            operation_list = Operation.objects.filter(
                from_category__user_id=user_id,
                from_category__type='Income')
            income = 0
            for i in operation_list:
                income += i.value
            return income
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_user_outcome(user_id):
        try:
            operation_list = Operation.objects.filter(
                to_category__user_id=user_id,
                to_category__type='Outcome')
            outcome = 0
            for i in operation_list:
                outcome += i.value
            return outcome
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_user_current(user_id):
        try:
            income = Operation.get_user_income(user_id=user_id)
            outcome = Operation.get_user_outcome(user_id=user_id)
            return income - outcome
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_user_operation_by_category(user_id, category_id):
        operation_list = Operation.get_user_operation(user_id)
        category = Category.get_category(category_id)
        data = []

        for operation in operation_list:
            if operation.from_category.name == category.name or operation.to_category.name == category.name:
                data.append(operation)
        print(data)
        return data

    @staticmethod
    def get_user_category_income(user_id, category_id):
        try:
            category = Category.get_category(category_id)
            operation_list = Operation.objects.filter(
                to_category__user_id=user_id,
                to_category__name=category.name)

            income = 0
            for i in operation_list:
                print(i.to_category)
                income += i.value
            return income
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_user_category_outcome(user_id, category_id):
        try:
            category = Category.get_category(category_id)
            operation_list = Operation.objects.filter(
                from_category__user_id=user_id,
                from_category__name=category.name)
            outcome = 0
            for i in operation_list:
                outcome += i.value
            return outcome
        except ObjectDoesNotExist:
            return None
