# coding: utf-8
import glob
import os
import time
import requests

import arcpy
from arcpy import env
from arcpy.sa import *
import arcpy.cartography as CA




def SendRequest(process):
            
    # api-endpoint 
    URL = "http://localhost:8000"
    
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {'process': process} 

    try:
        r = requests.get(url = URL, params = PARAMS) 
    except:
        pass

    # extracting data in json format 
    #data = r.json() 


    #print(data)




def GeraCN(pasta):
    arcpy.CheckOutExtension("Spatial")
    os.chdir(pasta)
    
    
    # Checando a existencia do arquivo tif, so depois continua
    count_tif = 0
    while(count_tif < 1):
        time.sleep(2)
        for arq in sorted(glob.glob('*.tif')):
            count_tif += 1 
    
    
    
    # Set environment settings
    env.workspace = pasta
    os.chdir(pasta)
    
    # Para cada arq tif, gera CN
    for arq in sorted(glob.glob('*.tif')):
        # criando as curvas de niveis
        Contour(arq, pasta + 'Curvas_Niveis.shp', 50, 0)
        
        # suavizando as curvas de niveis
        CA.SmoothLine(pasta + 'Curvas_Niveis.shp', pasta + 'Curvas_Niveis_Suav.shp', "PAEK" , 0.001345, "", "FLAG_ERRORS")
        
        # convertendo para esri geojson
        arcpy.FeaturesToJSON_conversion(pasta + 'Curvas_Niveis_Suav.shp', pasta + "Curvas_Niveis_Suav.json")

        SendRequest(2)    
        



