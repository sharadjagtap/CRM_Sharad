


from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

from accounts.models import tbl_account_info,Contact

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class AccountForm(ModelForm):
    class Meta:
        model=tbl_account_info
        fields='__all__'

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'


