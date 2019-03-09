from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import RegisterForm
from .models import users
def register_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("POST")
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            p = create_user(request)
            print(p)
            if p == 'success':
                return HttpResponse('success')
            if p == 'failure':
                return HttpResponse('failure')

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

    # if a GET (or any other method) we'll create a blank form
    else:
        print("GET")
        form = RegisterForm()

        return render(request, 'register.html', {'form': form})

def create_user(request):
    name = request.POST["name"]
    email = request.POST["email"]
    password = request.POST["password"]
    u = users(name=name, email=email, password_digest=password)
    try:
        u.save()
        return 'success'
    except:
        return 'failure'
