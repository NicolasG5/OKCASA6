import Pyro4
from models import ServicioChoice

@Pyro4.expose
class ServicioChoiceServer:
    def get_choices(self):
        return ServicioChoice.get_choices()

def start_server():
    servicio_choice_server = ServicioChoiceServer()
    daemon = Pyro4.Daemon()
    uri = daemon.register(servicio_choice_server)
    print("URI del servidor:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()