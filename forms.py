from django import forms

class RopaForm(forms.Form):
    descripcion = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    
class StaffForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)



    