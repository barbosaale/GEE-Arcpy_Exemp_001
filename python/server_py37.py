# coding: utf-8
import time
import os
import glob
# coding: utf-8

import py37gee


from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

pasta = r'C:\xampp\htdocs\tutoriais\tutorial1\python\saida'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        
        #self.send_header('Content-type','text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
                
        # pegando o parametro get
        query_components = parse_qs(urlparse(self.path).query)
        process = parse_qs(urlparse(self.path).query).get('process', None)
        
        
        
        if len(parse_qs(urlparse(self.path).query)) == 0:
            self.wfile.write(b"<center><h1>Servidor Python 3.7 !</h1></center>")
        
        
        elif process[0] == '1':
        
            self.wfile.write(process[0].encode('utf-8'))
            
            
            #-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            
            # Realiza o Download
            py37gee.DownloadImg(pasta)
            
                                
            # Descompacta arquivo zip
            py37gee.DescZip(pasta)
            
            
             # Gerando tiles do GEE para o Leaft
            py37gee.GeraTilesGEE(pasta)
            
                        
            # Enviando request p api.php
            py37gee.SendRequest(pasta, "http://localhost/tutoriais/tutorial1/api.php",process[0])     
            
            
            # Enviando request p server python, disparando geração de curvas de níveis           
            py37gee.SendRequest(pasta, "http://localhost:9000", "1")
           
                      
            #self.wfile.write(b'ok')
            #self.wfile.write(imsi[0].encode('utf-8'))
            #print( (imsi[0]) )
            
            
        
        elif process[0] == '2':
            py37gee.EsriJson2GeoJson(pasta)
            print (process[0])
        
        
        return
                
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
print ("servidor web rodando na porta 8000")
httpd.serve_forever()




