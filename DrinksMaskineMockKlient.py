# Klient til DrinksMaskineServer.py

from socket import *
import json

HOST = 'localhost'
PORT = 12000
BUFSIZ = 1024
ADDR = (HOST, PORT)
START_CUE = "start"

tcpCliSock = socket(AF_INET, SOCK_STREAM)

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
    print("Modtaget data fra serveren, printer data:")
    print(data)

print("Forbindelsen lukkes")
tcpCliSock.close()