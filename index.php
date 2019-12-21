<!DOCTYPE html>
<html>

<head>
	<title>Integrando GEE e Arcpy</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	
	<script async="true" src="js/jquery-3.4.1.min.js"> </script>	
	
	<!-- CSS -->
	<link href="css/style.css" rel="stylesheet" /> 


	<!-- Dependencias do Leaft -->
	<script src="https://cdn.jsdelivr.net/npm/leaflet@1.3.4/dist/leaflet.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.3.4/dist/leaflet.css"/>

	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>

	<!-- -- -- -- -- -- -- -- -- -- --  -->

	<!-- Bootstrap css -->
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">



</head>

<body>

<header>
	<nav class="navbar sombra navbar-login">
     	<div class="container">
        	
        	<div class="row">
        		
        		<div class="col">
          			
          			<h3>Integrando GEE e Arcpy</h3>
          			
        		</div>
        
		        <div class="col">
		          	
			        
		             <h5 style="text-align: right;">GeoAlgoritmo | 15 de Dezembro de 2019</h5>
	          
	          	</div>
      		
      		</div>
      	
      	</div>
    
    </nav>

</header>


<div class="container">
	<div class="row">
		<div class="col-sm-10">
			<div id="map" class="sombra b1 folium-map">
					
					
			</div>
			
		</div>
			

		<div class="col-sm-2">
			
			<div class="sombra menu">
			
				<a class="btn btn-primary btn-lg" href="javascript:func1()" role="button">Start</a>	
			
			</div>
		
		</div>
	</div>
</div>

<div class="container">
	<div class="row">
		<div class="col-md-12">
			<div class="sombra b2 prompt">
				
				

			</div>
		</div>
	</div>


</div>




<script type="text/javascript">


var func1 = function(){

	$.ajax({
		beforeSend:function(){
			$('.prompt').append('Obtendo dados do GEE...<br>');
		},
		url:'http://localhost:8000',
		method:'get',
		data: {'process': 1 },
		/*crossDomain: true,*/
    	dataType: '',
		//data:form.serialize()
	}).done(function(data){
		
				
	})

}



</script>









<script src="js/mapa.js"></script>

</body>

</html>



