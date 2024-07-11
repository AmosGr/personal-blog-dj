from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request) : 
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        return render(
            request=request, 
            template_name='welcome.html', 
            context={'name':name, 'last_name':last_name, 'age':age}
            )
    return render(request=request, 
                  template_name='welcome.html')

