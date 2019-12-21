<?php

/*
echo '<br><br> Conteúdo do GET: <br><br>';
foreach ($_GET as $key => $value){
    echo $key . ' -- ' . $value . '<br>';
}
*/

if( isset($_GET['process']) ){
	if( file_exists('process' . $_GET['process']) ){
	
	}else {
		$my_file = 'process' . $_GET['process'];
		$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);
		//write some data here
		fclose($handle);
	};
}




die( json_encode($_GET) );



?>