from django.shortcuts import render
from .models import Home, About, Profile, Skills, Portfolio

def index(request):

    # home
    home = Home.objects.latest('updated')

    # about
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # skills
    skills = Skills.objects.all()

    # portfolio
    portfolios = Portfolio.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'skills': skills,
        'portfolios': portfolios
    }

    return render(request, 'index.html', context)