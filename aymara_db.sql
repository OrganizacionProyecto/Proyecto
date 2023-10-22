-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-10-2023 a las 03:12:41
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `aymara_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

CREATE TABLE `administrador` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `administrador`
--

INSERT INTO `administrador` (`id`, `id_usuario`) VALUES
(3, NULL),
(1, 96),
(2, 98);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id`, `nombre`) VALUES
(0, 'Categoria 1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `dni` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id`, `id_usuario`, `dni`) VALUES
(1, 1, 29207507),
(2, 3, 27899661),
(3, 7, 29307507),
(4, 1, 29207507),
(5, NULL, 29207507),
(6, NULL, 29207507),
(7, NULL, 29207507),
(8, NULL, 29207507),
(9, NULL, 29207507),
(10, NULL, 29207507),
(11, NULL, 29207507),
(12, NULL, 29207507),
(13, 1, 29207507),
(14, 1, 29207507),
(15, 1, 29207507),
(16, 1, 29207507),
(17, NULL, 29207507),
(18, NULL, 29207507),
(19, NULL, 29207507),
(20, NULL, 29207507),
(21, NULL, 29207507),
(22, 1, 29207507),
(23, 1, 29207507),
(24, 1, 29207507),
(25, 1, 29207507),
(26, 1, 29207507),
(27, 1, 29207507),
(28, 1, 29207507),
(29, 1, 29207507),
(30, 1, 29207507),
(31, 1, 29207507),
(32, 1, 29207507),
(33, 1, 29207507),
(34, 1, 29207507),
(35, 1, 29207507),
(36, 1, 29207507),
(37, NULL, 29207507),
(38, 71, 29207507),
(39, 72, 29207507),
(40, NULL, 29207507),
(41, 74, 29207507),
(42, 75, 29207507),
(43, 76, 29207507),
(44, 77, 29207507);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE `pedido` (
  `id` int(11) NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `estado` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pedido`
--

INSERT INTO `pedido` (`id`, `id_cliente`, `estado`) VALUES
(1, 1, 'Pendiente'),
(2, 1, 'Pendiente'),
(3, 1, 'Pendiente'),
(4, NULL, 'Pendiente'),
(5, NULL, 'Pendiente'),
(6, NULL, 'Pendiente'),
(7, NULL, 'Pendiente'),
(8, NULL, 'Pendiente'),
(9, NULL, 'Pendiente'),
(10, 35, 'Pendiente'),
(11, 36, 'Pendiente'),
(12, 37, 'Pendiente'),
(13, 38, 'Pendiente'),
(14, 39, 'Pendiente'),
(15, 40, 'Pendiente'),
(16, 41, 'Pendiente'),
(17, 42, 'Pendiente'),
(18, 44, 'Pendiente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido_producto`
--

CREATE TABLE `pedido_producto` (
  `id` int(11) NOT NULL,
  `pedido_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pedido_producto`
--

INSERT INTO `pedido_producto` (`id`, `pedido_id`, `producto_id`) VALUES
(1, 1, 1),
(2, 1, 4),
(3, 2, 5),
(4, 2, 3),
(5, 9, 22),
(6, 10, 24),
(7, 11, 26),
(8, 12, 28),
(9, 13, 30),
(10, 14, 32),
(11, 15, 33),
(12, 16, 35),
(13, 17, 37),
(14, 18, 40);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `stock` int(11) NOT NULL,
  `categoria_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id`, `nombre`, `descripcion`, `precio`, `imagen`, `stock`, `categoria_id`) VALUES
(1, 'Yerba', 'Yerba del Litoral', '1500.00', 'img1.jpg', 40, 0),
(3, 'Producto 1', 'Descripción del Producto 1', '19.99', 'imagen1.jpg', 100, 0),
(4, 'Producto 2', 'Descripción del Producto 1', '1900.99', 'imagen1.jpg', 100, 0),
(5, 'Producto 1', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(6, 'Producto 1', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(13, 'Producto 1', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(14, 'Producto 1', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(15, 'Producto 1', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(16, 'Producto 1', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(17, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(18, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(19, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(20, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(21, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(22, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(23, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(24, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(25, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(26, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(27, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(28, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(29, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(30, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(31, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(32, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(33, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(35, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(37, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(39, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0),
(40, 'Producto 18', 'Descripción del Producto 1', '19.00', 'imagen1.jpg', 100, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `contrasenia` varchar(255) NOT NULL,
  `domicilio` varchar(255) NOT NULL,
  `tipo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `correo`, `contrasenia`, `domicilio`, `tipo`) VALUES
(1, 'Mr', 'Martin', 'Mr@example.com', 'contraseña123', '123 Calle Principal', 0),
(3, 'Mr', 'Martin', 'Mr2@example.com', 'contraseña123', '123 Calle Principal', 1),
(4, 'Mr', 'Martin', 'Mr3@example.com', 'contraseña123', '123 Calle Principal', 2),
(5, 'Mr', 'Martin', 'Mr4@example.com', 'contraseña123', '123 Calle Principal', 2),
(7, 'Mr', 'Martin', 'Mr5@example.com', 'contraseña123', '123 Calle Principal', 0),
(9, 'Mr', 'Martin', 'Mr6@example.com', 'contraseña123', '123 Calle Principal', 0),
(10, 'Mr', 'Martin', 'Mr7@example.com', 'contraseña123', '123 Calle Principal', 0),
(11, 'Mr', 'Martin', 'Mr8@example.com', 'contraseña123', '123 Calle Principal', 0),
(12, 'Mr', 'Martin', 'Mr9@example.com', 'contraseña123', '123 Calle Principal', 1),
(14, 'Mr', 'Martin', 'Mr10@example.com', 'contraseña123', '123 Calle Principal', 1),
(15, 'Mr', 'Martin', 'Mr11@example.com', 'contraseña123', '123 Calle Principal', 1),
(17, 'Mr', 'Martin', 'Mr12@example.com', 'contraseña123', '123 Calle Principal', 1),
(19, 'Mr', 'Martin', 'Mr14@example.com', 'contraseña123', '123 Calle Principal', 1),
(21, 'Mr', 'Martin', 'Mr15@example.com', 'contraseña123', '123 Calle Principal', 1),
(23, 'Mr', 'Martin', 'Mr16@example.com', 'contraseña123', '123 Calle Principal', 1),
(25, 'Mr', 'Martin', 'Mr17@example.com', 'contraseña123', '123 Calle Principal', 1),
(26, 'Mr', 'Martin', 'Mr18@example.com', 'contraseña123', '123 Calle Principal', 1),
(29, 'Mr', 'Martin', 'Mr20@example.com', 'contraseña123', '123 Calle Principal', 1),
(30, 'Mr', 'Martin', 'Mr21@example.com', 'contraseña123', '123 Calle Principal', 1),
(31, 'Mr', 'Martin', 'Mr23@example.com', 'contraseña123', '123 Calle Principal', 1),
(32, 'Mr', 'Martin', 'Mr24@example.com', 'contraseña123', '123 Calle Principal', 1),
(34, 'Mr', 'Martin', 'Mr25@example.com', 'contraseña123', '123 Calle Principal', 1),
(35, 'Mr', 'Martin', 'Mr26@example.com', 'contraseña123', '123 Calle Principal', 1),
(36, 'Mr', 'Martin', 'Mr27@example.com', 'contraseña123', '123 Calle Principal', 1),
(37, 'Mr', 'Martin', 'Mr28@example.com', 'contraseña123', '123 Calle Principal', 1),
(39, 'Mr', 'X', 'x@example.com', 'contraseña123', '123 Calle Principal', 1),
(40, 'Mr', 'X', 'xs@example.com', 'contraseña123', '123 Calle Principal', 1),
(41, 'Mr', 'X', 'xos@example.com', 'contraseña123', '123 Calle Principal', 1),
(42, 'Mr', 'X', 'is@example.com', 'contraseña123', '123 Calle Principal', 1),
(43, 'Mr', 'X', 'as@example.com', 'contraseña123', '123 Calle Principal', 1),
(46, 'Mr', 'X', 'ai@example.com', 'contraseña123', '123 Calle Principal', 1),
(48, 'Mr', 'X', 'ao@example.com', 'contraseña123', '123 Calle Principal', 1),
(52, 'Mr', 'X', 'o@example.com', 'contraseña123', '123 Calle Principal', 0),
(54, 'Mr', 'X', 'oq@example.com', 'contraseña123', '123 Calle Principal', 0),
(55, 'Mr', 'X', 'q@example.com', 'contraseña123', '123 Calle Principal', 0),
(56, 'Mr', 'X', 'qs@example.com', 'contraseña123', '123 Calle Principal', 0),
(58, 'Mr', 'X', 'qos@example.com', 'contraseña123', '123 Calle Principal', 0),
(59, 'Mr', 'X', 'ss@example.com', 'contraseña123', '123 Calle Principal', 0),
(60, 'Mr', 'X', 's0@example.com', 'contraseña123', '123 Calle Principal', 0),
(61, 'Mr', 'X', 's1@example.com', 'contraseña123', '123 Calle Principal', 0),
(62, 'Mr', 'X', 'aq@example.com', 'contraseña123', '123 Calle Principal', 0),
(63, 'Mr', 'X', 'ttt@example.com', 'contraseña123', '123 Calle Principal', 0),
(65, 'Mr', 'X', 'itt@example.com', 'contraseña123', '123 Calle Principal', 0),
(66, 'Mr', 'X', 'iitt@example.com', 'contraseña123', '123 Calle Principal', 0),
(67, 'Mr', 'X', 'qtt@example.com', 'contraseña123', '123 Calle Principal', 0),
(68, 'Mr', 'X', 'it@example.com', 'contraseña123', '123 Calle Principal', 0),
(69, 'Mr', 'X', 'iti@example.com', 'contraseña123', '123 Calle Principal', 0),
(70, 'Mr', 'X', 'uti@example.com', 'contraseña123', '123 Calle Principal', 0),
(71, 'Mr', 'X', 'ati@example.com', 'contraseña123', '123 Calle Principal', 0),
(72, 'Mr', 'X', 'afi@example.com', 'contraseña123', '123 Calle Principal', 0),
(74, 'Mr', 'X', 'afa@example.com', 'contraseña123', '123 Calle Principal', 0),
(75, 'Mr', 'X', 'ala@example.com', 'contraseña123', '123 Calle Principal', 0),
(76, 'Mr', 'X', 'oa@example.com', 'contraseña123', '123 Calle Principal', 0),
(77, 'Mr', 'X', 'ola@example.com', 'contraseña123', '123 Calle Principal', 0),
(78, 'Mr', 'X', 'ol3@example.com', 'contraseña123', '123 Calle Principal', 0),
(79, 'Mr', 'X', 'oooo@example.com', 'contraseña123', '123 Calle Principal', 0),
(81, 'Mr', 'X', 'ooo@example.com', 'contraseña123', '123 Calle Principal', 0),
(83, 'Mr', 'X', 'oowwo@example.com', 'contraseña123', '123 Calle Principal', 0),
(84, 'Mr', 'X', 'ooso@example.com', 'contraseña123', '123 Calle Principal', 0),
(85, 'Mr', 'X', 'oqqo@example.com', 'contraseña123', '123 Calle Principal', 0),
(86, 'Mr', 'X', 'oosqqso@example.com', 'contraseña123', '123 Calle Principal', 0),
(87, 'Mr', 'X', 'oosqqso@examplo.com', 'contraseña123', '123 Calle Principal', 0),
(88, 'Mr', 'X', 'oos1so@examplo.com', 'contraseña123', '123 Calle Principal', 0),
(89, 'Mr', 'X', 'os1so@examplo.com', 'contraseña123', '123 Calle Principal', 0),
(90, 'Mr', 'X', 'o1so@examplo.com', 'contraseña123', '123 Calle Principal', 0),
(91, 'Mr', 'X', 'oaso@examplo.com', 'contraseña123', '123 Calle Principal', 0),
(92, 'Mr', 'X', 'oalo@examplo.com', 'contraseña123', '123 Calle Principal', 0),
(93, 'Mr', 'X', 'oalo11@examplo.com', 'contraseña123', '123 Calle Principal', 0),
(95, 'Mr', 'X', 'oa1@examplo.com', 'contraseña123', '123 Calle Principal', 0),
(96, 'Mr', 'X', 'oa111@examplo.com', 'contraseña123', '123 Calle Principal', 0),
(98, 'Mr', 'X', 'wqqqa111@examplo.com', 'contraseña123', '123 Calle Principal', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_cliente` (`id_cliente`);

--
-- Indices de la tabla `pedido_producto`
--
ALTER TABLE `pedido_producto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `producto_id` (`producto_id`),
  ADD KEY `pedido_id` (`pedido_id`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `categoria_id` (`categoria_id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `correo` (`correo`),
  ADD KEY `tipo` (`tipo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administrador`
--
ALTER TABLE `administrador`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de la tabla `pedido`
--
ALTER TABLE `pedido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `pedido_producto`
--
ALTER TABLE `pedido_producto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD CONSTRAINT `administrador_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id`) ON DELETE SET NULL ON UPDATE NO ACTION;

--
-- Filtros para la tabla `pedido_producto`
--
ALTER TABLE `pedido_producto`
  ADD CONSTRAINT `pedido_producto_ibfk_1` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `pedido_producto_ibfk_2` FOREIGN KEY (`pedido_id`) REFERENCES `pedido` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`categoria_id`) REFERENCES `categoria` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
