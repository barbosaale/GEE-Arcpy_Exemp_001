# coding: utf-8

import os
import glob
import wget
import zipfile
import time
import requests

import ee
import folium

from arcgis2geojson import arcgis2geojson


# Trigger the authentication flow.
#ee.Authenticate()


ee.Initialize()

# Realizando download de imagem de GEE
def DownloadImg(pasta):
    os.chdir(pasta)
    image1 = ee.Image('srtm90_v4')
    path = image1.getDownloadUrl({
    'scale': 30,
    'crs': 'EPSG:4326',
    'region': '[[-48.75716782614552,-25.207848153927284], [-48.55357743307911,-25.207848153927284], [-48.55357743307911,-25.103743439911078], [-48.75716782614552,-25.103743439911078]]'
    })

    #print (path)
    
    url = path
    filename = wget.download(url)


#DownloadImg(pasta)

def DescZip(pasta):
    #Checando a existencia do arquivo zip, só depois continua
    os.chdir(pasta)
    count_zip = 0
    while(count_zip < 1):
        time.sleep(2)
        for arq in sorted(glob.glob('*.zip')):
            count_zip += 1 
    
    
    for arq in sorted(glob.glob('*.zip')):
                
        with zipfile.ZipFile(arq) as Zip:
            for Zip_info in Zip.infolist():
                if Zip_info.filename[-1] == '/':
                    continue
                Zip_info.filename = os.path.basename(Zip_info.filename)
                #print(Zip_info.filename)
                Zip.extract(Zip_info, pasta)
        
        
#DescZip(pasta)

   
def SendRequest(pasta, url, process):
        
    # api-endpoint 
    URL = url
    
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {'process': process} 

    try:
        r = requests.get(url = URL, params = PARAMS, timeout=0.5) 
        r.raise_for_status()
        
        print (r.status_code)
        print (r.text)
    
    except (requests.exceptions.Timeout, requests.ConnectionError):
        pass

    # extracting data in json format 
    #data = r.json() 
    #print(data)


''' --- -- --- --- --- --- --- --- ---- ---- --- '''

# Gerando tiles do GEE para o leaft


# Define a method for displaying Earth Engine image tiles to folium map.
def add_ee_layer(self, eeImageObject, visParams, name):
  map_id_dict = ee.Image(eeImageObject).getMapId(visParams)
  folium.raster_layers.TileLayer(
    tiles = map_id_dict['tile_fetcher'].url_format,
    attr = "Map Data &copy; <a href='https://earthengine.google.com/'>Google Earth Engine</a>",
    name = name,
    overlay = True,
    control = True
  ).add_to(self)



def  GeraTilesGEE(pasta):
    os.chdir(pasta)
    
    dem = ee.Image('srtm90_v4')

    # Add EE drawing method to folium.
    folium.Map.add_ee_layer = add_ee_layer

    # Set visualization parameters.
    visParams = {'min':0, 'max':3000, 'palette':['225ea8','41b6c4','a1dab4','ffffcc']}

    # Create a folium map object.
    myMap = folium.Map(location=[20, 0], zoom_start=3, height=500)

    # Add the elevation model to the map object.
    myMap.add_ee_layer(dem, visParams, 'DEM')

    # Add a layer control panel to the map.
    myMap.add_child(folium.LayerControl())

    # Display the map.
    #display(myMap)

    myMap.save("myMap.html")



def EsriJson2GeoJson(pasta):
    #Checando a existencia do arquivo json, só depois continua
    os.chdir(pasta)
    count_json = 0
    while(count_json < 1):
        time.sleep(2)
        for arq in sorted(glob.glob('*.json')):
            count_json += 1 
    
    os.chdir(pasta)
    file = "Curvas_Niveis_Suav.json"
    
    input = f = open(file, "r")
    contents = f.read()
    
    output = arcgis2geojson(contents)

    f2 = open('Curvas_Niveis_Suav_geojson.json', "w+")
    f2.write(output)
    
    f.close
    f2.close
    
    


