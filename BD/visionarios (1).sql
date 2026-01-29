-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-01-2026 a las 05:34:16
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
-- Estructura de tabla para la tabla `acudiente`
--

CREATE TABLE `acudiente` (
  `cedula_acudiente` varchar(16) NOT NULL,
  `nombre_acudiente` varchar(50) NOT NULL,
  `apellido_acudiente` varchar(50) NOT NULL,
  `telefono_acudiente` varchar(20) DEFAULT NULL,
  `correo_acudiente` varchar(100) DEFAULT NULL,
  `direccion_acudiente` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `caso_estado` enum('abierto','en proceso','en espera','cerrado','anulado') DEFAULT 'abierto'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `documento` varchar(16) NOT NULL,
  `est_nombres` varchar(255) NOT NULL,
  `est_apellidos` varchar(255) NOT NULL,
  `est_fecha_nacimiento` date DEFAULT NULL,
  `est_grado` varchar(20) DEFAULT NULL,
  `est_direccion` varchar(150) DEFAULT NULL,
  `est_telefono` varchar(10) DEFAULT NULL,
  `est_estado` enum('activo','retirado') DEFAULT 'activo',
  `documento_acudiente` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grados`
--

CREATE TABLE `grados` (
  `id_grado` int(11) NOT NULL,
  `nombre_grupo` varchar(20) NOT NULL,
  `director_user_id` varchar(16) NOT NULL,
  `estudiante_user_id` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `intervenciones`
--

CREATE TABLE `intervenciones` (
  `num_intervencion` int(11) NOT NULL,
  `num_caso` int(11) NOT NULL,
  `user_id` varchar(16) NOT NULL,
  `int_fecha` date NOT NULL,
  `int_descripcion` text NOT NULL,
  `int_compromiso` text DEFAULT NULL,
  `int_fecha_compromiso` date DEFAULT NULL,
  `int_estado_compromiso` enum('pendiente','en proceso','cumplida','no cumplida','anulada') DEFAULT 'pendiente',
  `int_estado` enum('programada','realizada','reprogramada','cancelada') DEFAULT 'realizada',
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `user_id` varchar(16) NOT NULL,
  `user_username` varchar(50) NOT NULL,
  `user_lastname` varchar(50) NOT NULL,
  `user_password_hash` varchar(255) NOT NULL,
  `user_phone` varchar(20) DEFAULT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `user_rol` enum('administrador','directivo','coordinacion','docente','director_grupo','profesional_apoyo') NOT NULL,
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `acudiente`
--
ALTER TABLE `acudiente`
  ADD PRIMARY KEY (`cedula_acudiente`);

--
-- Indices de la tabla `casos`
--
ALTER TABLE `casos`
  ADD PRIMARY KEY (`num_caso`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`documento`),
  ADD KEY `fk_estudiante_acudiente` (`documento_acudiente`);

--
-- Indices de la tabla `grados`
--
ALTER TABLE `grados`
  ADD PRIMARY KEY (`id_grado`),
  ADD KEY `director_user_id` (`director_user_id`),
  ADD KEY `estudiante_user_id` (`estudiante_user_id`);

--
-- Indices de la tabla `intervenciones`
--
ALTER TABLE `intervenciones`
  ADD PRIMARY KEY (`num_intervencion`),
  ADD KEY `fk_intervencion_caso` (`num_caso`),
  ADD KEY `fk_intervencion_usuario` (`user_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `casos`
--
ALTER TABLE `casos`
  MODIFY `num_caso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `grados`
--
ALTER TABLE `grados`
  MODIFY `id_grado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `intervenciones`
--
ALTER TABLE `intervenciones`
  MODIFY `num_intervencion` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD CONSTRAINT `fk_estudiante_acudiente` FOREIGN KEY (`documento_acudiente`) REFERENCES `acudiente` (`cedula_acudiente`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `grados`
--
ALTER TABLE `grados`
  ADD CONSTRAINT `grados_ibfk_1` FOREIGN KEY (`director_user_id`) REFERENCES `usuarios` (`user_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `grados_ibfk_2` FOREIGN KEY (`estudiante_user_id`) REFERENCES `estudiantes` (`documento`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `intervenciones`
--
ALTER TABLE `intervenciones`
  ADD CONSTRAINT `fk_intervencion_caso` FOREIGN KEY (`num_caso`) REFERENCES `casos` (`num_caso`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_intervencion_usuario` FOREIGN KEY (`user_id`) REFERENCES `usuarios` (`user_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
