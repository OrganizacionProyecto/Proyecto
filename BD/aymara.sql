

-- Schema aymara
CREATE SCHEMA IF NOT EXISTS `aymara` DEFAULT CHARACTER SET utf8 ;
USE `aymara` ;

CREATE TABLE IF NOT EXISTS `aymara`.`usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `contrasenia` varchar(255) NOT NULL,
  `domicilio` varchar(255) NOT NULL,
  `tipo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- Table `aymara`.`categoria`
CREATE TABLE IF NOT EXISTS `aymara`.`categoria` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

INSERT INTO `aymara`.`categoria` (`nombre`) VALUES
('Suplementos Dietarios'),
('Hierbas medicinales y te'),
('Alimentos dieteticos');

-- Table `aymara`.`producto`
CREATE TABLE IF NOT EXISTS `aymara`.`producto` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `descripcion` TEXT NOT NULL,
  `precio` DECIMAL(10, 2) NOT NULL,
  `imagen` VARCHAR(255) NULL,
  `stock` INT(11) NOT NULL,
  `categoria_id` INT(11) NULL,
  PRIMARY KEY (`id`),
  INDEX `categoria_id_idx` (`categoria_id` ASC),
  CONSTRAINT `categoria_id`
    FOREIGN KEY (`categoria_id`)
    REFERENCES `aymara`.`categoria` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

INSERT INTO `aymara`.`producto` (`nombre`, `descripcion`, `precio`, `stock`, `categoria_id`) VALUES
('Aceite de coco organico', 'Suplemento dietario a base de aceite de coco. 100% natural. Fortificado con vitamina A, E y D. Sabor original. Presentación 380 cc', 5200.99, 55, 1),
('Café Verde Plus', 'Suplemento dietario a base de café verde, vitamina B6, L-carnitina, té verde y garcinia cambogia.Ingesta diario recomendada 2 a 4 comprimidos por día. Presentación 60 comprimidos', 4436.00, 75, 1),
('Garcimax Slim', 'Suplemento dietario natural de heirbas (garcinia cambogia, fucus vesiculoso, té verde y café verde) y vitamina B1. Ingesta diaria recomendada 2 comprimidos diarios con abundante agua media hora antes de cada comida principal.Presentación 60 comprimidos', 2504.00, 50, 1);

-- Table `aymara`.`cliente`
CREATE TABLE IF NOT EXISTS `aymara`.`cliente` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_usuario` INT(11) NOT NULL,
	FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE,
  `dni` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_usuario_idx` (`id_usuario` ASC),
  CONSTRAINT `id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `aymara`.`usuario` (`id`)
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `aymara`.`administrador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_usuario_idx` (`id_usuario` ASC),
  CONSTRAINT `fk_admin_usuario` -- Cambia el nombre a uno único
    FOREIGN KEY (`id_usuario`)
    REFERENCES `aymara`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `administrador`
--

-- Table `aymara`.`pedido`
CREATE TABLE IF NOT EXISTS `aymara`.`pedido` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` INT(11) NOT NULL,
  `estado` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_usuario_idx` (`id_usuario` ASC),
  CONSTRAINT `fk_pedido_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `aymara`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;



CREATE TABLE IF NOT EXISTS `aymara`.`pedido_producto` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `pedido_id` INT(11) NULL,
  `producto_id` INT(11) NULL,
  PRIMARY KEY (`id`),
  INDEX `pedido_id_idx` (`pedido_id` ASC),
  INDEX `producto_id_idx` (`producto_id` ASC),
  CONSTRAINT `pedido_id`
    FOREIGN KEY (`pedido_id`)
    REFERENCES `aymara`.`pedido` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `producto_id`
    FOREIGN KEY (`producto_id`)
    REFERENCES `aymara`.`producto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;




