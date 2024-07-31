from django.urls import path
from . import views


urlpatterns = [

    path('', views.login, name="login"),
    path('login', views.login, name="login"),
    path('logining/', views.logining, name="logining"),
    path('signup', views.signup, name="signup"),
    
    path('logout',views.logout_view,name='logout'),

    path('index/',views.index, name="index"),
    path('genre/', views.genre, name="genre"),
    # for showing all the movies in genre
    path('showmovies/<int:movie_id>/', views.showmovies, name="showmovies"),
    # for showing the movie video
    path('video/<int:movie_id>/', views.video, name="video"), 
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('setoption', views.setoption, name="setoption"),

    path('history', views.history, name="history"),
    path('supportus', views.supportus, name="supportus"),
   

    path('action', views.action, name="action"),
    path('thriller', views.thriller, name="thriller"),
    path('comedy', views.comedy, name="comedy"),
    path('romantic', views.romantic, name="romantic"),
    path('horror', views.horror, name="horror"),
    path('tvseries', views.tvseries, name="tvseries"),

    path('allmovies', views.allmovies, name="allmovies"),
    path('search', views.search, name="search"),
    
    

    

]