import socket
import sys
import time
import errno
import math
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode('Server connecting\n'))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        try:
            function, number = data.split(":")
            fun = str(function)
            num = int(number)

            if fun[0] == 'a':
                fun = 'Logarithmic'
                answer = math.log10(num)
                print('Perform calculation: Log '+str(num)+' = '+str(answer))
            elif fun[0] == 'b':
                fun = 'Square root'
                answer = math.sqrt(num)
                print('Perform calculation: Square root of '+str(num)+' = '+str(answer))
            elif fun[0] == 'c':
                fun = 'Exponential'
                answer = math.exp(num)
                print('Perform calculation: E power of '+str(num)+' = '+str(answer))
            elif fun[0] == 'd':
                fun = "Factorial"
                answer = math.factorial(num)
                print('Perform calculation: '+str(num)+'! = '+str(answer))
            else:
                answer = ('Calculation error! Please try another input.')

            reply = (str(answer))

            print('Calculation completed. Answer sended.')
        except:
            reply = ('Invalid input! Please try again.')

        if not data:
            break
        s_sock.sendall(str.encode(reply))
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',8888))
    print("Server started\n")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                print(str(s_addr)+" connecting")
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:
                print('connection error')

    except Exception as e:
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
     	   s.close()
