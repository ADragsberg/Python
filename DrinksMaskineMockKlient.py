# Klient til DrinksMaskineServer.py

from socket import *
import json

HOST = 'localhost'
PORT = 12000
BUFSIZ = 1024
ADDR = (HOST, PORT)
START_CUE = "start"

tcpCliSock = socket(AF_INET, SOCK_STREAM)

# Lav Drink Metode (Antager at data er en json string med antal ingredienser samt en dict med ingredienser og mængder)
# Skal kigge på opskrift og bede bruger om at at "fylde glas op" med ingredienserne via pile op og ned
def lavDrink(data):
    print("Du skal nu lave en drink med følgende ingredienser:")
    print(data)

    keys = list(data['ingredienser'].keys())
    values = list(data['ingredienser'].values())
    print(keys)
    print(values)

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
    

# Læs input fra bruger
# Når input er "start" så sendes forespørgslen til serveren, som svarer med en drinkopskrift
while True:
    data = input('Indtast "start" for at starte maskinen:')
    if not data or not data == START_CUE:
        break

    tcpCliSock.connect(ADDR)
    print("Forbindelse oprettet til serveren")

    print("Sender forespørgsel til serveren")
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        print("Ingen data modtaget")
        break
    # json load
    data = json.loads(data)
    lavDrink(data)
    # print("Modtaget data fra serveren, printer data:")
    # print(data)

print("Forbindelsen lukkes")
tcpCliSock.close()