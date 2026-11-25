DELETE FROM alumnos
WHERE id = 13;

SELECT * FROM alumnos;

DELETE FROM alumnos
WHERE nombre = 'Pablo';

INSERT INTO alumnos
(id,nombre,apellidos,email)
VALUES
(NULL, 'Lucas','Andrés Griego','lucas@sturmprojekt.com');

// Los id que anteriormente se utilizaron, aunque eliminemos un alumno que lo utilizaba, y este quede libre, ya no se utiliza, 