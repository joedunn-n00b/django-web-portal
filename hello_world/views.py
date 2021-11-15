from django.shortcuts import render

# Create your views here.
"""Define a view function called hello_world(). 
When this function is called, it will render an HTML file called hello_world.html. """

# request obj is an HTTPRequest object that is created whenever a page is loaded
# It contains information about the request, such as the method, which can take several values including GET and POST.
def hello_world(request):
    return render(request, 'hello_world.html', {})
