-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-01-2026 a las 04:13:51
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
  `num_caso` int(6) NOT NULL,
  `documento` varchar(25) NOT NULL,
  `caso_tipo` enum('academico','personal','familiar','disciplinario') NOT NULL,
  `caso_descripcion` text NOT NULL,
  `caso_fecha_apertura` date NOT NULL,
  `caso_fecha_cierre` date DEFAULT NULL,
  `doc_pronal` varchar(25) NOT NULL,
  `caso_estado` enum('abierto','cerrado','en seguimiento') DEFAULT 'abierto'
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
  `est_direccion` varchar(150) DEFAULT NULL,
  `est_telefono` varchar(10) DEFAULT NULL,
  `est_estado` enum('activo','retirado') DEFAULT 'activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `intervenciones`
--

CREATE TABLE `intervenciones` (
  `num_intervencion` int(6) NOT NULL,
  `num_caso` int(6) NOT NULL,
  `int_descripcion` text NOT NULL,
  `int_fecha` date NOT NULL,
  `doc_pronal` varchar(25) NOT NULL,
  `int_compromiso` text DEFAULT NULL,
  `int_fecha_compromiso` date DEFAULT NULL,
  `int_estado_compromiso` enum('pendiente','cumplido','vencido') DEFAULT 'pendiente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesionales`
--

CREATE TABLE `profesionales` (
  `doc_pronal` varchar(25) NOT NULL,
  `prof_nombres` varchar(255) NOT NULL,
  `prof_apellidos` varchar(255) NOT NULL,
  `prof_cargo` varchar(50) NOT NULL,
  `prof_telefono` varchar(10) DEFAULT NULL,
  `prof_email` varchar(254) DEFAULT NULL,
  `prof_estado` enum('activo','inactivo') DEFAULT 'activo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `user_id` int(11) NOT NULL,
  `user_username` varchar(50) NOT NULL,
  `user_password_hash` varchar(255) NOT NULL,
  `user_rol` enum('administrador','directivo','coordinacion','docente','director_grupo','profesional_apoyo') NOT NULL,
  `doc_pronal` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `casos`
--
ALTER TABLE `casos`
  ADD PRIMARY KEY (`num_caso`),
  ADD KEY `documento` (`documento`),
  ADD KEY `doc_pronal` (`doc_pronal`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`documento`);

--
-- Indices de la tabla `intervenciones`
--
ALTER TABLE `intervenciones`
  ADD PRIMARY KEY (`num_intervencion`),
  ADD KEY `num_caso` (`num_caso`),
  ADD KEY `doc_pronal` (`doc_pronal`);

--
-- Indices de la tabla `profesionales`
--
ALTER TABLE `profesionales`
  ADD PRIMARY KEY (`doc_pronal`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `user_username` (`user_username`),
  ADD KEY `doc_pronal` (`doc_pronal`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `casos`
--
ALTER TABLE `casos`
  MODIFY `num_caso` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `intervenciones`
--
ALTER TABLE `intervenciones`
  MODIFY `num_intervencion` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `casos`
--
ALTER TABLE `casos`
  ADD CONSTRAINT `casos_ibfk_1` FOREIGN KEY (`documento`) REFERENCES `estudiantes` (`documento`) ON UPDATE CASCADE,
  ADD CONSTRAINT `casos_ibfk_2` FOREIGN KEY (`doc_pronal`) REFERENCES `profesionales` (`doc_pronal`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `intervenciones`
--
ALTER TABLE `intervenciones`
  ADD CONSTRAINT `intervenciones_ibfk_1` FOREIGN KEY (`num_caso`) REFERENCES `casos` (`num_caso`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `intervenciones_ibfk_2` FOREIGN KEY (`doc_pronal`) REFERENCES `profesionales` (`doc_pronal`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`doc_pronal`) REFERENCES `profesionales` (`doc_pronal`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
