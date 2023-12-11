# Klient til DrinksMaskineServer.py

from socket import *

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

    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)

print("Forbindelsen lukkes")
tcpCliSock.close()

