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
-- Schema trocatroca0
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `trocatroca0` ;
USE `trocatroca0` ;

-- -----------------------------------------------------
-- Table `trocatroca0`.`country`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca0`.`country` (
  `idcountry` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`idcountry`))
ENGINE = InnoDB
AUTO_INCREMENT = 3;


-- -----------------------------------------------------
-- Table `trocatroca0`.`FU`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca0`.`FU` (
  `idFU` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idFU`, `country_idcountry`),
  INDEX `fk_FU_country1_idx` (`country_idcountry` ASC),
  CONSTRAINT `fk_FU_country1`
    FOREIGN KEY (`country_idcountry`)
    REFERENCES `trocatroca0`.`country` (`idcountry`))
ENGINE = InnoDB
AUTO_INCREMENT = 3;


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
-- Table `trocatroca0`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca0`.`city` (
  `idcity` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `FU_idFU` INT NOT NULL,
  `FU_country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idcity`, `FU_idFU`, `FU_country_idcountry`),
  INDEX `fk_city_FU2_idx` (`FU_idFU` ASC, `FU_country_idcountry` ASC),
  CONSTRAINT `fk_city_FU2`
    FOREIGN KEY (`FU_idFU` , `FU_country_idcountry`)
    REFERENCES `trocatroca0`.`FU` (`idFU` , `country_idcountry`))
ENGINE = InnoDB
AUTO_INCREMENT = 3;


-- -----------------------------------------------------
-- Table `trocatroca0`.`street`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca0`.`street` (
  `idstreet` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `city_idcity` INT NOT NULL,
  `city_FU_idFU` INT NOT NULL,
  `city_FU_country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idstreet`, `city_idcity`, `city_FU_idFU`, `city_FU_country_idcountry`),
  INDEX `fk_street_city2_idx` (`city_idcity` ASC, `city_FU_idFU` ASC, `city_FU_country_idcountry` ASC),
  CONSTRAINT `fk_street_city2`
    FOREIGN KEY (`city_idcity` , `city_FU_idFU` , `city_FU_country_idcountry`)
    REFERENCES `trocatroca0`.`city` (`idcity` , `FU_idFU` , `FU_country_idcountry`))
ENGINE = InnoDB
AUTO_INCREMENT = 3;


-- -----------------------------------------------------
-- Table `trocatroca0`.`address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca0`.`address` (
  `idaddress` INT NOT NULL AUTO_INCREMENT,
  `number` VARCHAR(45) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `desc` VARCHAR(1000) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `street_idstreet` INT NOT NULL,
  `street_city_idcity` INT NOT NULL,
  `street_city_FU_idFU` INT NOT NULL,
  `street_city_FU_country_idcountry` INT NOT NULL,
  `person_idperson` INT NOT NULL,
  PRIMARY KEY (`idaddress`, `street_idstreet`, `street_city_idcity`, `street_city_FU_idFU`, `street_city_FU_country_idcountry`, `person_idperson`),
  INDEX `fk_address_street1_idx` (`street_idstreet` ASC, `street_city_idcity` ASC, `street_city_FU_idFU` ASC, `street_city_FU_country_idcountry` ASC),
  INDEX `fk_address_person1_idx` (`person_idperson` ASC),
  CONSTRAINT `fk_address_person1`
    FOREIGN KEY (`person_idperson`)
    REFERENCES `trocatroca0`.`person` (`idperson`),
  CONSTRAINT `fk_address_street1`
    FOREIGN KEY (`street_idstreet` , `street_city_idcity` , `street_city_FU_idFU` , `street_city_FU_country_idcountry`)
    REFERENCES `trocatroca0`.`street` (`idstreet` , `city_idcity` , `city_FU_idFU` , `city_FU_country_idcountry`))
ENGINE = InnoDB
AUTO_INCREMENT = 3;


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
-- Table `trocatroca0`.`item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca0`.`item` (
  `iditem` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(450) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `image_path` VARCHAR(450) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `image_blob` LONGBLOB NULL DEFAULT NULL,
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


-- -----------------------------------------------------
-- Table `trocatroca0`.`person_adv_donate_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca0`.`person_adv_donate_item` (
  `idpersonAdvDonateItem` INT NOT NULL AUTO_INCREMENT,
  `desc` VARCHAR(1000) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `delivers` VARCHAR(45) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `reason` VARCHAR(450) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `listed` VARCHAR(15) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `person_idperson` INT NOT NULL,
  `item_iditem` INT NOT NULL,
  `item_category_idcategory` INT NOT NULL,
  PRIMARY KEY (`idpersonAdvDonateItem`, `person_idperson`, `item_iditem`, `item_category_idcategory`),
  INDEX `fk_person_adv_donate_item_item1_idx` (`item_iditem` ASC, `item_category_idcategory` ASC),
  INDEX `fk_person_adv_donate_item_person1` (`person_idperson` ASC),
  CONSTRAINT `fk_person_adv_donate_item_item1`
    FOREIGN KEY (`item_iditem` , `item_category_idcategory`)
    REFERENCES `trocatroca0`.`item` (`iditem` , `category_idcategory`),
  CONSTRAINT `fk_person_adv_donate_item_person1`
    FOREIGN KEY (`person_idperson`)
    REFERENCES `trocatroca0`.`person` (`idperson`))
ENGINE = InnoDB
AUTO_INCREMENT = 3;


-- -----------------------------------------------------
-- Table `trocatroca0`.`person_adv_exch_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca0`.`person_adv_exch_item` (
  `idpersonAdvExchItem` INT NOT NULL AUTO_INCREMENT,
  `desc` VARCHAR(1000) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `delivers` VARCHAR(45) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `reason` VARCHAR(450) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `listed` VARCHAR(15) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `market_price` VARCHAR(45) COLLATE 'utf8mb3_general_ci' NULL DEFAULT NULL,
  `person_idperson` INT NOT NULL,
  `item_iditem` INT NOT NULL,
  `item_category_idcategory` INT NOT NULL,
  PRIMARY KEY (`idpersonAdvExchItem`, `person_idperson`, `item_iditem`, `item_category_idcategory`),
  INDEX `fk_person_adv_exch_item0_person1_idx` (`person_idperson` ASC),
  INDEX `fk_person_adv_exch_item_item1_idx` (`item_iditem` ASC, `item_category_idcategory` ASC),
  CONSTRAINT `fk_person_adv_exch_item0_person1`
    FOREIGN KEY (`person_idperson`)
    REFERENCES `trocatroca0`.`person` (`idperson`),
  CONSTRAINT `fk_person_adv_exch_item_item1`
    FOREIGN KEY (`item_iditem` , `item_category_idcategory`)
    REFERENCES `trocatroca0`.`item` (`iditem` , `category_idcategory`))
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
ALTER TABLE `trocatroca0`.`person_adv_donate_item`
ADD COLUMN `time_created` DATETIME DEFAULT CONVERT_TZ(NOW(),'UTC','America/Sao_Paulo');
ALTER TABLE `trocatroca0`.`person_adv_exch_item`
ADD COLUMN `time_created` DATETIME DEFAULT CONVERT_TZ(NOW(),'UTC','America/Sao_Paulo');
ALTER TABLE `trocatroca0`.`item`