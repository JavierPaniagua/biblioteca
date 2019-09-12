-- CREAR LA BASE DE DATOS
CREATE DATABASE biblioteca;

-- CREAR LAS TABLAS QUE NO TIENEN RELACION CON OTRAS TABLAS
CREATE TABLE public.categorias
(
    id_categoria serial NOT NULL,
    nombre_categoria character varying NOT NULL,
    CONSTRAINT categorias_pkey PRIMARY KEY (id_categoria),
    CONSTRAINT categorias_nombre_categoria_unk UNIQUE (nombre_categoria)

);

CREATE TABLE public.autores
(
    id_autor serial NOT NULL,
    nombre_autor character varying NOT NULL,
    CONSTRAINT autores_pkey PRIMARY KEY (id_autor),
    CONSTRAINT autores_nombre_autor_unk UNIQUE (nombre_autor)

);

CREATE TABLE public.cursos
(
    id_curso serial NOT NULL,
    nombre_curso character varying NOT NULL,
    CONSTRAINT cursos_pkey PRIMARY KEY (id_curso),
    CONSTRAINT cursos_nombre_curso_unk UNIQUE (nombre_curso)

);

CREATE TABLE public.especialidades
(
    id_especialidad serial NOT NULL,
    nombre_especialidad character varying NOT NULL,
    CONSTRAINT especialidades_pkey PRIMARY KEY (id_especialidad),
    CONSTRAINT especialidades_nombre_especialidad_unk UNIQUE (nombre_especialidad)

);

CREATE TABLE public.profesores
(
    id_profesor serial NOT NULL,
    nombre_profesor character varying NOT NULL,
    cedula_profesor character varying NOT NULL,
    direccion_profesor character varying NOT NULL,
    telefono_profesor character varying NOT NULL,
    CONSTRAINT profesores_pkey PRIMARY KEY (id_profesor),
    CONSTRAINT profesores_nombre_profesor_unk UNIQUE (nombre_profesor),
    CONSTRAINT profesores_cedula_profesor_unk UNIQUE (cedula_profesor)

);

-- CREAR LAS TABLAS QUE TIENEN RELACION CON OTRAS TABLAS

CREATE TABLE public.libros
(
    id_libro serial NOT NULL,
    nombre_libro character varying NOT NULL,
    id_categoria int NOT NULL,
    CONSTRAINT libros_pkey PRIMARY KEY (id_libro),
    CONSTRAINT libros_nombre_libro_unk UNIQUE (nombre_libro),
    CONSTRAINT libros_id_categoria_fkey FOREIGN KEY (id_categoria) REFERENCES public.categorias (id_categoria)

);

CREATE TABLE public.alumnos
(
    id_alumno serial NOT NULL,
    nombre_alumno character varying NOT NULL,
    cedula_alumno character varying NOT NULL,
    direccion_alumno character varying NOT NULL,
    telefono_alumno character varying NOT NULL,
    id_curso int NOT NULL,
    id_especialidad int NOT NULL,
    CONSTRAINT alumnos_pkey PRIMARY KEY (id_alumno),
    CONSTRAINT alumnos_nombre_alumno_unk UNIQUE (nombre_alumno),
    CONSTRAINT alumnos_id_curso_fkey FOREIGN KEY (id_curso) REFERENCES public.cursos (id_curso),
    CONSTRAINT alumnos_id_especialidad_fkey FOREIGN KEY (id_especialidad) REFERENCES public.especialidades (id_especialidad)

);