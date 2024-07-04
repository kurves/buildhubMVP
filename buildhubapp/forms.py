from django import forms

from .models import Project, Message

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['bio']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']