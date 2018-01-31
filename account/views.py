from django.shortcuts import render
from account.forms import CreateForm
import requests
from django.http import HttpResponse


# to avoid office proxy policy
session = requests.Session()
session.trust_env = False


# Create your views here.
def list_all(request):
    template = 'list_all.html'

    if request.method == 'GET':
        response = session.get('http://127.0.0.1:8000/api/users/')
        print("Response code", response.status_code)
        json_data = response.json()
        context = {'users': json_data}
        return render(request, template, context)


def create(request):
    form = CreateForm
    context = {'form': form, 'msg': 'User Registration'}
    template = 'create.html'
    url = 'http://127.0.0.1:8000/api/users/'

    print("Requested:", request)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = CreateForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            data = form.cleaned_data
            response = session.get(url)
            json_data = response.json()
            for user in json_data:
                if user['username'] == data['username']:
                    context['msg'] = 'Account already exists'
            else:
                response = session.post(url, data=data)
                print("Response code", response.status_code)
                if response.status_code == 201:
                    print("Account Created.")
                    return HttpResponse('Registration Successful')

    # If this is a first request then render the template with the context
    return render(request, template, context)

