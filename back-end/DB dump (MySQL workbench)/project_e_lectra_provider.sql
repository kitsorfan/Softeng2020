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
-- Table structure for table `provider`
--

DROP TABLE IF EXISTS `provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provider` (
  `ProviderID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Phone` bigint DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Website` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`ProviderID`),
  UNIQUE KEY `ProviderID` (`ProviderID`),
  UNIQUE KEY `Name` (`Name`),
  UNIQUE KEY `Phone` (`Phone`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `Website` (`Website`),
  CONSTRAINT `provider_chk_1` CHECK ((`Email` like _utf8mb4'%_@_%._%')),
  CONSTRAINT `provider_chk_2` CHECK ((`Website` like _utf8mb4'https://_%._%'))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provider`
--

LOCK TABLES `provider` WRITE;
/*!40000 ALTER TABLE `provider` DISABLE KEYS */;
INSERT INTO `provider` VALUES (1,'dei',8009001000,NULL,'https://www.dei.gr/'),(2,'heron',18288,'customercare@heron.gr','https://www.heron.gr/'),(3,'Protergia',18311,NULL,'https://www.protergia.gr/'),(4,'volton',11300,'cs@volton.gr','https://volton.gr/'),(5,'zenith',18321,'info@zenith.gr','https://www.zenith.gr/'),(6,'energa',11218,'info@energa.gr','https://www.energa.gr/');
/*!40000 ALTER TABLE `provider` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-14  1:22:10
