#Calculadora Manasses Fernandes

import socket
HOST = socket.gethostbyname('localhost')
PORT = 2000
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind((HOST,PORT))
tcp_server_socket.listen()
client, addr = tcp_server_socket.accept()
print('Conexão de:', addr)

while True:
   
 data = client.recv(1024)
 if not data: break
 print("\n o primeiro numero para a soma é", data)
 data1 = client.recv(1024)
   
 if not data: break
 print("\n o segundo numero para a soma é", data1)
 soma = int(data) + int(data1) 
 print ("\n o resultado da soma é: ",soma)
    	
 data2 = client.recv(1024)
 if not data: break
 print("\n o numero para calculo raiz quadrada é", data2)
 from math import sqrt
 n = float(data2)
 raiz = sqrt(n)
 print ("O resultado da raiz quadrada é: ",raiz)

client.close()
tcp_server_socket.close()
