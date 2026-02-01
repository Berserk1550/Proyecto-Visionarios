-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-01-2026 a las 18:09:15
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

--
-- Volcado de datos para la tabla `acudiente`
--

INSERT INTO `acudiente` (`cedula_acudiente`, `nombre_acudiente`, `apellido_acudiente`, `telefono_acudiente`, `correo_acudiente`, `direccion_acudiente`) VALUES
('31644051', 'Jenny', 'Juspian', '3098765421', 'jenny@mail.com', 'calle26#18-80');

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

--
-- Volcado de datos para la tabla `casos`
--

INSERT INTO `casos` (`num_caso`, `documento`, `caso_tipo`, `caso_descripcion`, `caso_fecha_apertura`, `caso_fecha_cierre`, `doc_pronal`, `caso_estado`) VALUES
(1, '1115965790', 'academico', 'El estudiante no presenta el taller y charla mucho en clase', '2026-01-28', '0000-00-00', '1006371222', 'abierto'),
(2, '1115965790', 'familiar', 'El estudiante refiere ser maltratado físicamente en casa, se remite a Psicología.', '2026-01-28', NULL, '1006371222', 'abierto');

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
  `est_estado` enum('activo','retirado') DEFAULT 'activo',
  `documento_acudiente` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`documento`, `est_nombres`, `est_apellidos`, `est_fecha_nacimiento`, `est_grado`, `est_direccion`, `est_telefono`, `est_estado`, `documento_acudiente`) VALUES
('1115965790', 'Santiago', 'Lopez Juspian', '2010-09-15', '6A', 'calle26#18-80', '3124567890', 'activo', '31644051');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grados`
--

CREATE TABLE `grados` (
  `id_grado` int(11) NOT NULL,
  `nombre_grupo` varchar(20) NOT NULL,
  `director_doc_pronal` varchar(25) NOT NULL,
  `estudiante_documento` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `int_estado_compromiso` enum('pendiente','en proceso','cumplida','no cumplida','anulada') DEFAULT 'pendiente',
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
('1006371222', 'Emily Natalia', 'Lopez Juspian', '1db4a0041876241916ff8b935a46b680de655e06456c77c1d2970688ea2838b9', '3154256143', 'emily@visionarios.edu.co', 'administrador', 'activo', '2026-01-28 18:39:08');

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
  ADD PRIMARY KEY (`num_caso`),
  ADD KEY `fk_caso_estudiante` (`documento`),
  ADD KEY `fk_caso_profesional` (`doc_pronal`);

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
  ADD KEY `fk_grado_director` (`director_doc_pronal`),
  ADD KEY `fk_grado_estudiante` (`estudiante_documento`);

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
  MODIFY `num_caso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `grados`
--
ALTER TABLE `grados`
  MODIFY `id_grado` int(11) NOT NULL AUTO_INCREMENT;

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
-- Filtros para la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD CONSTRAINT `fk_estudiante_acudiente` FOREIGN KEY (`documento_acudiente`) REFERENCES `acudiente` (`cedula_acudiente`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `grados`
--
ALTER TABLE `grados`
  ADD CONSTRAINT `fk_grado_director` FOREIGN KEY (`director_doc_pronal`) REFERENCES `usuarios` (`doc_pronal`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_grado_estudiante` FOREIGN KEY (`estudiante_documento`) REFERENCES `estudiantes` (`documento`) ON DELETE CASCADE ON UPDATE CASCADE;

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
