import socket

ClientSocket = socket.socket()
host = '192.168.170.14'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(2048)
print(Response.decode("utf-8"))

while True:
    print('<<<<<Online Calculator>>>>>\n')
    print('Function available:')
    print('a - Logarithmic(base-10)')
    print('b - Square Root')
    print('c - Exponential')
    print('d - Factorial')
    print('x - Exit\n')

    func = input('Choose the function : ')

    if func != 'x':
        numb = input('Enter the number : ')
        ClientSocket.send(str.encode(func+':'+numb))
        Response = ClientSocket.recv(2048)
        print('Answer :')
        print(Response.decode('utf-8'))

    else:
        break

ClientSocket.close()
