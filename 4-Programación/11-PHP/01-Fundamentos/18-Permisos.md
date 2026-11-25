En linux la carpeta de publicación está muy protegida, por ataques

Entonces: 

Si estáis en VUESTRO propio ordenador, y por lo tanto apache no está en produccion sino en desarrollo:

Levantaís los permisos al maximo de la carpeta de publicación:

sudo chmod 777 -R /var/www/html
(Esto te da permisos para crear carpetas y archivos en tu apache)

SOLO para equipos de desarrollo
Cuando esto sea en servidor de produccion NO hay que poner 777 sino que en sistemas infomáticos or diré lo que hay que poner

