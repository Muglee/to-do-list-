from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from myApp.models import *
from django import forms 

class myUserCreationform(UserCreationForm):
    class Meta:
        model = customUSer
        fields=UserCreationForm.Meta.fields+("email","first_name","last_name")
        

class myAuthenticationForm(AuthenticationForm):
    class Meta:
        model=customUSer 
        fields = ["username","password"]
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = categoryModel
        fields = ["categoryName"]
        
class CategorytaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ["categoryName","taskName","description","priority","due_date","status","completed_date"]
        widgets = {
            'due_date' : forms.DateInput(attrs={'type':'date',"class":"form-group"}),
            'completed_date' : forms.DateInput(attrs={'type':'date',"class":"form-group"}),
            'description' : forms.Textarea(attrs={'type':'text',"class":"form-group"})
            }
            
            
        