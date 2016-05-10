'''
Created on 08-Sep-2014

@author: mayank
'''

'''
Importing required libraries
'''
import socket
from os import curdir, sep
import datetime

'''
Checking if URL passed is incorrect
'''
def checkIfIncorrectURL():
    #Checking presence of consecutive dots
    if '..' in line or '...' in line or '....' in line:
        return True
    #Checking presence of unsafe characters from RFC1738
    elif '^' in line or '~' in line or '`' in line:
        return True
    #Checking presence of Delims
    elif '<' in line or '>' in line or '#' in line or '%' in line:
        return True
    else:
        return False

'''
Checking If passed file extension is handeled by WebServer
'''
def checkContentType():
    l = line.split('/')
    length = len(l)
    if '.' in l[length - 2]:
        position = l[length-2].index('.')
        extension = l[length-2][position:position+5]
        if extension.strip() not in config['typesHandled']:
            return True
        else:
            return False
    else:
        return False
        
'''
Function to Validate if correct request is made, it includes checking HTTP Version, URL Syntax, Request Method, Unsupported File Types, Supported File Extensions.
'''
def validateRequest():
    #Validating if Invalid HTTP-Version is used
    if 'HTTP/1.1' not in line and 'HTTP/1.0' not in line:
        html_data = 'HTTP/1.0 400 Bad Request: Invalid HTTP-Version:\n Content-Type: txt/html\n\n <html><h1>HTTP 400 Bad Request</h1><h2>Invalid HTML-Version</h2></html>'
        if data:
            client.send(html_data)            
        return False
    #Validating if Invalid URL is used
    elif checkIfIncorrectURL():
        html_data = 'HTTP/1.0 400 Bad Request: Invalid URL:\n Content-Type: txt/html\n\n <html><h1>HTTP 400 Bad Request</h1><h2>Invalid URL</h2></html>'
        if data:
            client.send(html_data)            
        return False
    #Validating if Invalid method is used(ASK PROFESSOR)
    elif 'GET' not in line:
        html_data = 'HTTP/1.0 400 Bad Request: Invalid Method:\n Content-Type: txt/html\n\n <html><h1>HTTP 400 Bad Request</h1><h2>Invalid Method</h2></html>'
        if data:
            client.send(html_data)            
        return False
    #Validating if File type is supported
    elif '.mpg' in line or '.ogg' in line:
        html_data = 'HTTP/1.0 501 Not Implemented:\n Content-Type: txt/html\n\n <html><h1>HTTP 501 Not Implemented</h1><h2>This type of file is not supported by browser.</h2></html>'
        if data:
            client.send(html_data) 
        return False
    #Validating if content type is implemented 
    elif checkContentType():
        html_data = 'HTTP/1.0 501 Not Implemented:\n Content-Type: txt/html\n\n <html><h1>HTTP 501 Not Implemented</h1><h2>This type of file is not implemented by server</h2></html>'
        if data:
            client.send(html_data) 
        return False
    else:
        return True


'''
Main Function
'''
config = {}
#Executing Configuration File
execfile("ws.conf", config)
host = config["host"]
port = config["port"]
backlog = 5
size = 1024
#Creating Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
today = datetime.date.today()
print 'Server Started'
print str(today)
while 1:
    '''
    processing Client's request
    '''
    try:
        client, address = s.accept()
        cfile = client.makefile('rw', 0)
        line = cfile.readline().strip()
        data = client.recv(size)
        l = line.split('/')
        length = len(l)
        n = l[length - 2].split(' ')
        sendReply = False
        mt = config["typesHandled"]
        ext = ""
        if validateRequest():
            if n[0] is '':
                print 'deafult html'
                fName = config["default"]
                mimeType = mt[".html"]
                sendReply = True
            else:
                fName = n[0]
                if '.' in fName:
                    pos = fName.index('.')
                    ext = fName[pos:pos+5]
                    ext = ext.strip()
                if ext in ".png":
                    mimeType = mt[".png"]
                    sendReply = True
                elif ext in ".gif":            
                    print 'I am here'
                    mimeType = mt[".gif"]
                    sendReply = True            
                elif ext in ".html":
                    mimeType = mt[".html"]
                    sendReply = True            
                elif ext in ".txt":
                    mimeType = mt[".txt"]
                    sendReply = True
            try:
                if sendReply == True:
                    f = open(curdir + sep + config["path"] + fName, 'rb')
                    html_data = 'HTTP/1.1 200 OK\n Content-Type: '+ mimeType + '\n\n'
                    if data:
                        print 'data sent'
                        client.send(html_data)
                        client.send(f.read())
            except IOError:
                html_data = 'HTTP/1.1 404 Not Found:\n Content-Type: txt/html\n\n <html><h1>HTTP 404 File Not Found</h1><h2>Requested File Name: '+ fName +'</h2></html>'
                if data:
                    client.send(html_data)            
        client.close()
    except:
        html_data = 'HTTP/1.1 500 Internal Server Error:\n Content-Type: txt/html\n\n <html><h1>HTTP 500 Internal Server Error</h1><h2>Cannot Allocate Memory</h2></html>'
        if data:
            client.send(html_data)

