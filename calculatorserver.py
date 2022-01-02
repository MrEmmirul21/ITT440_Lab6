import socket
import sys
import time
import errno
import math
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
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
            elif fun[0] == 'b':
                fun = 'Square root'
                answer = math.sqrt(num)
            elif fun[0] == 'c':
                fun = 'Exponential'
                answer = math.exp(num)
            elif fun[0] == 'd':
                fun = "Factorial"
                answer = math.factorial(num)
            else:
                answer = ('Error')

            reply = (str(answer))

            print ('Calculation complete, answer sent to client\n')
        except:
            print ('Input error')
            reply = ('Invalid input, try again')

        if not data:
            break
        s_sock.sendall(str.encode(reply))
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',8888))
    print("listen to client...")
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
