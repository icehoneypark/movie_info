from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        # fields = ('username',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        # fields = ('username', 'password', 'email')
        fields= '__all__'