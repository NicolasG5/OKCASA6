from django.test import TestCase
from django.urls import reverse
from .models import *


class EquipoInspeccionTestCase(TestCase):
    def test_equipo_inspeccion(self):
        # Crea una instancia del modelo
        equipo = EquipoInspeccion(nombres='Equipo de Prueba', disponibilidad='Disponible', Cantidad=5)

        # Verifica los atributos del equipo
        self.assertEqual(equipo.nombres, 'Equipo de Prueba')
        self.assertEqual(equipo.disponibilidad, 'Disponible')
        self.assertEqual(equipo.Cantidad, 5)

        # Guarda el equipo en la base de datos
        equipo.save()

        # Recupera el equipo de la base de datos
        saved_equipo = EquipoInspeccion.objects.get(pk=equipo.pk)

        # Verifica que el equipo guardado sea igual al original
        self.assertEqual(saved_equipo.nombres, 'Equipo de Prueba')
        self.assertEqual(saved_equipo.disponibilidad, 'Disponible')
        self.assertEqual(saved_equipo.Cantidad, 5)



class SolicitudEnLineaTest(TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        # Crea objetos Tecnico
        tecnico = Tecnico.objects.create(nombre="Técnico 1")
        
        # Crea una instancia de SolicitudEnLinea
        self.solicitud = SolicitudEnLinea.objects.create(
            tecnico_id=tecnico,
            nombre="John",
            apellido="Doe",
            correo="johndoe@example.com",
            fecha="2023-06-25",
            hora="12:00",
            estado="Pendiente",
            descripcion="Descripción de la solicitud",
            servicio=2
        )
    
    def test_solicitud_str_representation(self):
        # Verifica que el método __str__() devuelva una representación adecuada
        expected_str = "Descripción de la solicitud - John Doe (johndoe@example.com) - Fecha: 2023-06-25 Hora: 12:00 - Estado: Pendiente - Servicio: Montar y desmontar material"
        self.assertEqual(str(self.solicitud).strip().lower(), expected_str.strip().lower())

class RegisterViewTest(TestCase):
    def test_register_success(self):
        # Crea un diccionario con los datos de prueba para el registro
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }

        # Realiza una petición POST a la URL de registro con los datos
        response = self.client.post(reverse('register'), data)

        # Verifica que la respuesta sea un redireccionamiento a la URL de éxito
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

        # Verifica que el usuario haya sido creado correctamente
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_password_mismatch(self):
        # Crea un diccionario con los datos de prueba para el registro
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'confirm_password': 'mismatchedpassword'
        }

        # Realiza una petición POST a la URL de registro con los datos
        response = self.client.post(reverse('register'), data)

        # Verifica que la respuesta sea un código de estado exitoso
        self.assertEqual(response.status_code, 200)

        # Verifica que se haya mostrado un mensaje de error en el formulario
        self.assertFormError(response, 'form', 'confirm_password', 'Passwords do not match.')

        # Verifica que el usuario no haya sido creado
        self.assertFalse(User.objects.filter(username='testuser').exists())

class UrlsTest(TestCase):
    def test_solicitud_url(self):
        # Obtiene la URL inversa para 'solicitud'
        url = reverse('solicitud')

        # Realiza una petición GET a la URL
        response = self.client.get(url)

        # Verifica que la respuesta sea un código de estado exitoso
        self.assertEqual(response.status_code, 302)

        # Agrega aquí más aserciones para verificar el contenido de la respuesta, si es necesario

    # def test_historial_url(self):
    #     # Obtiene la URL inversa para 'historial'
    #     url = reverse('historial')

    #     # Realiza una petición GET a la URL
    #     response = self.client.get(url)

    #     # Verifica que la respuesta sea un código de estado exitoso
    #     self.assertEqual(response.status_code, 200)

    #     # Agrega aquí más aserciones para verificar el contenido de la respuesta, si es necesario