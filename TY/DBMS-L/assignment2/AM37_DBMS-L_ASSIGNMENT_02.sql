-- MariaDB dump 10.19-11.1.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	11.1.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `library`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `library` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

USE `library`;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book` (
  `book_id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `pub_year` varchar(255) DEFAULT NULL,
  `publisher_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`book_id`),
  KEY `publisher_name` (`publisher_name`),
  CONSTRAINT `book_ibfk_1` FOREIGN KEY (`publisher_name`) REFERENCES `publisher` (`name`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES
(1,'DBMS','Jan 2017','McGraw-Hill'),
(2,'ADBMS','Jun 2016','McGraw-Hill'),
(4,'CG','Sep 2015','Grupo Planeta'),
(5,'OS','May 2016','Pearson');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_authors`
--

DROP TABLE IF EXISTS `book_authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book_authors` (
  `author_name` varchar(255) NOT NULL,
  `book_id` int(11) NOT NULL,
  PRIMARY KEY (`book_id`,`author_name`),
  CONSTRAINT `book_authors_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_authors`
--

LOCK TABLES `book_authors` WRITE;
/*!40000 ALTER TABLE `book_authors` DISABLE KEYS */;
INSERT INTO `book_authors` VALUES
('Navathe',1),
('Navathe',2),
('Edward Angel',4),
('Galvin',5);
/*!40000 ALTER TABLE `book_authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_copies`
--

DROP TABLE IF EXISTS `book_copies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book_copies` (
  `no_of_copies` int(11) DEFAULT NULL,
  `book_id` int(11) NOT NULL,
  `branch_id` int(11) NOT NULL,
  PRIMARY KEY (`book_id`,`branch_id`),
  KEY `branch_id` (`branch_id`),
  CONSTRAINT `book_copies_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`) ON DELETE CASCADE,
  CONSTRAINT `book_copies_ibfk_2` FOREIGN KEY (`branch_id`) REFERENCES `library_branch` (`branch_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_copies`
--

LOCK TABLES `book_copies` WRITE;
/*!40000 ALTER TABLE `book_copies` DISABLE KEYS */;
INSERT INTO `book_copies` VALUES
(10,1,10),
(5,1,11),
(2,2,12),
(5,2,13),
(3,4,11),
(1,5,10);
/*!40000 ALTER TABLE `book_copies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_lending`
--

DROP TABLE IF EXISTS `book_lending`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book_lending` (
  `date_out` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `book_id` int(11) NOT NULL,
  `branch_id` int(11) NOT NULL,
  `card_no` int(11) NOT NULL,
  PRIMARY KEY (`book_id`,`branch_id`,`card_no`),
  KEY `branch_id` (`branch_id`),
  KEY `card_no` (`card_no`),
  CONSTRAINT `book_lending_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`) ON DELETE CASCADE,
  CONSTRAINT `book_lending_ibfk_2` FOREIGN KEY (`branch_id`) REFERENCES `library_branch` (`branch_id`) ON DELETE CASCADE,
  CONSTRAINT `book_lending_ibfk_3` FOREIGN KEY (`card_no`) REFERENCES `card` (`card_no`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_lending`
--

LOCK TABLES `book_lending` WRITE;
/*!40000 ALTER TABLE `book_lending` DISABLE KEYS */;
INSERT INTO `book_lending` VALUES
('2017-01-01','2017-07-01',1,10,101),
('2017-04-12','2017-05-12',1,11,104),
('2017-02-21','2017-04-21',2,13,101),
('2017-03-15','2017-06-15',4,11,101);
/*!40000 ALTER TABLE `book_lending` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `card`
--

DROP TABLE IF EXISTS `card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `card` (
  `card_no` int(11) NOT NULL,
  PRIMARY KEY (`card_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `card`
--

LOCK TABLES `card` WRITE;
/*!40000 ALTER TABLE `card` DISABLE KEYS */;
INSERT INTO `card` VALUES
(100),
(101),
(102),
(103),
(104);
/*!40000 ALTER TABLE `card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `library_branch`
--

DROP TABLE IF EXISTS `library_branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `library_branch` (
  `branch_id` int(11) NOT NULL,
  `branch_name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library_branch`
--

LOCK TABLES `library_branch` WRITE;
/*!40000 ALTER TABLE `library_branch` DISABLE KEYS */;
INSERT INTO `library_branch` VALUES
(10,'RR Nagar','Bangalore'),
(11,'Dept of CSE, Atria IT','Bangalore'),
(12,'Rajaji Nagar','Bangalore'),
(13,'NITTE','Mangalore'),
(14,'MANIPAL','Udupi');
/*!40000 ALTER TABLE `library_branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publisher`
--

DROP TABLE IF EXISTS `publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `publisher` (
  `name` varchar(255) NOT NULL,
  `phone` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publisher`
--

LOCK TABLES `publisher` WRITE;
/*!40000 ALTER TABLE `publisher` DISABLE KEYS */;
INSERT INTO `publisher` VALUES
('Grupo Planeta',5555,'Bangalore'),
('Hachette Livre',4444,'Chennai'),
('McGraw-Hill',1111,'Bangalore'),
('Pearson',2222,'Delhi'),
('Random House',3333,'Hyderabad');
/*!40000 ALTER TABLE `publisher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `v_books`
--

DROP TABLE IF EXISTS `v_books`;
/*!50001 DROP VIEW IF EXISTS `v_books`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_books` AS SELECT
 1 AS `book_id`,
  1 AS `title`,
  1 AS `no_of_copies` */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_publication`
--

DROP TABLE IF EXISTS `v_publication`;
/*!50001 DROP VIEW IF EXISTS `v_publication`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_publication` AS SELECT
 1 AS `pub_year` */;
SET character_set_client = @saved_cs_client;

--
-- Current Database: `library`
--

USE `library`;

--
-- Final view structure for view `v_books`
--

/*!50001 DROP VIEW IF EXISTS `v_books`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_books` AS select `b`.`book_id` AS `book_id`,`b`.`title` AS `title`,`c`.`no_of_copies` AS `no_of_copies` from ((`book` `b` join `book_copies` `c`) join `library_branch` `l`) where `b`.`book_id` = `c`.`book_id` and `c`.`branch_id` = `l`.`branch_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_publication`
--

/*!50001 DROP VIEW IF EXISTS `v_publication`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_publication` AS select `book`.`pub_year` AS `pub_year` from `book` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-27 16:56:08
