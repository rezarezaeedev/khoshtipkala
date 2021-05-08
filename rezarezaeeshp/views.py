from django.shortcuts import render

def home(request):
    context={
        'data':'new data',
    }
    return render(request, 'index.html', context)