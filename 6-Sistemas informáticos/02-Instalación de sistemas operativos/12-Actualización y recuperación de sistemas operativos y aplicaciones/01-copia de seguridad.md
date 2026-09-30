1.-Tenemos una base de datos llamada dam1; con el comando "cd",
vamos al directorio donde nos apetece hacer el back ap. ej: 

2.-mysqldump -u root -p dam1 > backupdam1.sql   ( por un error tuve que usar el comando: sudo mysqldump dam1 > backupdam1.sql )

# backup autoincremental
3.-mysqldump -u root -p dam1 > backupdam120260921.sql     (yo use sudo mysqldump dam1 > backupdam120260930.sql