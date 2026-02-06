-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-02-2026 a las 14:34:02
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `visionarios`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `casos`
--

CREATE TABLE `casos` (
  `num_caso` int(11) NOT NULL,
  `documento` varchar(25) NOT NULL,
  `caso_tipo` enum('academico','personal','familiar','disciplinario') NOT NULL,
  `caso_descripcion` text NOT NULL,
  `caso_fecha_apertura` date NOT NULL,
  `caso_fecha_cierre` date DEFAULT NULL,
  `doc_pronal` varchar(25) NOT NULL,
  `caso_estado` enum('abierto','en proceso','en espera','cerrado','anulado') DEFAULT 'abierto'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `documento` varchar(25) NOT NULL,
  `est_nombres` varchar(255) NOT NULL,
  `est_apellidos` varchar(255) NOT NULL,
  `est_fecha_nacimiento` date DEFAULT NULL,
  `est_grado` varchar(20) DEFAULT NULL,
  `est_estado` enum('activo','retirado') DEFAULT 'activo',
  `nombre_acudiente` varchar(50) DEFAULT NULL,
  `apellido_acudiente` varchar(50) DEFAULT NULL,
  `telefono_acudiente` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`documento`, `est_nombres`, `est_apellidos`, `est_fecha_nacimiento`, `est_grado`, `est_estado`, `nombre_acudiente`, `apellido_acudiente`, `telefono_acudiente`) VALUES
('38875059', 'Adriana', 'Vasco', '2010-05-15', '9-3', 'activo', 'Orley', 'Vasco', '3173374649');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `intervenciones`
--

CREATE TABLE `intervenciones` (
  `id_intervencion` int(11) NOT NULL,
  `num_caso` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `doc_pronal` varchar(25) NOT NULL,
  `descripcion` text NOT NULL,
  `int_compromiso` text DEFAULT NULL,
  `int_fecha_compromiso` date DEFAULT NULL,
  `int_estado_compromiso` enum('pendiente','por vencer','no cumplida','anulada') DEFAULT 'pendiente',
  `int_estado` enum('programada','realizada','reprogramada','cancelada') DEFAULT 'realizada',
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `doc_pronal` varchar(25) NOT NULL,
  `prof_nombres` varchar(255) NOT NULL,
  `prof_apellidos` varchar(255) NOT NULL,
  `user_password_hash` varchar(255) NOT NULL,
  `prof_telefono` varchar(20) DEFAULT NULL,
  `prof_email` varchar(100) DEFAULT NULL,
  `user_rol` enum('administrador','directivo','coordinacion','docente','director_grupo','profesional_apoyo') NOT NULL,
  `prof_estado` enum('activo','inactivo') DEFAULT 'activo',
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`doc_pronal`, `prof_nombres`, `prof_apellidos`, `user_password_hash`, `prof_telefono`, `prof_email`, `user_rol`, `prof_estado`, `fecha_registro`) VALUES
('1112389606', 'Luis', 'Muriel', '15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225', '3173374649', 'nose@gmail.com', 'directivo', 'activo', '2026-02-03 02:55:24');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `casos`
--
ALTER TABLE `casos`
  ADD PRIMARY KEY (`num_caso`),
  ADD KEY `fk_caso_estudiante` (`documento`),
  ADD KEY `fk_caso_profesional` (`doc_pronal`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`documento`);

--
-- Indices de la tabla `intervenciones`
--
ALTER TABLE `intervenciones`
  ADD PRIMARY KEY (`id_intervencion`),
  ADD KEY `num_caso` (`num_caso`),
  ADD KEY `doc_pronal` (`doc_pronal`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`doc_pronal`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `casos`
--
ALTER TABLE `casos`
  MODIFY `num_caso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `intervenciones`
--
ALTER TABLE `intervenciones`
  MODIFY `id_intervencion` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `casos`
--
ALTER TABLE `casos`
  ADD CONSTRAINT `fk_caso_estudiante` FOREIGN KEY (`documento`) REFERENCES `estudiantes` (`documento`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_caso_profesional` FOREIGN KEY (`doc_pronal`) REFERENCES `usuarios` (`doc_pronal`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `intervenciones`
--
ALTER TABLE `intervenciones`
  ADD CONSTRAINT `intervenciones_ibfk_1` FOREIGN KEY (`num_caso`) REFERENCES `casos` (`num_caso`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `intervenciones_ibfk_2` FOREIGN KEY (`doc_pronal`) REFERENCES `usuarios` (`doc_pronal`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
