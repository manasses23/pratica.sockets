import socket
HOST = socket.gethostbyname('localhost')
PORT = 2000
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))



n1 = input ("\n digite o um numero para a soma: \n")				
byte_msg = n1.encode('utf-8')
client.send(byte_msg)

n2 = input("\n digite o segundo numero para a soma: \n")
byte_msg1 = n2.encode('utf-8')
client.send(byte_msg1)
	
	
n3 = input("\n digite um numero para calcular a raiz quadrada: \n")
byte_msg2 = n3.encode('utf-8')
client.send(byte_msg2)
	

      

