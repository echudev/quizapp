
BEGIN TRANSACTION;

CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    contrasenia VARCHAR(50) NOT NULL
);

CREATE TABLE HistorialPartidas (
    id INTEGER PRIMARY KEY,
    fecha VARCHAR(10) NOT NULL,
    hora VARCHAR(6) NOT NULL,
    usuarios_id INTEGER NOT NULL,
    tiempo INTEGER NOT NULL,
    puntaje INTEGER NOT NULL,
    FOREIGN KEY (usuarios_id) REFERENCES Usuarios(id)
);

COMMIT;