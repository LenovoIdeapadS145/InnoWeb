from .models import New_Feedback, New_Model
from django.forms import ModelForm, TextInput

class New_Form(ModelForm):
    class Meta:
        model = New_Model
        fields = ["Word"]
        widgets = {"Word": TextInput(attrs = {"class": "input", "placeholder": "Word"})}

class New_Form1(ModelForm):
    class Meta:
        model = New_Model
        fields = ["Word", "Content"]
        widgets = {"Word": TextInput(attrs = {"class": "input", "placeholder": "Word"}),
                   "Content": TextInput(attrs = {"class": "input", "placeholder": "Content"})}

class New_Form2(ModelForm):
    class Meta:
        model = New_Feedback
        fields = ["Feedback1"]
        widgets = {"Feedback1": TextInput(attrs = {"class": "input", "placeholder": "Word"})}