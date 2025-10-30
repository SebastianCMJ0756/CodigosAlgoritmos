import requests

#       ///////////////////////////////////////
#      APIPOKE - Busqueda binaria y grafos
#       Conexion con la API y obtencion de datos
#       ///////////////////////////////////////

class APIPOKE:
    def __init__(self, URL):
        self.URL = URL      #Direccion de la API que se usara
    
    def ObtencionDatos(self):
        Respuesta= requests.get(self.URL)   #Se hace la solicitud 

        if Respuesta.status_code != 200:    #Manejo de errores
            print("No se pudo obtener los datos de la POKEAPI...")
            return None

        return Respuesta.json()    #Respuesta convertida a JSON