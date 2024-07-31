$('.watchlistbtn').click(function(e){
    e.preventDefault();
    var movie_id= $(this).closest('.movie_data').find('.mov_id').val(); //movie_datais the parent class
    var token   = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        method : "POST",
        url: "addwatchlist",
        data:{
            'movie_id':movie_id,
            csrfmiddlewaretoken : token,
        },
        success: function(response){
            alert.success(response.status)
        }
    });
});