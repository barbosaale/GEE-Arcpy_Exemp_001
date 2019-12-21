# GEE-Arcpy_Exemp_001
Um exemplo simples de integração da API do GEE com o Arcpy do Arcgis 10.2

A aplicação simula uma aplicação web integrando o uso da biblioteca do Google Earth Engine e a biblioteca Arcpy do Arcgis 10.2, através da linguagem python.

<b>Utilização:</b>
- Colocar todos os arquivos na pasta do servidor web local, por exemplo se você estiver utilizando o Windows pode utilizar o pacote Xampp ou o Wampserver. Link para download do Xampp: https://www.apachefriends.org/pt_br/index.html.  Link para donwload do Wampserver: http://www.wampserver.com/en/

- Após ligar o servidor web local e acessar a pasta onde estão os arquivos no navegador, automaticamente carregará o arquivo index.php.

- Recomendo utilizar uma versão do python 3 para instalação da biblioteca do google earth engine. 
Vou deixar o link de um tutorial mostrando a instalação da biblioteca: https://www.earthdatascience.org/tutorials/intro-google-earth-engine-python-api/
Se preferir pode instalar a biblioteca do google earth engine através do prompt do Anaconda. Neste caso é preciso ter instalado este pacote.Link para o download do Anaconda: https://www.anaconda.com/distribution/
Após ter instalado o Anaconda, para instalar a blioteca do google earth engine utilizar este comando no prompt de comando do Anaconda: conda install -c conda-forge earthengine-api
Para ligar o servidor do python 3, no prompt de comando, entrar na pasta python onde estão os arquivos da aplicação e digitar o comando: python server_py37.py

- Este exemplo tem como dependencia uma instalação do Arcgis 10.2. Procurar a pasta onde está instalado o python 2.7 do Arcgis, depois você irá rodar o python.exe desta pasta. Para ligar o servidor do python 2.7, no prompt de comando, entrar na pasta python onde estão os arquivos da aplicação e digitar o comando: python server_py27.py , lembrando que é necessário chamar o interpretador do python da pasta da instalação do Arcgis.
