<?php



$conteudo = file_get_contents('python/saida/myMap.html', $flags='FILE_TEXT');

$conteudo_filt1 = explode( "https://earthengine.googleapis.com/", strstr( $conteudo, 'https://earthengine.googleapis.com/' )  )[1];  

$conteudo_filt2 = explode("',", $conteudo_filt1)[0];

/*
echo '<h3>';
print_r($conteudo_filt2);
echo '</h3>';
*/

die( json_encode( ['chave' => $conteudo_filt2 ] ) );




?>
