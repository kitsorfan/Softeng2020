
/* -- DROP IF RESET IS NEEDED

ALTER TABLE Vehicle DROP FOREIGN KEY FKVehicle960723;
ALTER TABLE `Session` DROP FOREIGN KEY FKSession61705;
ALTER TABLE `Session` DROP FOREIGN KEY FKSession967689;
ALTER TABLE `Session` DROP FOREIGN KEY FKSession916250;
ALTER TABLE Point DROP FOREIGN KEY FKPoint351783;
ALTER TABLE Point DROP FOREIGN KEY FKPoint28372;
DROP TABLE IF EXISTS Point;
DROP TABLE IF EXISTS Provider;
DROP TABLE IF EXISTS `Session`;
DROP TABLE IF EXISTS Station;
DROP TABLE IF EXISTS Status;
DROP TABLE IF EXISTS `User`;
DROP TABLE IF EXISTS Vehicle;

-- OR THE WHOLE DB
DROP DATABASE IF EXISTS project_e_lectra;
*/

-- ---<<SQL code for creating our database schema>>--------------
-- ------------<DATABASE CREATION>--------------

CREATE DATABASE IF NOT EXISTS project_e_lectra;
USE project_e_lectra;

-- ------------<ENTITIES CREATION>--------------
CREATE TABLE Point (
  PointID    int NOT NULL,
  StationID  int NOT NULL,
  Type       varchar(10) DEFAULT 'AC2' NOT NULL,
  LastUpdate timestamp NOT NULL UNIQUE,
  StatusID   tinyint NOT NULL,
  PRIMARY KEY (PointID,
  StationID),
  INDEX (StationID));

CREATE TABLE Provider (
  ProviderID int NOT NULL AUTO_INCREMENT,
  Name       varchar(100) NOT NULL,
  Phone      varchar(13) UNIQUE,
  Email      varchar(100) UNIQUE,
  Website    varchar(300) UNIQUE,
  PRIMARY KEY (ProviderID),
  UNIQUE INDEX (ProviderID),
  UNIQUE INDEX (Name));

CREATE TABLE `Session` (
  SessionID             bigint NOT NULL,
  StartedOn             timestamp NOT NULL,
  FinishedOn            timestamp NOT NULL,
  RequestedAmountOfTime smallint,
  RequestedEnergy       float,
  EnergyDeliverd        float NOT NULL,
  Protocol              varchar(10) NOT NULL,
  PaymentType           varchar(10) NOT NULL,
  PricePolicyRef        varchar(10) NOT NULL,
  CostPerKWh            float NOT NULL,
  SessionCost           float NOT NULL,
  BonusPointsRedeemed   int NOT NULL,
  BonusPointsGained     int NOT NULL,
  VehicleID             bigint NOT NULL,
  PointID               int NOT NULL,
  ProviderID            int NOT NULL,
  PointStationID        int NOT NULL,
  PointStationID2       int NOT NULL,
  PRIMARY KEY (SessionID));

CREATE TABLE Station (
  StationID    int NOT NULL AUTO_INCREMENT,
  Name         varchar(32),
  Operator     varchar(30) NOT NULL,
  StationType  varchar(20) NOT NULL comment 'Public, Private, military, etc.',
  Street       varchar(32) NOT NULL,
  StreetNumber smallint NOT NULL,
  PostalCode   varchar(10),
  Town         varchar(32),
  Country      varchar(32),
  Latitude     double NOT NULL,
  Longitude    double NOT NULL,
  Phone        varchar(13),
  Email        varchar(255) UNIQUE,
  Website      varchar(255) UNIQUE,
  RatingStars  float DEFAULT 5 NOT NULL comment 'For users'' rating system, from 1 to 5, with one decimal',
  TotalVotes   int DEFAULT 0 NOT NULL,
  PRIMARY KEY (StationID),
  UNIQUE INDEX (Operator),
  INDEX (PostalCode),
  INDEX (Country));


CREATE TABLE Status (
  StatusID      tinyint NOT NULL,
  StatusName    varchar(50) NOT NULL,
  IsOperational boolean NOT NULL,
  PRIMARY KEY (StatusID),
  UNIQUE INDEX (StatusID));

CREATE TABLE `User` (
  UserID      int NOT NULL AUTO_INCREMENT,
  Name        varchar(32) NOT NULL,
  Surname     varchar(32) NOT NULL,
  Birthdate   date NOT NULL,
  BonusPoints int DEFAULT 0 NOT NULL comment 'Bonus Points >0' 	,
  Phone       int UNIQUE,
  PRIMARY KEY (UserID),
  UNIQUE INDEX (UserID),
  INDEX (Surname));

CREATE TABLE Vehicle (
  VehicleID      bigint NOT NULL AUTO_INCREMENT,
  Brand          varchar(20) NOT NULL,
  Model          varchar(30) NOT NULL,
  ReleaseYear    year DEFAULT '2021',
  Type           varchar(10) DEFAULT 'BEV' NOT NULL comment 'CUV, SUV, truck, supercar, limo, 4x4 etc.',
  BatterySize    float NOT NULL,
  CurrentBattery float NOT NULL,
  UserID         int NOT NULL,
  PRIMARY KEY (VehicleID),
  UNIQUE INDEX (VehicleID),
  INDEX (Brand),
  INDEX (Model),
  INDEX (Type));

ALTER TABLE Vehicle ADD CONSTRAINT FKVehicle960723 FOREIGN KEY (UserID) REFERENCES `User` (UserID);
ALTER TABLE `Session` ADD CONSTRAINT FKSession61705 FOREIGN KEY (VehicleID) REFERENCES Vehicle (VehicleID);
ALTER TABLE `Session` ADD CONSTRAINT FKSession967689 FOREIGN KEY (PointID, PointStationID2) REFERENCES Point (PointID, StationID);
ALTER TABLE `Session` ADD CONSTRAINT FKSession916250 FOREIGN KEY (ProviderID) REFERENCES Provider (ProviderID);
ALTER TABLE Point ADD CONSTRAINT FKPoint351783 FOREIGN KEY (StatusID) REFERENCES Status (StatusID);
ALTER TABLE Point ADD CONSTRAINT FKPoint28372 FOREIGN KEY (StationID) REFERENCES Station (StationID);
