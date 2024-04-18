; Tablas de servicios
; SQL Server
CREATE TABLE agua_corriente (
	id_agua_corriente int NOT NULL PRIMARY KEY,
	agua_corriente varchar(255) NOT NULL
);

CREATE TABLE calefaccion (
	id_calefaccion int NOT NULL PRIMARY KEY,
	calefaccion varchar(255) NOT NULL
);

CREATE TABLE cocina (
	id_cocina int NOT NULL PRIMARY KEY,
	cocina varchar(255) NOT NULL
);

CREATE TABLE efluentes_cloacales (
	id_efluentes_cloacales int NOT NULL PRIMARY KEY,
	efluentes_cloacales varchar(255) NOT NULL
);

CREATE TABLE energia_electrica (
	id_energia_electrica int NOT NULL PRIMARY KEY,
	energia_electrica varchar(255) NOT NULL
);

;; Decada de creacion

CREATE TABLE decada_de_creacion (
	id_decada_de_creacion int NOT NULL PRIMARY KEY,
	decada_de_creacion varchar(255) NOT NULL
);

CREATE TABLE clasificacion_barrio (
	id_clasificacion_barrio int NOT NULL PRIMARY KEY,
	clasificacion_barrio varchar(255) NOT NULL
);

CREATE TABLE titulo_propiedad (
	id_titulo_propiedad int NOT NULL PRIMARY KEY,
	titulo_propiedad varchar(255) NOT NULL
);


;; Tablas de lugar

CREATE TABLE provincia (
	id_provincia int NOT NULL PRIMARY KEY,
	provincia varchar (255) NOT NULL
);

CREATE TABLE departamento (
);

CREATE TABLE localidad ( 
);

CREATE TABLE barrio (
);


