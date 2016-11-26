import socket, datetime, os, base64

now = datetime.datetime.now()

def fire_404(host, port, s, path):
    err_resp = """\
HTTP/1.1 404
Content-Type: text/html

{}
"""
    htmlfile = open('Website/404.html', 'r')
    print ("[\033[1;94m{}\033[00m] \033[1;31m{}{}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), 'Sending 404 to: ', str(c_addr[0]))[0])
    htmltext = htmlfile.read()
    sock.sendall(err_resp.format(''.join(htmltext)))
    sock.close()

def chrome_404(host, port, s, path):
    err_resp = """\
HTTP/1.1 404
Content-Type: text/html

{}
"""
    htmlfile = open('Website/404.html', 'r')
    print ("[\033[1;94m{}\033[00m] \033[1;31m{}{}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), 'Sending 404 to: ', str(c_addr[0]))[0])
    htmltext = htmlfile.read()
    sock.sendall(''.join(htmltext))
    sock.close()


def chrome_png(host, port, s, path):
    err_resp = """\
HTTP/1.1 200 OK
Content-Type: image/png

{}
"""
    try:
        img_jpeg = open('Website'+path, 'rb')
        img = img_jpeg.readlines()
        sock.sendall(''.join(img))
        sock.close()
        
    except Exception as e:
        chrome_404(host, port, s, path)

def fire_png(host, port, s, path):
    err_resp = """\
HTTP/1.1 200 OK
Content-Type: image/png

{}
"""
    try:
        img_png = open('Website'+path, 'rb')
        img = img_png.readlines()
        sock.sendall(err_resp.format(''.join(img)))
        sock.close()
        
    except Exception as e:
        print(e)
        htmlfile = open('Website/404_stuff/old_404.html', 'r')
        print ("[\033[1;94m{}\033[00m] \033[1;31m{}{}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), 'Sending 404 to: ', str(c_addr[0]))[0])
        htmltext = htmlfile.read()
        sock.sendall(err_resp.format(''.join(htmltext)))
        sock.close()

def chrome_jpeg(host, port, s, path):
    err_resp = """\
HTTP/1.1 200 OK
Content-Type: image/jpeg

{}
"""     
    try:
        img_jpeg = open('Website'+path, 'rb')
        img = img_jpeg.readlines()
        sock.sendall(''.join(img))
        sock.close()
    
    except Exception as e:
        chrome_404(host, port, s, path)

def fire_jpeg(host, port, s, path):
    err_resp = """\
HTTP/1.1 200 OK
Content-Type: image/jpeg

{}
"""     
    try:
        img_jpeg = open('Website'+path, 'rb')
        img = img_jpeg.readlines()
        sock.sendall(err_resp.format(''.join(img)))
        sock.close()
    
    except Exception as e:
        fire_404(host, port, s, path)

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

    elif '.png' in path:
        fire_png(host, port, s, path)

    elif '.jpeg' in path:
        fire_jpeg(host, port, s, path)

    elif path != '/':
        try:
            file = open('Website'+path, 'r')
            text = file.readlines()
            sock.sendall(http_resp.format(''.join(text)))
            sock.close()

        except Exception as e:
            fire_404(host, port, s, path)

def Phone_Chrome(host, port, s):
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

    elif '.png' in path:
        chrome_png(host, port, s, path)

    elif '.jpeg' in path:
        chrome_jpeg(host, port, s, path)
        

    elif path != '/':
        try:
            file = open('Website'+path, 'r')
            text = file.readlines()
            sock.sendall(http_resp)
            sock.sendall(''.join(text))
            sock.close()

        except Exception as e:
            chrome_404(host, port, s, path)

def Phone_FireFox(host, port, s):

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

    elif '.png' in path:
        fire_png(host, port, s, path)

    elif '.jpeg' in path:
        fire_jpeg(host, port, s, path)

    elif path != '/':
        try:
            file = open('Website'+path, 'rb')
            text = file.readlines()
            sock.sendall(http_resp.format(''.join(text)))
            sock.close()

        except Exception as e:
            fire_404(host, port, s, path)          

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
    
    print(raw_request)

    if 'Firefox/50.0' in raw_request:
        print ("[\033[1;94m{}\033[00m] \033[1;32m{} {} {}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), str(c_addr[0]) ,'Has Browser:', 'Firefox/50.0'))
        Phone_FireFox(host, port, s)
    
    elif 'Chrome' in raw_request:
        print ("[\033[1;94m{}\033[00m] \033[1;32m{} {} {}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), str(c_addr[0]) ,'Has Browser:', 'Chrome'))
        Phone_Chrome(host, port, s)

    elif 'Firefox/45.0' in raw_request:
        print ("[\033[1;94m{}\033[00m] \033[1;32m{} {} {}\033[00m".format(now.strftime("%Y-%m-%d %H:%M"), str(c_addr[0]) ,'Has Browser:', 'FireFox'))
        FireFox(host, port, s)


if __name__ == '__main__':
    main(host, port, s)