ALTER TABLE clientes
ADD CONSTRAINT chk_clientes_email
CHECK (
    email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
);

| nombre       | apellidos          | email            | Identificador |
+--------------+--------------------+------------------+---------------+
| Jose Vicente | Carratalá Sanchis  | info@jocarsa.com |             1 |
| Jose Vicente | Carratalá Sanchis  | info@jocarsa.com |             2 |
| Juan         | García Lopez       | juan@garcia.com  |             3 |
| Jaime        | Martinez           | Hola que tal     |             4 |

DELETE FROM clientes WHERE Identificador = 4;  (primero elimino el cliente
que no cumple la condición, para luego generar el ALTER TABLE que aplica la condición)

Rectificado ello, ya puedo dar el siguiente comando:

ALTER TABLE clientes
ADD CONSTRAINT chk_clientes_email
CHECK (
    email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
);