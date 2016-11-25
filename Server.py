import socket, datetime, os

now = datetime.datetime.now()

def Chrome(host, port, s):
    http_resp = """\
HTTP/1.1 200 OK
Content-Type: text/html

"""

    if path == '/':
         htmlfile = open('Website/index.html', 'r')
         htmltext = htmlfile.readlines()
         sock.sendall(http_resp)
         sock.sendall(''.join(htmltext))
         sock.close()

    elif path != '/':
        try:
            file = open('/root/Desktop/Quirky/Quirky HTTP Server/Website'+path, 'r')
            text = file.readlines()
            sock.sendall(http_resp)
            sock.sendall(''.join(text))
            sock.close()

        except Exception as e:
            err_resp = """\
HTTP/1.1 404
""" 
            htmlfile = open('Website/404_stuff/old_404.html', 'r')
            print ("[\033[1;94m{}\033[00m] \033[1;31m{}{}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), 'Sending 404 to: ', str(c_addr[0]))[0])
            htmltext = htmlfile.readlines()
            sock.sendall
            sock.sendall(''.join(htmltext))
            sock.close()


def FireFox(host, port, s):

    http_resp = """\
HTTP/1.1 200 OK
Content-Type: text/html
Server: Quirky HTTP
Message: Yew

{}
"""
    if path == '/':
        htmlfile = open('Website/index.html', 'r')
        htmltext = htmlfile.readlines()
        sock.sendall(http_resp.format(''.join(htmltext)))
        sock.close()

    elif path != '/':
        try:
            file = open('/root/Desktop/Quirky/Quirky HTTP Server/Website'+path, 'r')
            text = file.readlines()
            sock.sendall(http_resp.format(''.join(text)))
            sock.close()

        except Exception as e:
            err_resp = """\
HTTP/1.1 200 OK
Content-Type: image/jpeg

{}
""" 
            htmlfile = open('Website/404_stuff/old_404.html', 'r')
            print ("[\033[1;94m{}\033[00m] \033[1;31m{}{}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), 'Sending 404 to: ', str(c_addr[0]))[0])
            htmltext = htmlfile.readlines()
            sock.sendall(err_resp.format(''.join(htmltext)))
            sock.close()          

banner = """
           ___        _      _            _   _ _____ _____ ____  
          / _ \ _   _(_)_ __| | ___   _  | | | |_   _|_   _|  _ \ 
         | | | | | | | | '__| |/ / | | | | |_| | | |   | | | |_) |
         | |_| | |_| | | |  |   <| |_| | |  _  | | |   | | |  __/ 
          \__\_\___,_|_|_|  |_|\_\___, | |_| |_| |_|   |_| |_|    
                                  |___/                           
         """

print('\033[1;33m{}\033[00m'.format(banner))

host = '192.168.0.13'
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(51)

print ("[\033[1;94m{}\033[00m] \033[1;35m{}{} {}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), 'Running on ', host, port))
print ("[\033[1;94m{}\033[00m] \033[1;35m{}{}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), 'Running in: ', os.getcwd()))
i = 0
while True:
    i += 1
    print ("[\033[1;94m{}\033[00m] \033[1;32m{}{}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), 'Open for Connection: ', i))
    sock, c_addr = s.accept()
    print ("[\033[1;94m{}\033[00m] \033[1;32m{}{}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), 'Got Connection from: ', str(c_addr[0])[0]))
    raw_request = sock.recv(1024)
    request = raw_request.split('\n', 1)[0]
    user_agent = raw_request.split('\n', 3)[0]
    
    request_line = raw_request.splitlines()[0]
    request_line = request_line.rstrip('\r\n')
    (request_method,  # GET
     path,            # /hello
     request_version  # HTTP/1.1
     ) = request_line.split()
    print ("[\033[1;94m{}\033[00m] \033[1;33m{}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), request.strip('[')))
    if 'Firefox/50.0' in raw_request:
        print ("[\033[1;94m{}\033[00m] \033[1;32m{} {} {}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), str(c_addr[0]) ,'Has Browser:', 'Firefox/50.0'))
        FireFox(host, port, s)
    elif 'Chrome' in raw_request:
        print ("[\033[1;94m{}\033[00m] \033[1;32m{} {} {}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), str(c_addr[0]) ,'Has Browser:', 'Chrome'))
        Chrome(host, port, s)


if __name__ == '__main__':
    main(host, port, s)