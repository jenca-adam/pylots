import socket
import re
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
p='GET (\S+) HTTP/1.1'
s.bind(('localhost',5556))

s.listen(5)
routes={}
def route(route,string):
    routes[route]=string
def run():
    while True:
        (c,addr)=s.accept()
        a=c.makefile().readline()
        if not re.search(p,a):
            c.sendall(
                b'''HTTP/1.1 400 BAD REQUEST'''
                )
            continue
        route=re.search(p,a).group(1)
        if route not in routes:
            print(a.replace('\n',' ')+':'+' HTTP/1.1 404 NOT FOUND')

            c.sendall(
                b'''HTTP/1.1 404 NOT FOUND'''
                )
            continue
        m=routes[route]
        l=len(m)
        t=time.ctime(time.time())
        print(a.replace('\n',' ')+':'+' HTTP/1.1 200 OK')
        c.sendall(
        f'''HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: {l}
Server: Python/3.9 - Aufschlager/0.1
Date: {t} GMT

{m}
        '''.encode('utf-8'))


