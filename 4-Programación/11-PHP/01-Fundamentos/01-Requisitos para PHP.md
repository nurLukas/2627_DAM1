#  Hace falta un servidor local

** Linux: **
sudo apt install apache2 (sevidor web)
sudo apt instal php (instalar php sobre apache)

Vuestra carpeta de publicacion estará en /var/www/html

TODO el PHP que pongáis, deberá estar dentro de esa carpeta

Si por ejemplo tenéis /var/www/html/php8/hola.php
En el navegador tendréis que poner http://localhost/php8/hola.php
Es decir /var/www/html/... equivale a http://localhost/...

** Windows: **
https://www.apachefriends.org/es/index.html

Descargáis e instaláis
Arrancais el panel de control

Vuestra carpeta de publicacion en Windows será:

C:\xampp\htdocs\...
Si por ejemplo poneis C:/XAMPP/htdocs/php8/hola.php
En el navegador tendreis que poner http://localhost/php8/hola.php

Es decir C:///XAMPP/htdocs/... Equivale a http://localhost/...

NOTA: ya tengo la carpeta php8 en C:\xampp\htdocs\ --> en esa carpeta esta el archivo de prueba "02-Salidas.php"

En el navegador puse http://localhost/php8/02-Salidas.php y ya va



en "error.log" abriendo el archivo con un editor de texto podremos ver los fallos
en "acces.log" tendremos los logs pero de todos los accesos al servidor