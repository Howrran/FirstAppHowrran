check_name = function(value){
    let csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    console.log(value);
    data = {check_username: value};
    $.ajax({
        url: '/account/registration/',
        type: 'POST',
        data: data,
        success: function(data){
            console.log(data);
            if (!data['name_available']) {
            $('input[name ="username"]')[0].style.innerText = "0 0 2px 1px rgba(245, 0, 0, 0.7), 0 2px 2px 0 rgba(245, 0, 0, 0.7)";
            console.log(document.getElementById('error-message'));
            document.getElementById('error-message').text = "Username is already taken!"; }
            if(data['name_available']) {
            $('input[name ="username"]')[0].style.innerText = "0 0 2px 1px rgba(0, 180, 0, 0.7), 0 2px 2px 0 rgba(0, 180, 0, 0.7)";
            document.getElementById('error-message').text = "";}
            },
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", `${csrf_token}`);
        },
        dataType: 'json',
    });
}