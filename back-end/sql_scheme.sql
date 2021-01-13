/*
e-Lectra Project by The Charging Aces:
~Stelios Kandylakis
~Margarita  Oikonomakou
~Kitsos     Orfanopoulos
~Vasilis    Papalexis
~Georgia    Stamou
~Dido       Stoikou

Softeng, ECE NTUA, 2021
*/

-- ---<<SQL code for creating our database schema>>--------------

DROP DATABASE IF EXISTS project_e_lectra;


-- ------------<DATABASE CREATION>--------------

CREATE DATABASE IF NOT EXISTS project_e_lectra;
USE project_e_lectra;

-- ------------<ENTITIES CREATION>--------------
-- ------------<1. ELECTRICITY PROVIDER>--------------
CREATE TABLE Provider (
  ProviderID int NOT NULL AUTO_INCREMENT,
  Name       varchar(100) NOT NULL,
  Phone      varchar(13) UNIQUE,
  Email      varchar(100) UNIQUE,
  Website    varchar(300) UNIQUE,
  PRIMARY KEY (ProviderID),
  UNIQUE INDEX (ProviderID),
  UNIQUE INDEX (Name));

  -- ------------<2. USER>----------------------------
CREATE TABLE User (
  UserID      int NOT NULL,
  Name        varchar(32) NOT NULL,
  Surname     varchar(32) NOT NULL,
  Birthdate   date NOT NULL,
  BonusPoints int DEFAULT 0 CHECK (BonusPoints>=0) NOT NULL,
  Phone       int UNIQUE,
  PRIMARY KEY (UserID),
  UNIQUE INDEX (UserID),
  INDEX (Surname));

  -- ------------<3. VEHICLE>--------------
CREATE TABLE Vehicle (
  VehicleID      bigint NOT NULL AUTO_INCREMENT,
  Brand          varchar(20) NOT NULL,
  Model          varchar(30) NOT NULL,
  ReleaseYear    year DEFAULT '2021',
  Type           varchar(10) DEFAULT 'BEV' NOT NULL comment 'CUV, SUV, truck, supercar, limo, 4x4 etc.',
  BatterySize    decimal(8,2) NOT NULL,
  CurrentBattery decimal(8,2) NOT NULL,
  UserID         int NOT NULL,
  PRIMARY KEY (VehicleID),
  UNIQUE INDEX (VehicleID),
  INDEX (Brand),
  INDEX (Model),
  INDEX (Type));

  -- ------------<4. STATUS OF THE CHARGING POINT>-------------- --Kitsos
  CREATE TABLE Status (
    StatusID      tinyint NOT NULL,
    StatusName    varchar(50) NOT NULL,
    IsOperational boolean NOT NULL CHECK (IsOperational in (0,1)),
    PRIMARY KEY (StatusID),
    UNIQUE INDEX (StatusID));

    -- ------------<5. CHARGING STATION>-------------- --Stelios
  CREATE TABLE Station (
    StationID    int NOT NULL AUTO_INCREMENT,
    Name         varchar(32) NOT NULL,
    Operator     varchar(30) NOT NULL,
    StationType  varchar(20) NOT NULL,
    Street       varchar(32) NOT NULL,
    StreetNumber smallint NOT NULL CHECK(StreetNumber>0),
    PostalCode   varchar(10),
    Town         varchar(32),
    Country      varchar(32),
    Latitude     decimal(10,8) CHECK (latitude>=-90 and latitude<=90) NOT NULL,
    Longitude    decimal(11,8) CHECK (longitude>=-90 and longitude<=90) NOT NULL,
    Phone        int CHECK (Phone>0),
    Email        varchar(255) UNIQUE,
    Website      varchar(255) UNIQUE,
    RatingStars  decimal(4,2) DEFAULT 5 CHECK (RatingStars>=0 AND RatingStars<=5) NOT NULL,
    TotalVotes   int DEFAULT 0 CHECK (TotalVotes>=0) NOT NULL,
    PRIMARY KEY (StationID),
    INDEX (Operator),
    INDEX (PostalCode),
    INDEX (Country)) ;

    -- ------------<6. CHARGING POINT>-------------- --Vasilis
    CREATE TABLE ChargingPoint (
      PointID    int NOT NULL AUTO_INCREMENT,
      StationID  int NOT NULL,
      PointType  varchar(10) DEFAULT 'AC2' NOT NULL,
      LastUpdate datetime NOT NULL UNIQUE,
      StatusID   tinyint NOT NULL,
      PRIMARY KEY (PointID, StationID), -- composite key
      FOREIGN KEY (StationID) REFERENCES Station(StationID)
      ON UPDATE CASCADE ON DELETE CASCADE, -- if station is deleted then the point will deleted too
      FOREIGN KEY (StatusID) REFERENCES Status(StatusID)
      ON UPDATE CASCADE ON DELETE RESTRICT, -- status can't be deleted if there are points with that status
      UNIQUE INDEX StationPointID(StationID, PointID));

      -- ------------<7. CHARGING SESSION>-------------- --Kitsos
CREATE TABLE Session (
  SessionID             bigint NOT NULL AUTO_INCREMENT,
  StartedOn             datetime NOT NULL,
  FinishedOn            datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  RequestedAmountOfTime smallint CHECK (RequestedAmountOfTime>=0),
  RequestedEnergy       decimal(10,3) CHECK (RequestedEnergy>=0),
  EnergyDeliverd        decimal(10,3) NOT NULL CHECK (EnergyDeliverd>=0),
  Protocol              varchar(10) NOT NULL,
  PaymentType           varchar(10) NOT NULL,
  PricePolicyRef        varchar(10) NOT NULL,
  CostPerKWh            decimal(10,4) NOT NULL CHECK (CostPerKWh>=0),
  SessionCost           decimal(10,2) NOT NULL CHECK (SessionCost>=0),
  BonusPointsRedeemed   int NOT NULL DEFAULT 0 CHECK(BonusPointsRedeemed>=0),
  BonusPointsGained     int NOT NULL DEFAULT 0 CHECK(BonusPointsGained>=0),
  VehicleID             bigint,
  StationPointID        int,
  ProviderID            int,
  PRIMARY KEY (SessionID),
  FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID)
  ON UPDATE CASCADE ON DELETE SET NULL, -- if vehicle is deleted the records will continue to show as NULL
  FOREIGN KEY (StationPointID) REFERENCES ChargingPoint(PointID)
  ON UPDATE CASCADE ON DELETE SET NULL, --  if the charging point is deleted the records will continue to show as NULL
  FOREIGN KEY (ProviderID) REFERENCES Provider(ProviderID)
  ON UPDATE CASCADE ON DELETE SET NULL);




ALTER TABLE Vehicle ADD CONSTRAINT FKVehicle960723 FOREIGN KEY (UserID) REFERENCES `User` (UserID);

alter table Provider add constraint chk_provider_email check (Provider.Email like '%_@_%._%');

alter table Provider add constraint chk_provider_website check (Provider.Website like 'https://_%._%');

alter table User add constraint chk_user_phone check (User.Phone like'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]');



