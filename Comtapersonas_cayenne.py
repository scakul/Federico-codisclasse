from random import randint
from time import sleep
import cayenne.client

def cayene(valors):
    contador = valors


def distancia():
    persones = randint(0,1)
    return persones


#Cayenne authentication info. This should be obtain fram de cayenne Dashboard
MQTT_USERNAME = "e04838a0-7c78-11e9-94e9-493d67fd755e"
MQTT_PASSWORD = "62f55716eab2454c898266c64b10e6f5f41c0a06"
MQTT_CLIENT_ID = "6b170ab0-7c79-11e9-94e9-493d67fd755e"
client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

while True:
    client.loop()
    persones = 0
    pasa1 = 0
    contador = 0
    for segons in range(60):
        pasa = distancia()
        if pasa >= 1:
            contador = contador + 1
        print(contador)    
        sleep(1)
    cayene(contador)
