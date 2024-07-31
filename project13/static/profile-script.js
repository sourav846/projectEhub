$(document).ready(function(){
    $("#signup_btn").click(function(){
        $Name = $('#namefield').val();
        $Email = $('#emailfield').val();
        $Password = $('#passwordfield').val();
        $.ajax({
            url: 'regcod',
            data: {'name': $Name, 'email': $Email, 'password': $Password},
            type: 'get',
            dataType: 'json',
            success: function(d){
                if (d.sts) {
                    alert(d.msg);
                    window.location.href = '/showprofile/';  // Redirect to the showprofile page
                } else {
                    alert(d.msg);
                }
            },
            error: function(d) {
                console.log(d);
            }
        });
    });
});