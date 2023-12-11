from socket import *
import requests

# RestService


# TCP Socket forbindelse til Client

#Constants
SERVER_PORT = 12000
BUFF_SIZE = 1024
START_CUE = 'start'
BASE_URL = 'https://drinksmaskinerest.azurewebsites.net/api/opskrift'



serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', SERVER_PORT))
serverSocket.listen(1)


while True:
    print('Server is waiting for a connection')
    connectionSocket, addr = serverSocket.accept()
    print(addr, 'connected. Waiting for Client to start')

# client initierer
    start = connectionSocket.recv(BUFF_SIZE).decode()
    if start == START_CUE:
        url = BASE_URL
        try:
            response = requests.get(url)
            print('get request sent to REST')
        except:
            print('OOPS! someshting went wrong')
            response = 'ERROR'

    if response.status_code == 200:
        data = response.json()
        print('json from REST is loaded')        
        connectionSocket.send(data.encode())
        print('data sent to client')
    #Genstarter forbindelsen
    connectionSocket.close()
    print('connection closed')








    # def handleClient(start):
    #     if start == START_CUE:
    #         url = BASE_URL
    #         try:
    #             response = requests.get(url)
    #             print('get request sent to REST')
    #         except:
    #             print('OOPS! someshting went wrong')
    #             response = 'ERROR'

    #         if response == error:
    #             return


    #         if response.status_code == 200:
    #             data = response.json()
    #             print('json from REST is loaded')

    #             connectionSocket.send(data.encode())
    #             print('data sent to client')
    #         else:
    #             handleClient(start)



