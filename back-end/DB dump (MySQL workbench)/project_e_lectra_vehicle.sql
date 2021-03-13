-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: project_e_lectra
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `VehicleID` bigint NOT NULL AUTO_INCREMENT,
  `Brand` varchar(20) NOT NULL,
  `Model` varchar(30) NOT NULL,
  `ReleaseYear` year DEFAULT '2021',
  `Type` varchar(10) NOT NULL DEFAULT 'BEV',
  `BatterySize` decimal(8,2) NOT NULL,
  `CurrentBattery` decimal(8,2) NOT NULL,
  `UserID` int NOT NULL,
  PRIMARY KEY (`VehicleID`),
  UNIQUE KEY `VehicleID` (`VehicleID`),
  KEY `UserID` (`UserID`),
  KEY `Brand` (`Brand`),
  KEY `Model` (`Model`),
  KEY `Type` (`Type`),
  CONSTRAINT `vehicle_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `vehicle_chk_1` CHECK ((`Type` in (_utf8mb4'PHEV',_utf8mb4'BEV',_utf8mb4'FCEV'))),
  CONSTRAINT `vehicle_chk_2` CHECK ((`BatterySize` <= 100.00)),
  CONSTRAINT `vehicle_chk_3` CHECK ((`CurrentBattery` <= 100.00))
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES (1,'Tesla','ev00',2019,'PHEV',17.00,46.00,13),(2,'Opel','ev01',2020,'BEV',17.00,36.00,24),(3,'VolksWagen','ev04',2012,'FCEV',15.00,18.00,10),(4,'Porche','ev05',2014,'FCEV',17.00,54.00,19),(5,'Ford','ev00',2014,'FCEV',22.00,74.00,4),(6,'VolksWagen','ev02',2021,'PHEV',31.00,65.00,9),(7,'Skoda','ev00',2019,'PHEV',30.00,92.00,16),(8,'Buggati','ev01',2017,'PHEV',29.00,87.00,3),(9,'Tesla','ev05',2009,'BEV',32.00,69.00,16),(10,'Opel','ev00',2011,'BEV',29.00,32.00,9),(11,'VolksWagen','ev03',2018,'PHEV',25.00,50.00,20),(12,'Porche','ev02',2018,'FCEV',30.00,46.00,10),(13,'Ford','ev00',2017,'PHEV',23.00,72.00,14),(14,'VolksWagen','ev02',2013,'BEV',24.00,25.00,19),(15,'Skoda','ev02',2012,'FCEV',26.00,43.00,24),(16,'Buggati','ev00',2015,'FCEV',99.00,77.00,23),(17,'Tesla','ev01',2016,'FCEV',74.00,82.00,23),(18,'Opel','ev04',2009,'PHEV',82.00,94.00,8),(19,'VolksWagen','ev05',2021,'PHEV',62.00,23.00,9),(20,'Porche','ev00',2011,'PHEV',82.00,66.00,20),(21,'Ford','ev02',2011,'BEV',69.00,57.00,17),(22,'VolksWagen','ev00',2021,'BEV',17.00,25.00,20),(23,'Skoda','ev01',2016,'PHEV',14.00,30.00,14),(24,'Buggati','ev05',2015,'FCEV',14.00,68.00,18),(25,'Tesla','ev00',2013,'PHEV',14.00,41.00,10),(26,'Opel','ev03',2010,'BEV',25.00,39.00,19),(27,'VolksWagen','ev02',2015,'FCEV',30.00,23.00,16),(28,'Porche','ev00',2016,'FCEV',27.00,43.00,1),(29,'Ford','ev02',2010,'FCEV',25.00,23.00,13),(30,'VolksWagen','ev02',2012,'PHEV',27.00,73.00,8),(31,'Skoda','ev00',2011,'PHEV',27.00,72.00,24),(32,'Buggati','ev01',2011,'PHEV',24.00,88.00,1),(33,'Tesla','ev04',2009,'BEV',25.00,23.00,11),(34,'Opel','ev05',2020,'BEV',30.00,57.00,15),(35,'VolksWagen','ev00',2011,'PHEV',24.00,97.00,14);
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-14  1:22:09
