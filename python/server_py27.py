# coding: utf-8

import SimpleHTTPServer
import SocketServer
from urlparse import urlparse, parse_qs

import py27arcpy
 
PORT = 9000
 
pasta = r'C:\xampp\htdocs\tutoriais\tutorial1\python\saida\\'
 
class my_handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        
      
        # pegando o parametro get
        query_components = parse_qs(urlparse(self.path).query)
        process = parse_qs(urlparse(self.path).query).get('process', None)
      
        #print len(parse_qs(urlparse(self.path).query))
        
        if len(parse_qs(urlparse(self.path).query)) == 0:
            self.wfile.write("<center><h1>Servidor Python 2.7 !</h1></center>")
        
        elif process[0] == '1':
            self.wfile.write("<center><h1>Gerando CN... !</h1></center>")
            
            # Gera as Curvas de Niveis
            py27arcpy.GeraCN(pasta)
            
                  
        
        return
 
 
try:
   httpd = SocketServer.ThreadingTCPServer(('localhost', PORT), my_handler)
 
   print "servidor web rodando na porta ", PORT
   httpd.serve_forever()
 
except KeyboardInterrupt:
   print "Voce pressionou ^C, encerrando..."
   httpd.socket.close()