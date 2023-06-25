from django import forms
from .models import SolicitudEnLinea
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView


from django import forms
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/'

    def form_valid(self, form):
        password = form.cleaned_data.pop('password')
        confirm_password = form.cleaned_data.pop('confirm_password')

        if password != confirm_password:
            form.add_error('confirm_password', 'Passwords do not match.')
            return self.form_invalid(form)

        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        return super().form_valid(form)


class OtraOpcionWidget(forms.Select):
    def __init__(self, choices, attrs=None):
        super().__init__(attrs, choices=choices)

    def format_output(self, rendered_widgets):
        return '<div class="otra-opcion-widget">%s</div>' % rendered_widgets


class OtraOpcionField(forms.ChoiceField):
    def __init__(self, choices, *args, **kwargs):
        super().__init__(choices=choices, *args, **kwargs)

    def compress(self, value):
        if value:
            return value
        return ''


class SolicitudEnLineaForm(forms.ModelForm):
    CHOICES = (
        ('Opcion 1', 'Estudio de suelo'),
        ('Opcion 2', 'Montar y desmontar material'),
        ('Opcion 3', 'Mantenimiento y reparación'),
        ('Opcion 4', 'Otra opción'),
    )

    servicios = forms.CharField(widget=OtraOpcionWidget(choices=CHOICES))

    class Meta:
        model = SolicitudEnLinea
        fields = ('nombre', 'apellido', 'correo', 'fecha', 'hora', 'estado', 'descripcion', 'servicios',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Juan'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Pérez'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: correo@example.com'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 2023-06-01'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 12:00'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Descripción de la solicitud'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['servicios'].widget.choices = self.CHOICES


# class SolicitudEnLinea(models.Model):
#     CHOICES = (
#         ('Opcion 1', 'Estudio de suelo'),
#         ('Opcion 2', 'Montar y desmontar material'),
#         ('Opcion 3', 'Mantenimiento y reparación'),
#     )

#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)
#     correo = models.EmailField()
#     fecha = models.DateField()
#     hora = models.TimeField()
#     estado = models.CharField(max_length=100)
#     descripcion = models.TextField()
#     servicios = models.CharField(max_length=100, choices=CHOICES)

#     def __str__(self):
#         return self.nombre + ' ' + self.apellido
# o