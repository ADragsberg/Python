# Klient til DrinksMaskineServer.py

from socket import *
import json

# Constants
HOST = 'localhost'
PORT = 12000
BUFSIZ = 1024
ADDR = (HOST, PORT)
START_CUE = "start"

tcpCliSock = socket(AF_INET, SOCK_STREAM)

# Lav drink (data er en json string med ingredienser(inklusiv mængde) og antal ingredienser)
def lavDrink(data):
    print("Du skal nu lave en følgende drink:")
    print(data)

    keys = list(data['ingredienser'].keys())
    values = list(data['ingredienser'].values())

    i = 0
    while i < data['antalIngs']:
        print(f"Fyld {values[i]} ml {keys[i]} i glasset")

        amountToFill = int(values[i])
        actualAmount = 0

        while actualAmount < amountToFill:
            # Hvis bruger trykker på pil op
            if input().lower() == "up":
                actualAmount += 50
                print(f"{actualAmount} ml {keys[i]} i glasset")

        i +=1

    print("Drinken er nu klar til at blive serveret, velbekomme!")

# Læs input fra bruger
# Hvis input er "start" så sendes forespørgslen til serveren, som svarer med en drinkopskrift
data = input('Indtast "start" for at starte maskinen:')
if not data or not data == START_CUE:
    print("Ugyldigt input")
tcpCliSock.connect(ADDR)
print("Forbindelse oprettet til serveren")
print("Sender forespørgsel til serveren")
tcpCliSock.send(data.encode())
data = tcpCliSock.recv(BUFSIZ).decode()
if not data:
    print("Ingen data modtaget")
# json load
data = json.loads(data)
lavDrink(data)

print("Forbindelsen lukkes")
tcpCliSock.close()