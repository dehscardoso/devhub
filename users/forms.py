from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Nome:', 'email':'E-mail:', 'username':'Usuário:', 
            'password1':'Senha:', 'password2':'Confirmação Senha:'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username',
                  'location', 'bio', 'short_intro', 'profile_image',
                  'social_github', 'social_linkedin', 'social_twitter',
                  'social_youtube', 'social_website']
                  
        labels = {'name':'Nome:', 'email':'E-mail:', 'username':'Usuário:',
                  'location':'Localização:', 'bio':'Apresentação:', 'short_intro':'Intro:', 
                  'profile_image':'Imagem do Perfil:', 'social_github':'GitHub:',
                  'social_linkedin':'LinkedIn:', 'social_twitter':'Twitter:',
                  'social_youtube':'YouTube:', 'social_website':'WebSite:'}

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        labels = {
            'name':'Nome:', 'description':'Descrição:'
        }
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']
        labels = {
            'name':'Nome:', 'email':'E-mail:', 'subject':'Assunto:', 'body':'Mensagem:'
        }
    
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})