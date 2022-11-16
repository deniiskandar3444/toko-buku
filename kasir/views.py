from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title':'About Us'
    }
    return render(request, template_name, context)