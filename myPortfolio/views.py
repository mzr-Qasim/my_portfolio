from django.shortcuts import render, redirect , get_object_or_404
from Home.models import Home
from About.models import About
from Skills.models import Skills
from Services.models import Services
from Portfolio.models import Portfolio, Category

def homePage(request):
    Home_Page = Home.objects.all()
    About_Section =About.objects.all()
    Skills_Section = Skills.objects.all()
    Services_Section = Services.objects.all()
    Portfolio_Section = Portfolio.objects.all()
    Categories = Category.objects.all()

    Data= {
    "Home_Page_Data": Home_Page,
    "About_Section_Data": About_Section, 
    "Skills_Data": Skills_Section,
    "Services_Data": Services_Section,
    "Portfolio_Data":Portfolio_Section ,
    "Categories_Data": Categories,

    
       
    }


    return render(request, 'index.html',Data)