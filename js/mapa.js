var bounds = null;
    

var map = L.map(
    'map', {
    center: [-28, -55],
    zoom: 5,
    maxBounds: bounds,
    layers: [],
    worldCopyJump: false,
    crs: L.CRS.EPSG3857,
    zoomControl: true,
    });

    
    
var tile_layer_openstreetmap = L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        {
        "attribution": null,
        "detectRetina": false,
        "maxNativeZoom": 18,
        "maxZoom": 18,
        "minZoom": 0,
        "noWrap": false,
        "opacity": 1,
        "subdomains": "abc",
        "tms": false
}).addTo(map);




var layer_control = {
    base_layers : { "openstreetmap" : tile_layer_openstreetmap, },
    
    };

layerControl = L.control.layers(
    layer_control.base_layers,
    layer_control.overlays,
    {position: 'topright',
    collapsed: true,
    autoZIndex: true
    }
    ).addTo(map);
            
    

// ------------------------------------------
//-------------------------------------------



var checkMyMap = setInterval(function(){
    checkMyMap1();
}, 3000);

var checkMyMap1 = function(){
    
    $.ajax({
        
        url:'./python/saida/myMap.html',
        type:'HEAD',
        
        success: function() {
            //arquivo existe
            
            //adiciona o layer com o dem
            addLayerDem();
            
            clearInterval(checkMyMap);
        },

        error: function() {
            //arquivo não existe
            
        },
     });
}

var tile_layer_srtm;
var addLayerDem = function(){
    
    var chave;
    $.ajax({
        url:'./api2.php',
        method:'get',
        data: '',
        /*crossDomain: true,*/
        asycn: false,
        dataType: 'json',
        //data:form.serialize()
    }).done(function(data){
        
        chave = data['chave'].toString();
        xurl = ('https://earthengine.googleapis.com/' + chave)

    })


    
    tile_layer_srtm = L.tileLayer(
        xurl,
        {
        "attribution": "Map Data &copy; <a href='https://earthengine.google.com/'>Google Earth Engine</a>",
        "detectRetina": false,
        "maxNativeZoom": 18,
        "maxZoom": 18,
        "minZoom": 0,
        "noWrap": false,
        "opacity": 1,
        "subdomains": "abc",
        "tms": false
    }).addTo(map);
    
    
    layer_control1 = {
    base_layers : { "openstreetmap" : tile_layer_openstreetmap, },
    overlays : { "DEM" : tile_layer_srtm, }
    };



    
    layerControl.remove()
    
    layerControl1 = L.control.layers(
    layer_control1.base_layers,
    layer_control1.overlays,
    {position: 'topright',
    collapsed: true,
    autoZIndex: true
    }
    ).addTo(map);
    
    $('.prompt').append('<br>Tiles do GEE adicionados com suceso !')
}


// - - - - - - - - -  - - - -  - - - - 


var checkMyMap_b = setInterval(function(){
    checkMyMap2();
}, 3000);

var checkMyMap2 = function(){
    
    $.ajax({
        
        url:'./python/saida/Curvas_Niveis_Suav_geojson.json',
        type:'HEAD',
        
        success: function() {
            //arquivo existe
            addLayerCN();
            
            clearInterval(checkMyMap_b);
        },

        error: function() {
            //arquivo não existe
            
        },
     });
}




var addLayerCN = function(){
    
    var chave;
    $.ajax({
        url:'./python/saida/Curvas_Niveis_Suav_geojson.json',
        method:'get',
        data: '',
        /*crossDomain: true,*/
        asycn: false,
        dataType: 'json',
        //data:form.serialize()
    }).done(function(data){
        
        layer_cn = L.geoJSON(data).addTo(map);
        
        layer_cn.setStyle({
            color: 'black',
            weight: 0.8
        });
    })


    
        
    layer_control = {
    base_layers : { "openstreetmap" : tile_layer_openstreetmap, },
    overlays : { "DEM" : tile_layer_srtm, "Curvas Niveis": layer_cn }
    };



    
    layerControl1.remove()
    
    layerControl2 = L.control.layers(
    layer_control.base_layers,
    layer_control.overlays,
    {position: 'topright',
    collapsed: true,
    autoZIndex: true
    }
    ).addTo(map);
    
    $('.prompt').append('<br>Curvas de Níveis adicionadas com suceso !')
}
