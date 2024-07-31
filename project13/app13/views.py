from urllib import request
from django.shortcuts import get_object_or_404, render,  redirect
from .models import Movies,profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password


    
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        
        if profile.objects.filter(Email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('/signup')  # Redirect back to signup page
            
        else:
             # Hash the password
            user = profile(Name=name, Email=email, Password=password)
            user.save()
            messages.success(request, 'Data saved successfully')
            return redirect('login')  # Redirect to login page after signup

    else:
        # If not POST, render the signup page with an empty form or context
        return render(request, 'signup.html')
    
# def logining(request):
#     if request.method == 'POST':
#         email = request.POST.get('Email')
#         password = request.POST.get('Password')
        
#         # Use Django's authentication system to validate credentials
#         try:
#                 user=profile.objects.get(Email=email)
#                 if not user:
#                     messages.warning(request,'Email does not exist')
#                     return redirect('/login')
#                 elif password!=user.Password:
#                     messages.warning(request,'Password Incorrect')
#                     return redirect('/login')
#                 else:
#                     messages.success(request,'Success')
#                     return redirect('/index/')
#         except:
#                 messages.warning(request,'Email or Password incorrect')
#                 return redirect('/login')
#     else:
#         return render(request,'login.html')
def logining(request):
    if request.method == 'POST':
         email = request.POST.get('Email')
         password = request.POST.get('Password')
         
         try:
                user=profile.objects.get(Email=email)
                if not user:
                    messages.warning(request,'Email does not exist')
                    return redirect('index')
                elif password!=user.Password:
                    messages.warning(request,'Password Incorrect')
                    return redirect('index')
                else:
                    messages.success(request,'Success')
                    return redirect('index')
         except:
                messages.warning(request,'Email or Password incorrect')
                return redirect('index')
    else:
        return render(request,'login.html')
     

def index(request):
    return render(request,'index.html')
    
# -------------------------------------------------------- History  ------------------------------------------------------------------------




def watch_movie(request, movie_id):
    movie = get_object_or_404(Movies, pk=movie_id)
    profile = get_object_or_404(profile, pk=request.user.profile.id)  # Assuming Profile is associated with the user

    # Create a WatchHistory entry
    

    # Your existing logic for rendering the movie page
    # ...

    return render(request, 'movie_detail.html', {'movie': movie})
# -------------------------------------------------------- dnt delete it  ------------------------------------------------------------------------




def genre(request):
    movie = Movies.objects.all()
    return render(request, 'genre.html',{'movie':movie})


def contact(request):
    return render(request, 'contact.html')



def about(request):
    return render(request, 'about.html')


def action(request):
    return render(request, 'action.html')


def thriller(request):
    return render(request, 'thriller.html')


def comedy(request):
    return render(request, 'comedy.html')


def romantic(request):
    return render(request, 'romantic.html')


def horror(request):
    return render(request, 'horror.html')


def tvseries(request):
    return render(request, 'tvseries.html')


def allmovies(request):
    movie = Movies.objects.all()
    return render(request, 'allmovies.html',{'movie':movie})


def showmovies(request, movie_id):
    movie = Movies.objects.get(pk=movie_id)
    return render(request, 'showmovies.html', {'movie': movie})

def video(request, movie_id):
    movie= Movies.objects.get(pk=movie_id)
    return render(request, 'video.html', {'movie': movie})


def setoption(request):    
    return render(request, "setoption.html")


def search(request):
    return render(request, 'search.html')


def history(request):    
    return render(request, "history.html")


def supportus(request):    
    return render(request, "supportus.html")


from django.core.mail import send_mail
from django.http import HttpResponse

           

# /////////////////////////////////////////////////      Login & Register     \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from django.http import JsonResponse, HttpResponse



def login(request):
    return render(request, 'login.html')







def logout_view(request):

    logout(request)
    return redirect('login')  # Redirect to the login page after logout



