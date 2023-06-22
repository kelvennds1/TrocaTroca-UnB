SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';
CREATE SCHEMA IF NOT EXISTS `trocatroca1` ;
USE `trocatroca1` ;
CREATE TABLE IF NOT EXISTS `trocatroca1`.`person` (
  `idperson` INT NOT NULL AUTO_INCREMENT,
  `registration` VARCHAR(100) CHARACTER SET utf8 NULL,
  `passw` VARCHAR(1000) CHARACTER SET utf8 NULL,
  `name` VARCHAR(1000) CHARACTER SET utf8 NULL,
  `email` VARCHAR(1000) CHARACTER SET utf8 NULL,
  PRIMARY KEY (`idperson`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `trocatroca1`.`category` (
  `idcategory` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(450) CHARACTER SET utf8 NULL,
  `desc` VARCHAR(100) CHARACTER SET utf8 NULL,
  PRIMARY KEY (`idcategory`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `trocatroca1`.`item` (
  `iditem` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(450) CHARACTER SET utf8 NULL,
  `model_color` VARCHAR(450) CHARACTER SET utf8 NULL,
  `brand_species` VARCHAR(450) CHARACTER SET utf8 NULL,
  `year_acquired` VARCHAR(45) CHARACTER SET utf8 NULL,
  `desc` VARCHAR(1000) CHARACTER SET utf8 NULL,
  `condition` VARCHAR(450) CHARACTER SET utf8 NULL,
  `vaccines` VARCHAR(1000) CHARACTER SET utf8 NULL,
  `likes` VARCHAR(1000) CHARACTER SET utf8 NULL,
  `dislikes` VARCHAR(1000) CHARACTER SET utf8 NULL,
  `category_idcategory` INT NOT NULL,
  PRIMARY KEY (`iditem`, `category_idcategory`),
  INDEX `fk_object_category1_idx` (`category_idcategory` ASC),
  CONSTRAINT `fk_object_category1`
    FOREIGN KEY (`category_idcategory`)
    REFERENCES `trocatroca1`.`category` (`idcategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `trocatroca1`.`person_adv_donate_item` (
  `idpersonAdvDonateItem` INT NOT NULL AUTO_INCREMENT,
  `desc` VARCHAR(1000) CHARACTER SET utf8 NULL,
  `delivers` VARCHAR(45) CHARACTER SET utf8 NULL,
  `reason` VARCHAR(450) CHARACTER SET utf8 NULL,
  `listed` VARCHAR(15) CHARACTER SET utf8 NULL,
  `person_idperson` INT NOT NULL,
  `item_iditem` INT NOT NULL,
  `item_category_idcategory` INT NOT NULL,
  PRIMARY KEY (`idpersonAdvDonateItem`, `person_idperson`, `item_iditem`, `item_category_idcategory`),
  INDEX `fk_person_adv_donate_item_item1_idx` (`item_iditem` ASC, `item_category_idcategory` ASC),
  CONSTRAINT `fk_person_adv_donate_item_person1`
    FOREIGN KEY (`person_idperson`)
    REFERENCES `trocatroca1`.`person` (`idperson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_person_adv_donate_item_item1`
    FOREIGN KEY (`item_iditem` , `item_category_idcategory`)
    REFERENCES `trocatroca1`.`item` (`iditem` , `category_idcategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `trocatroca1`.`country` (
  `idcountry` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) CHARACTER SET utf8 NULL,
  PRIMARY KEY (`idcountry`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `trocatroca1`.`FU` (
  `idFU` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) CHARACTER SET utf8 NULL,
  `country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idFU`, `country_idcountry`),
  INDEX `fk_FU_country1_idx` (`country_idcountry` ASC),
  CONSTRAINT `fk_FU_country1`
    FOREIGN KEY (`country_idcountry`)
    REFERENCES `trocatroca1`.`country` (`idcountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `trocatroca1`.`city` (
  `idcity` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) CHARACTER SET utf8 NULL,
  `FU_idFU` INT NOT NULL,
  `FU_country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idcity`, `FU_idFU`, `FU_country_idcountry`),
  INDEX `fk_city_FU2_idx` (`FU_idFU` ASC, `FU_country_idcountry` ASC),
  CONSTRAINT `fk_city_FU2`
    FOREIGN KEY (`FU_idFU` , `FU_country_idcountry`)
    REFERENCES `trocatroca1`.`FU` (`idFU` , `country_idcountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `trocatroca1`.`street` (
  `idstreet` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) CHARACTER SET utf8 NULL,
  `city_idcity` INT NOT NULL,
  `city_FU_idFU` INT NOT NULL,
  `city_FU_country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idstreet`, `city_idcity`, `city_FU_idFU`, `city_FU_country_idcountry`),
  INDEX `fk_street_city2_idx` (`city_idcity` ASC, `city_FU_idFU` ASC, `city_FU_country_idcountry` ASC),
  CONSTRAINT `fk_street_city2`
    FOREIGN KEY (`city_idcity` , `city_FU_idFU` , `city_FU_country_idcountry`)
    REFERENCES `trocatroca1`.`city` (`idcity` , `FU_idFU` , `FU_country_idcountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `trocatroca1`.`address` (
  `idaddress` INT NOT NULL AUTO_INCREMENT,
  `number` VARCHAR(45) CHARACTER SET utf8 NULL,
  `desc` VARCHAR(1000) CHARACTER SET utf8 NULL,
  `street_idstreet` INT NOT NULL,
  `street_city_idcity` INT NOT NULL,
  `street_city_FU_idFU` INT NOT NULL,
  `street_city_FU_country_idcountry` INT NOT NULL,
  `person_idpessoa` INT NOT NULL,
  PRIMARY KEY (`idaddress`, `street_idstreet`, `street_city_idcity`, `street_city_FU_idFU`, `street_city_FU_country_idcountry`, `person_idpessoa`),
  INDEX `fk_address_street1_idx` (`street_idstreet` ASC, `street_city_idcity` ASC, `street_city_FU_idFU` ASC, `street_city_FU_country_idcountry` ASC),
  INDEX `fk_address_person1_idx` (`person_idpessoa` ASC),
  CONSTRAINT `fk_address_street1`
    FOREIGN KEY (`street_idstreet` , `street_city_idcity` , `street_city_FU_idFU` , `street_city_FU_country_idcountry`)
    REFERENCES `trocatroca1`.`street` (`idstreet` , `city_idcity` , `city_FU_idFU` , `city_FU_country_idcountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_address_person1`
    FOREIGN KEY (`person_idpessoa`)
    REFERENCES `trocatroca1`.`person` (`idperson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS `trocatroca1`.`person_adv_exch_item` (
  `idpersonAdvExchItem` INT NOT NULL AUTO_INCREMENT,
  `desc` VARCHAR(1000) CHARACTER SET utf8 NULL,
  `delivers` VARCHAR(45) CHARACTER SET utf8 NULL,
  `reason` VARCHAR(450) CHARACTER SET utf8 NULL,
  `listed` VARCHAR(15) CHARACTER SET utf8 NULL,
  `market_price` VARCHAR(45) CHARACTER SET utf8 NULL,
  `person_idperson` INT NOT NULL,
  `item_iditem` INT NOT NULL,
  `item_category_idcategory` INT NOT NULL,
  PRIMARY KEY (`idpersonAdvExchItem`, `person_idperson`, `item_iditem`, `item_category_idcategory`),
  INDEX `fk_person_adv_exch_item0_person1_idx` (`person_idperson` ASC),
  INDEX `fk_person_adv_exch_item_item1_idx` (`item_iditem` ASC, `item_category_idcategory` ASC),
  CONSTRAINT `fk_person_adv_exch_item0_person1`
    FOREIGN KEY (`person_idperson`)
    REFERENCES `trocatroca1`.`person` (`idperson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_person_adv_exch_item_item1`
    FOREIGN KEY (`item_iditem` , `item_category_idcategory`)
    REFERENCES `trocatroca1`.`item` (`iditem` , `category_idcategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `trocatroca1` ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
