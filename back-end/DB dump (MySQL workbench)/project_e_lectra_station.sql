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
-- Table structure for table `station`
--

DROP TABLE IF EXISTS `station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `station` (
  `StationID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(32) NOT NULL,
  `Operator` varchar(30) NOT NULL,
  `StationType` varchar(20) NOT NULL,
  `Street` varchar(32) NOT NULL,
  `StreetNumber` smallint NOT NULL,
  `PostalCode` varchar(10) DEFAULT NULL,
  `Town` varchar(32) DEFAULT NULL,
  `Country` varchar(32) DEFAULT NULL,
  `Latitude` decimal(10,8) NOT NULL,
  `Longitude` decimal(11,8) NOT NULL,
  `Phone` bigint DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Website` varchar(255) DEFAULT NULL,
  `RatingStars` decimal(4,2) NOT NULL DEFAULT '5.00',
  `TotalVotes` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`StationID`),
  UNIQUE KEY `StationID` (`StationID`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `Website` (`Website`),
  KEY `Operator` (`Operator`),
  KEY `PostalCode` (`PostalCode`),
  KEY `Country` (`Country`),
  CONSTRAINT `station_chk_1` CHECK ((`StreetNumber` > 0)),
  CONSTRAINT `station_chk_2` CHECK (((`latitude` >= -(90)) and (`latitude` <= 90))),
  CONSTRAINT `station_chk_3` CHECK (((`longitude` >= -(180)) and (`longitude` <= 180))),
  CONSTRAINT `station_chk_4` CHECK ((`Phone` > 0)),
  CONSTRAINT `station_chk_5` CHECK ((`Email` like _utf8mb4'%_@_%._%')),
  CONSTRAINT `station_chk_6` CHECK ((`Website` like _utf8mb4'https://_%._%')),
  CONSTRAINT `station_chk_7` CHECK (((`RatingStars` >= 0) and (`RatingStars` <= 5))),
  CONSTRAINT `station_chk_8` CHECK ((`TotalVotes` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `station`
--

LOCK TABLES `station` WRITE;
/*!40000 ALTER TABLE `station` DISABLE KEYS */;
INSERT INTO `station` VALUES (1,'E-Autonomous Vehicle Charger','Stella Kolokotronis','commercial','Poseidonos',2,'92903','Irakleio','Greece',38.39212400,23.86940100,2234337591,'lordpapadakis1956@hotmail.eu','https://telnet.legal.softeng.in.mp3',4.23,195),(2,'Public Home','Xenia Oikonomou','public','Dionisiou Aeropagitou',113,'82531','Drama','Greece',38.16058400,21.73940100,1197196255,'faviconsupertroll2020@protonmail.gr','https://telnet.filesystem.softeng.met.xlm',1.74,41),(3,'Electric Car Plugin','Vasilis Loulakis','public','Agiou Alexandrou',221,'63154','Patra','Greece',38.61335400,22.23972100,4425784218,'faviconellada2019@hotmail.in','https://www2.mama.home.it.html',2.10,199),(4,'National Vehicle Charger','Makis Anastasiou','public','Peiraios',53,'47011','Trikala','Greece',39.32150400,22.19731100,5981805215,'giorgosforthewin1941@gmail.it','https://www2.poetry.softeng.com.ddl',2.68,59),(5,'Electric Car','Giorgos Kolokotronis','public','Axilleos',196,'14770','Alexandroupoli','Greece',38.24930400,23.01267100,8313237714,'mariarandom1991@mail.ntua.gr','https://snr.filesystem.mechan.com.html',2.50,19),(6,'Military Home','Maria Takoroni','military','Dionisiou Aeropagitou',139,'55925','Karditsa','Greece',39.47077400,21.70693100,4758571566,'userpapadakis2019@yahoo.gov','https://www.filesystem.ece.ntua.met.mp4',2.87,21),(7,'Super Car Plugin','Makis Papadopoulos','private','Oulof Palme',228,'14803','Alexandroupoli','Greece',38.84598400,22.30828100,1190864965,'giannispapadakis2003@mailfence.gov','https://email.webpage.ece.ntua.ger.xlm',1.05,89),(8,'My Vehicle Charger','Giorgos Sotiropoulos','military','Vasileos Konstantinou',186,'36991','Patra','Greece',38.64783400,23.19435100,5530139749,'marialove1958@info.gr','https://www2.mama.ntua.com.xlm',4.07,177),(9,'BP Car Plugin','Stella Sotiropoulos','commercial','Ermou',82,'54523','Larisa','Greece',37.55548400,22.40712100,4904620736,'providerlove2016@yahoo.us','https://www.starwars.ntua.com.mp4',1.79,77),(10,'National Home','Kostas Papadakis','private','Kokkinopoulou',136,'82132','Alexandroupoli','Greece',37.39079400,21.25529100,5669379636,'providerforthewin1983@info.com','https://www.bing.ece.ntua.eu.mp4',3.01,126),(11,'Military Home','Kostas Anastasiou','public','Katexaki',141,'20024','Drama','Greece',38.86032400,22.89858100,3951660530,'giorgosmaestros1962@info.com','https://www.poetry.home.us.html',1.99,37),(12,'My Home','Giorgos Papadopoulos','private','Peiraios',42,'88474','Drama','Greece',38.17912400,21.95961100,3013024752,'providersupertroll1994@info.ger','https://www2.starwars.ntua.us.htm',2.21,105),(13,'BP Station','Vasilis Loulakis','commercial','Oulof Palme',190,'55475','Lamia','Greece',38.47031400,21.56693100,1647243090,'mariasupertroll1962@hotmail.com','https://www.legal.ece.ntua.gov.ddl',2.52,52),(14,'Military Station','Marios Kapodistrias','public','Agiou Alexandrou',251,'88678','Livadia','Greece',38.78931400,21.79458100,1473345163,'faviconpapadakis2011@info.com','https://email.fancy.ntua.uk.ddl',2.20,94),(15,'Public Home','Stella Papadopoulos','military','Sotiros',251,'68910','Karditsa','Greece',38.90009400,21.18781100,1477753168,'providersupertroll2012@info.gr','https://telnet.legal.ece.ntua.uk.pdf',2.33,27),(16,'Euro Car','Maria Kolokotronis','commercial','Vasileos Konstantinou',107,'53558','Larisa','Greece',38.90318400,21.48098100,9211244112,'userforthewin1998@yahoo.gr','https://www2.webpage.mechan.uk.mp3',4.67,174),(17,'Electric Home','Stella Papadakis','private','Sotiros',194,'70861','Karditsa','Greece',37.89668400,22.57672100,4608848752,'faviconrandom1973@ece.ntua.uk','https://telnet.poetry.home.gr.pdf',2.70,30),(18,'Electric Vehicle Charger','Giorgos Kolokotronis','public','Taxiarxon',149,'47336','Drama','Greece',37.60177400,21.28278100,7236239219,'johnlove2017@mailfence.uk','https://telnet.poetry.softeng.met.ddl',2.60,147),(19,'My Station','Marios Sotiropoulos','military','Axilleos',43,'21581','Trikala','Greece',37.96464400,21.78126100,4377055328,'lordlove1981@protonmail.gr','https://email.starwars.home.gr.ddl',3.01,195),(20,'BP Car Plugin','Maria Loulakis','public','Thiseos',198,'35848','Trikala','Greece',38.41427400,22.64586100,5753421786,'johnlove1954@outlook.met','https://www2.minister.ntua.gov.xlm',2.59,56),(21,'E-Autonomous Home','Stella Kolokotronis','commercial','Bouboulinas',65,'18561','Thessaloniki','Greece',37.67037400,23.40537100,8490523231,'faviconlove1955@info.gov','https://telnet.legal.mechan.gr.json',0.50,129),(22,'Super Car Plugin','Stella Kolokotronis','private','Syggrou',85,'85147','Drama','Greece',39.16934400,22.48029100,2440696199,'providerellada1982@outlook.ger','https://www.filesystem.ntua.in.mp4',3.65,135),(23,'BP Car Plugin','Vasilis Papadopoulos','public','Iroon Politexneiou',94,'53229','Trikala','Greece',38.86704400,21.98967100,6682891376,'providerlove1994@info.in','https://www.mama.ntua.eu.ddl',2.86,40),(24,'Military Car','Maria Sotiropoulos','commercial','Syggrou',69,'14926','Thessaloniki','Greece',37.92513400,22.98183100,4120002041,'mariarandom1966@mailfence.gr','https://www.google.home.gov.htm',2.10,95),(25,'Euro Car Plugin','Mixalis Georgiou','public','Oulof Palme',67,'98879','Irakleio','Greece',39.01105400,22.68024100,5103240296,'userlove2005@hotmail.it','https://email.legal.softeng.us.json',1.86,117),(26,'Super Station','Elena Sotiropoulos','public','Katexaki',252,'27199','Livadia','Greece',38.10851400,21.30325100,6080072690,'lordsupertroll2000@mailfence.uk','https://email.webpage.ece.ntua.gov.xlm',3.26,117),(27,'Super Car Plugin','Makis Anastasiou','military','Agiou Alexandrou',6,'94132','Irakleio','Greece',38.17500400,23.40721100,3863354556,'mariasupertroll2004@protonmail.eu','https://snr.webpage.home.gr.html',1.78,107),(28,'Euro Station','Vasilis Oikonomou','commercial','Poseidonos',106,'59541','Patra','Greece',38.65658400,21.32841100,6144437639,'faviconrandom1954@protonmail.ger','https://telnet.bing.softeng.met.json',0.80,52),(29,'My Vehicle Charger','Mixalis Sotiropoulos','commercial','Ilioupoleos',71,'51023','Lamia','Greece',37.69570400,21.57610100,3248077007,'providerworld1962@info.gr','https://www2.mama.ece.ntua.ger.html',2.89,198),(30,'E-Autonomous Car','Giorgos Georgiou','military','Katexaki',127,'22116','Livadia','Greece',38.26000400,21.35634100,1321338946,'operatorlove1964@mail.ntua.ger','https://telnet.minister.ntua.eu.mp3',2.70,49),(31,'Super Car','Mixalis Loulakis','military','Kokkinopoulou',158,'49462','Livadia','Greece',39.25179400,24.00891100,3548399118,'mariaellada1942@outlook.com','https://email.legal.home.ger.mp4',2.33,117),(32,'Public Station','Mixalis Sotiropoulos','public','Bouboulinas',196,'62055','Drama','Greece',38.11683400,22.94414100,1857954915,'giorgoslove1944@outlook.in','https://www2.mama.ece.ntua.ger.pdf',2.64,26),(33,'Euro Car','Dimitra Oikonomou','public','Thiseos',249,'72057','Patra','Greece',38.10602400,22.63708100,1414658870,'mariamaestros1952@info.us','https://www.legal.mechan.met.htm',3.46,132),(34,'BP Vehicle Charger','Elena Anastasiou','military','Ermou',48,'55664','Athens','Greece',39.16800400,22.05404100,2124995988,'lordforthewin1982@yahoo.gov','https://www.google.home.gr.mp3',2.98,32),(35,'Public Car Plugin','Manolis Papadakis','commercial','Axilleos',149,'82095','Alexandroupoli','Greece',38.23305400,21.80335100,2328760063,'lordpapadakis1971@ece.ntua.it','https://email.filesystem.mechan.gr.pdf',2.86,19),(36,'National Home','Stella Anastasiou','private','Ermou',76,'71138','Patra','Greece',39.33920400,23.83020100,1887264650,'mariamaestros1945@info.us','https://telnet.mama.softeng.uk.json',1.05,95),(37,'E-Autonomous Station','Mixalis Takoroni','public','Dionisiou Aeropagitou',38,'61693','Livadia','Greece',39.60791400,21.66220100,3838597285,'johnmaestros1951@protonmail.it','https://www2.poetry.softeng.met.html',3.91,129),(38,'Electric Station','Giorgos Kolokotronis','commercial','Ermou',124,'37684','Athens','Greece',38.53521400,21.94347100,8387482318,'faviconworld1962@outlook.it','https://telnet.mama.softeng.uk.docx',3.69,180),(39,'Public Home','Manolis Anastasiou','public','Agiou Alexandrou',12,'31056','Athens','Greece',38.56241400,22.32085100,6026868517,'giannisrandom1949@outlook.gr','https://snr.bing.home.com.docx',1.94,131),(40,'BP Car Plugin','Elena Papadakis','private','Bouboulinas',180,'92269','Larisa','Greece',39.55900400,23.83331100,4821453631,'giannismaestros1961@yahoo.gov','https://www.minister.ece.ntua.eu.json',1.86,187);
/*!40000 ALTER TABLE `station` ENABLE KEYS */;
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
