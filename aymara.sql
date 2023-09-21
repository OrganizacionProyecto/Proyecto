
-- Schema aymara
CREATE SCHEMA IF NOT EXISTS `aymara` DEFAULT CHARACTER SET utf8 ;
USE `aymara` ;

-- Table `aymara`.`categoria`
CREATE TABLE IF NOT EXISTS `aymara`.`categoria` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

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

###xx_


-- Table `aymara`.`cliente`
CREATE TABLE IF NOT EXISTS `aymara`.`cliente` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `correo` VARCHAR(255) NOT NULL,
  `dni` INT(11) NOT NULL,
  `contrasenia` VARCHAR(255) NOT NULL,
  `domicilio` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- Table `aymara`.`pedido`
CREATE TABLE IF NOT EXISTS `aymara`.`pedido` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` INT(11) NOT NULL,
  `estado` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_usuario_idx` (`id_usuario` ASC),
  CONSTRAINT `id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `aymara`.`cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Table `aymara`.`pedido_producto`
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


