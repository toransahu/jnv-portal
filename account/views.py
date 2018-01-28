from django.shortcuts import render
from account.forms import CreateForm
import requests


# Create your views here.
def list_all(request):
    template = 'list_all.html'
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:8000/api/users/')
        json_data = response.json()
        context = {'users': json_data}
        return render(request, template, context)


def create(request):
    form = CreateForm
    context = {'form': form}
    template = 'create.html'
    print("Requested:", request)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = CreateForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # response = requests.get('http://127.0.0.1:8000/api/users/', )
            response = requests.post('http://127.0.0.1:8000/api/users/', data=form.cleaned_data)
            print("Response code", response.status_code)
            if response.status_code == 201:
                print("Account Created.")

    # If this is a first request then render the template with the context
    return render(request, template, context)

