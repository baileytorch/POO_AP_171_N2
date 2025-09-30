USE ap_171_n2;

CREATE TABLE IF NOT EXISTS comunas(
	codigo_comuna VARCHAR(5) NOT NULL,
	nombre_comuna VARCHAR(30) NOT NULL,
	CONSTRAINT PK_comunas PRIMARY KEY(codigo_comuna));