from django.forms import ModelForm
from users.models import User

class CreateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
