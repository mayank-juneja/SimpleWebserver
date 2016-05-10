WebServer Program Version 1.0 09/09/2014
author: Mayank Juneja

OBJECTIVE
------------------
To create a HTTP-based web server that handles various requests from users.

VERSION INFORMATION
-------------------------------------
- This Version of Web Server is developed using Python 2.7 on Windows OS
- It is made to run on localhost and port 9090 which can be changed in configuration file.
- It contains main webserver file, a configuration file and a data folder which contains a .gif, .png, .txt and .html file named as test. Data Folder also contains a server's default webpage named index.html
- This Version responds to the request with four file types i.e. .gif, .png, .txt and .html using HTTP/1.1
- Implemented Errors and Exceptions are:
	-HTTP/1.0 400 Bad Request: Invalid HTTP-Version
	-HTTP/1.0 400 Bad Request: Invalid URL
	-HTTP/1.0 400 Bad Request: Invalid Method
	-HTTP/1.0 501 Not Implemented: File Type not supported by browser
	-HTTP/1.0 501 Not Implemented: File Type not implemented
	-HTTP/1.1 404 Not Found: File not found
	-HTTP/1.1 500 Internal Server Error

GENERAL USAGE NOTES
--------------------------------------
- Set host and port parameters from configuration file. By default they are set to localhost and port: 9090 
- Run .py file named webserver.py using command prompt.
-After webserver is started, send request from a web browser in format eg. localhost:9090 (To display default webpage) and localhost:9090/test.png(To fetch a .png file from server)
-Any incorrect URL, method, filetype or other server errors are handled by webserver.

References
-----------------
- http://www.w3.org/Protocols/rfc1945/rfc1945
- http://www.pythonforbeginners.com/
- https://wiki.python.org/
- http://stackoverflow.com/questions/20242434/how-to-run-python-scripts-on-a-web-servere-g-localhost
- http://ilab.cs.byu.edu/python/socket/echoserver.html

----------------------------------------------------------------------------------------------------------------------------
Mayank Juneja can be reached at:

Voice:	530-820-2311
E-mail:	mayank.juneja@colorado.edu
