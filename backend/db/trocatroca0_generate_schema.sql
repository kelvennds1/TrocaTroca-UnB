-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema trocatroca0
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Table `trocatroca0`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca0`.`category` (
  `idcategory` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(450) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `desc` VARCHAR(100) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`idcategory`))
ENGINE = InnoDB
AUTO_INCREMENT = 3;
-- -----------------------------------------------------
-- Schema trocatroca0
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `trocatroca0` ;
USE `trocatroca0` ;

-- -----------------------------------------------------
-- Table `trocatroca0`.`person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca0`.`person` (
  `idperson` INT NOT NULL AUTO_INCREMENT,
  `registration` VARCHAR(100) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `passw` VARCHAR(1000) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `name` VARCHAR(1000) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `email` VARCHAR(1000) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`idperson`))
ENGINE = InnoDB
AUTO_INCREMENT = 3;


-- -----------------------------------------------------
-- Table `trocatroca0`.`item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca0`.`item` (
  `iditem` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(450) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `image_path` VARCHAR(450) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  -- `image_blob` LONGBLOB NULL DEFAULT NULL,
  `model_color` VARCHAR(450) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `brand_species` VARCHAR(450) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `year_acquired` VARCHAR(45) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `desc` VARCHAR(1000) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `condition` VARCHAR(450) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `vaccines` VARCHAR(1000) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `likes` VARCHAR(1000) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `dislikes` VARCHAR(1000) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `category_idcategory` INT NOT NULL,
  PRIMARY KEY (`iditem`, `category_idcategory`),
  INDEX `fk_object_category1_idx` (`category_idcategory` ASC),
  CONSTRAINT `fk_object_category1`
    FOREIGN KEY (`category_idcategory`)
    REFERENCES `trocatroca0`.`category` (`idcategory`))
ENGINE = InnoDB
AUTO_INCREMENT = 3;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



CREATE TABLE IF NOT EXISTS swap (
    idswap INT NOT NULL AUTO_INCREMENT,
    p1kGive VARCHAR(1000) NOT NULL,
    p1kReceive VARCHAR(1000) NOT NULL,
    p2kGive VARCHAR(1000),
    p2kReceive VARCHAR(1000),
    time_created DATETIME DEFAULT CONVERT_TZ(NOW(),'UTC','America/Sao_Paulo'),
    PRIMARY KEY (idswap)
) ENGINE = InnoDB
AUTO_INCREMENT = 3;

alter table person_adv_donate_item rename column item_category_idcategory to
category_idcategory;


ALTER TABLE `trocatroca0`.`item`
ADD COLUMN `time_created` DATETIME DEFAULT CONVERT_TZ(NOW(),'UTC','America/Sao_Paulo');