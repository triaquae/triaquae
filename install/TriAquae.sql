-- MySQL dump 10.13  Distrib 5.5.34, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: TriAquae
-- ------------------------------------------------------
-- Server version	5.5.34-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `TriAquae`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `TriAquae` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `TriAquae`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add devinfo',8,'add_devinfo'),(23,'Can change devinfo',8,'change_devinfo'),(24,'Can delete devinfo',8,'delete_devinfo'),(25,'Can add check_ devinfo',9,'add_check_devinfo'),(26,'Can change check_ devinfo',9,'change_check_devinfo'),(27,'Can delete check_ devinfo',9,'delete_check_devinfo'),(28,'Can add idc',10,'add_idc'),(29,'Can change idc',10,'change_idc'),(30,'Can delete idc',10,'delete_idc'),(31,'Can add group',11,'add_group'),(32,'Can change group',11,'change_group'),(33,'Can delete group',11,'delete_group'),(34,'Can add ip',12,'add_ip'),(35,'Can change ip',12,'change_ip'),(36,'Can delete ip',12,'delete_ip'),(37,'Can add remote user',13,'add_remoteuser'),(38,'Can change remote user',13,'change_remoteuser'),(39,'Can delete remote user',13,'delete_remoteuser'),(40,'Can add triaquae user',14,'add_triaquaeuser'),(41,'Can change triaquae user',14,'change_triaquaeuser'),(42,'Can delete triaquae user',14,'delete_triaquaeuser'),(43,'Can add auth by ip and remote user',15,'add_authbyipandremoteuser'),(44,'Can change auth by ip and remote user',15,'change_authbyipandremoteuser'),(45,'Can delete auth by ip and remote user',15,'delete_authbyipandremoteuser'),(46,'Can add server status',16,'add_serverstatus'),(47,'Can change server status',16,'change_serverstatus'),(48,'Can delete server status',16,'delete_serverstatus'),(49,'Can add ops log',17,'add_opslog'),(50,'Can change ops log',17,'change_opslog'),(51,'Can delete ops log',17,'delete_opslog'),(52,'Can add ops log temp',18,'add_opslogtemp'),(53,'Can change ops log temp',18,'change_opslogtemp'),(54,'Can delete ops log temp',18,'delete_opslogtemp'),(55,'Can add quick link',19,'add_quicklink'),(56,'Can change quick link',19,'change_quicklink'),(57,'Can delete quick link',19,'delete_quicklink'),(58,'Can add migration history',20,'add_migrationhistory'),(59,'Can change migration history',20,'change_migrationhistory'),(60,'Can delete migration history',20,'delete_migrationhistory');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$10000$lkH3vI84fjWd$8NIlJMF83vux1fXrkV6NRGbi7GQDIOTibY4/HJIG750=','2013-11-17 10:30:06',1,'admin','','','admin@company.com',1,1,'2013-09-20 10:41:03'),(2,'pbkdf2_sha256$10000$TcOtjz12WGd8$V/+nY7IZbkvmtHsMYUhY6hqJA/R6eZAao0Gp5H/QBFQ=','2013-09-20 11:47:31',0,'tri_user01','','','',0,1,'2013-09-20 10:46:20');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=157 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2013-09-20 10:42:33',1,17,'1','0',1,''),(2,'2013-09-20 10:43:12',1,11,'1','TestGroup',1,''),(3,'2013-09-20 10:43:18',1,12,'1','127.0.0.1',1,''),(4,'2013-09-20 10:44:05',1,12,'2','61.135.169.105',1,''),(5,'2013-09-20 10:45:12',1,13,'1','root',1,''),(6,'2013-09-20 10:45:21',1,13,'2','triaquae',1,''),(7,'2013-09-20 10:45:38',1,13,'3','coral',1,''),(8,'2013-09-20 10:45:51',1,14,'1','admin',1,''),(9,'2013-09-20 10:46:20',1,3,'2','tri_user01',1,''),(10,'2013-09-20 10:46:46',1,14,'2','tri_user01',1,''),(11,'2013-09-20 10:47:39',1,11,'2','BJ',1,''),(12,'2013-09-20 10:47:55',1,12,'3','10.98.33.226',1,''),(13,'2013-09-20 10:48:23',1,12,'3','10.98.33.226',2,'Changed port and status_monitor_on.'),(14,'2013-09-20 10:48:50',1,15,'1','10.98.33.226	coral',1,''),(15,'2013-09-20 11:02:48',1,14,'2','tri_user01',2,'Changed remoteuser and group.'),(16,'2013-09-20 11:47:10',1,15,'2','10.98.33.226	triaquae',1,''),(17,'2013-09-20 11:56:22',1,17,'37','send /usr/local/triWEB/TriAquae/backend/Hardware_Collect_Script.py to /tmp/Hardware_Collect_Script.py ',3,''),(18,'2013-09-20 11:56:22',1,17,'36','send /tmp/TriSFTP_send_file_20130920_19_47_52.tgz to remote path /tmp/ ',3,''),(19,'2013-09-20 11:56:22',1,17,'35','send /tmp/TriSFTP_send_file_20130920_19_43_54.tgz to remote path /tmp/ ',3,''),(20,'2013-09-20 11:56:22',1,17,'34','send /tmp/TriSFTP_send_file_20130920_19_41_16.tgz to remote path /tmp/ ',3,''),(21,'2013-09-20 11:56:22',1,17,'33','send /tmp/TriSFTP_send_file_20130920_19_37_48.tgz to remote path /tmp/ ',3,''),(22,'2013-09-20 11:56:22',1,17,'32','send /tmp/TriSFTP_send_file_20130920_19_36_56.tgz to remote path /tmp/aa.txt ',3,''),(23,'2013-09-20 11:56:22',1,17,'31','get file /tmp/aa.txt from remote servers',3,''),(24,'2013-09-20 11:56:22',1,17,'30','get file /tmp/aa.txt from remote servers',3,''),(25,'2013-09-20 11:56:22',1,17,'29','get file /tmp/aa.txt from remote servers',3,''),(26,'2013-09-20 11:56:22',1,17,'28','get file /tmp/aa.txt from remote servers',3,''),(27,'2013-09-20 11:56:22',1,17,'27','get file /tmp/aa.txt from remote servers',3,''),(28,'2013-09-20 11:56:22',1,17,'26','get file /tmp/aa.txt from remote servers',3,''),(29,'2013-09-20 11:56:22',1,17,'25','get file /tmp/aa.txt from remote servers',3,''),(30,'2013-09-20 11:56:22',1,17,'24','get file /tmp/aa.txt from remote servers',3,''),(31,'2013-09-20 11:56:22',1,17,'23','get file /tmp/aa.txt from remote servers',3,''),(32,'2013-09-20 11:56:22',1,17,'22','get file /tmp/aa.txt from remote servers',3,''),(33,'2013-09-20 11:56:22',1,17,'21','get file /tmp/aa.txt from remote servers',3,''),(34,'2013-09-20 11:56:22',1,17,'20','get file /tmp/aa.txt from remote servers',3,''),(35,'2013-09-20 11:56:22',1,17,'19','get file /tmp/aa.txt from remote servers',3,''),(36,'2013-09-20 11:56:22',1,17,'18','get file /tmp/aa.txt from remote servers',3,''),(37,'2013-09-20 11:56:22',1,17,'17','get file /tmp/aa.txt from remote servers',3,''),(38,'2013-09-20 11:56:22',1,17,'16','get file /tmp/aa.txt from remote servers',3,''),(39,'2013-09-20 11:56:22',1,17,'15','get file /tmp/aa.txt from remote servers',3,''),(40,'2013-09-20 11:56:22',1,17,'14','get file /tmp/aa.txt from remote servers',3,''),(41,'2013-09-20 11:56:22',1,17,'13','N/A',3,''),(42,'2013-09-20 11:56:22',1,17,'12','N/A',3,''),(43,'2013-09-20 11:56:22',1,17,'11','get file /tmp/aa.txt from remote servers',3,''),(44,'2013-09-20 11:56:22',1,17,'10','get file /tmp/aa.txt from remote servers',3,''),(45,'2013-09-20 11:56:22',1,17,'9','send /tmp/TriSFTP_send_file_20130920_19_05_13.tgz to remote path /tmp/ ',3,''),(46,'2013-09-20 11:56:22',1,17,'8','top -bn 1',3,''),(47,'2013-09-20 11:56:22',1,17,'7','top -bn 1',3,''),(48,'2013-09-20 11:56:22',1,17,'6','df',3,''),(49,'2013-09-20 11:56:22',1,17,'5','pwd',3,''),(50,'2013-09-20 11:56:22',1,17,'4','python /usr/local/triWEB/TriAquae/backend/baoleihost.py 10.98.33.226 22 coral SSH_PASSWD 1 admin',3,''),(51,'2013-09-20 11:56:22',1,17,'3','python /usr/local/triWEB/TriAquae/backend/baoleihost.py 10.98.33.226 22 coral SSH_PASSWD 1 admin',3,''),(52,'2013-09-20 11:56:22',1,17,'2','python /usr/local/triWEB/TriAquae/backend/baoleihost.py 10.98.33.226 22 coral SSH_PASSWD 1 admin',3,''),(53,'2013-09-20 11:57:16',1,18,'86','10.98.33.226',3,''),(54,'2013-09-20 11:57:16',1,18,'85','61.135.169.105',3,''),(55,'2013-09-20 11:57:16',1,18,'84','127.0.0.1',3,''),(56,'2013-09-20 11:57:16',1,18,'83','10.98.33.226',3,''),(57,'2013-09-20 11:57:16',1,18,'82','127.0.0.1',3,''),(58,'2013-09-20 11:57:16',1,18,'81','61.135.169.105',3,''),(59,'2013-09-20 11:57:16',1,18,'80','10.98.33.226',3,''),(60,'2013-09-20 11:57:16',1,18,'79','127.0.0.1',3,''),(61,'2013-09-20 11:57:16',1,18,'78','61.135.169.105',3,''),(62,'2013-09-20 11:57:16',1,18,'77','10.98.33.226',3,''),(63,'2013-09-20 11:57:16',1,18,'76','127.0.0.1',3,''),(64,'2013-09-20 11:57:16',1,18,'75','61.135.169.105',3,''),(65,'2013-09-20 11:57:16',1,18,'74','10.98.33.226',3,''),(66,'2013-09-20 11:57:16',1,18,'73','127.0.0.1',3,''),(67,'2013-09-20 11:57:16',1,18,'72','61.135.169.105',3,''),(68,'2013-09-20 11:57:16',1,18,'71','127.0.0.1',3,''),(69,'2013-09-20 11:57:16',1,18,'70','61.135.169.105',3,''),(70,'2013-09-20 11:57:16',1,18,'69','10.98.33.226',3,''),(71,'2013-09-20 11:57:16',1,18,'68','127.0.0.1',3,''),(72,'2013-09-20 11:57:16',1,18,'67','61.135.169.105',3,''),(73,'2013-09-20 11:57:16',1,18,'66','10.98.33.226',3,''),(74,'2013-09-20 11:57:16',1,18,'65','127.0.0.1',3,''),(75,'2013-09-20 11:57:16',1,18,'64','61.135.169.105',3,''),(76,'2013-09-20 11:57:16',1,18,'63','127.0.0.1',3,''),(77,'2013-09-20 11:57:16',1,18,'62','61.135.169.105',3,''),(78,'2013-09-20 11:57:16',1,18,'61','10.98.33.226',3,''),(79,'2013-09-20 11:57:16',1,18,'60','127.0.0.1',3,''),(80,'2013-09-20 11:57:16',1,18,'59','61.135.169.105',3,''),(81,'2013-09-20 11:57:16',1,18,'58','10.98.33.226',3,''),(82,'2013-09-20 11:57:16',1,18,'57','127.0.0.1',3,''),(83,'2013-09-20 11:57:16',1,18,'56','61.135.169.105',3,''),(84,'2013-09-20 11:57:16',1,18,'55','10.98.33.226',3,''),(85,'2013-09-20 11:57:16',1,18,'54','127.0.0.1',3,''),(86,'2013-09-20 11:57:16',1,18,'53','61.135.169.105',3,''),(87,'2013-09-20 11:57:16',1,18,'52','10.98.33.226',3,''),(88,'2013-09-20 11:57:16',1,18,'51','127.0.0.1',3,''),(89,'2013-09-20 11:57:16',1,18,'50','61.135.169.105',3,''),(90,'2013-09-20 11:57:16',1,18,'49','10.98.33.226',3,''),(91,'2013-09-20 11:57:16',1,18,'48','127.0.0.1',3,''),(92,'2013-09-20 11:57:16',1,18,'47','61.135.169.105',3,''),(93,'2013-09-20 11:57:16',1,18,'46','10.98.33.226',3,''),(94,'2013-09-20 11:57:16',1,18,'45','127.0.0.1',3,''),(95,'2013-09-20 11:57:16',1,18,'44','61.135.169.105',3,''),(96,'2013-09-20 11:57:16',1,18,'43','10.98.33.226',3,''),(97,'2013-09-20 11:57:16',1,18,'42','127.0.0.1',3,''),(98,'2013-09-20 11:57:16',1,18,'41','61.135.169.105',3,''),(99,'2013-09-20 11:57:16',1,18,'40','10.98.33.226',3,''),(100,'2013-09-20 11:57:16',1,18,'39','127.0.0.1',3,''),(101,'2013-09-20 11:57:16',1,18,'38','10.98.33.226',3,''),(102,'2013-09-20 11:57:16',1,18,'37','127.0.0.1',3,''),(103,'2013-09-20 11:57:16',1,18,'36','61.135.169.105',3,''),(104,'2013-09-20 11:57:16',1,18,'35','10.98.33.226',3,''),(105,'2013-09-20 11:57:16',1,18,'34','127.0.0.1',3,''),(106,'2013-09-20 11:57:16',1,18,'33','61.135.169.105',3,''),(107,'2013-09-20 11:57:16',1,18,'32','10.98.33.226',3,''),(108,'2013-09-20 11:57:16',1,18,'31','127.0.0.1',3,''),(109,'2013-09-20 11:57:16',1,18,'30','61.135.169.105',3,''),(110,'2013-09-20 11:57:16',1,18,'29','10.98.33.226',3,''),(111,'2013-09-20 11:57:16',1,18,'28','127.0.0.1',3,''),(112,'2013-09-20 11:57:16',1,18,'27','61.135.169.105',3,''),(113,'2013-09-20 11:57:16',1,18,'26','10.98.33.226',3,''),(114,'2013-09-20 11:57:16',1,18,'25','127.0.0.1',3,''),(115,'2013-09-20 11:57:16',1,18,'24','61.135.169.105',3,''),(116,'2013-09-20 11:57:16',1,18,'23','10.98.33.226',3,''),(117,'2013-09-20 11:57:16',1,18,'22','127.0.0.1',3,''),(118,'2013-09-20 11:57:16',1,18,'21','10.98.33.226',3,''),(119,'2013-09-20 11:57:16',1,18,'20','localhost',3,''),(120,'2013-09-20 11:57:16',1,18,'19','10.98.33.226',3,''),(121,'2013-09-20 11:57:16',1,18,'18','-g',3,''),(122,'2013-09-20 11:57:16',1,18,'17','10.98.33.226',3,''),(123,'2013-09-20 11:57:16',1,18,'16','127.0.0.1',3,''),(124,'2013-09-20 11:57:16',1,18,'15','10.98.33.226',3,''),(125,'2013-09-20 11:57:16',1,18,'14','127.0.0.1',3,''),(126,'2013-09-20 11:57:16',1,18,'13','10.98.33.226',3,''),(127,'2013-09-20 11:57:16',1,18,'12','127.0.0.1',3,''),(128,'2013-09-20 11:57:16',1,18,'11','61.135.169.105',3,''),(129,'2013-09-20 11:57:16',1,18,'10','127.0.0.1',3,''),(130,'2013-09-20 11:57:16',1,18,'9','10.98.33.226',3,''),(131,'2013-09-20 11:57:16',1,18,'8','127.0.0.1',3,''),(132,'2013-09-20 11:57:16',1,18,'7','61.135.169.105',3,''),(133,'2013-09-20 11:57:16',1,18,'6','10.98.33.226',3,''),(134,'2013-09-20 11:57:16',1,18,'5','61.135.169.105',3,''),(135,'2013-09-20 11:57:16',1,18,'4','127.0.0.1',3,''),(136,'2013-09-20 11:57:16',1,18,'3','61.135.169.105',3,''),(137,'2013-09-20 11:57:16',1,18,'2','127.0.0.1',3,''),(138,'2013-09-20 11:57:16',1,18,'1','10.98.33.226',3,''),(139,'2013-11-17 08:51:36',1,12,'4','192.168.1.106',1,''),(140,'2013-11-17 09:36:18',1,19,'1','QuickLink object',1,''),(141,'2013-11-17 09:52:32',1,19,'2','QuickLink object',1,''),(142,'2013-11-17 09:52:45',1,19,'3','QuickLink object',1,''),(143,'2013-11-17 09:52:57',1,19,'4','QuickLink object',1,''),(144,'2013-11-17 09:53:08',1,19,'5','QuickLink object',1,''),(145,'2013-11-17 10:03:20',1,19,'6','QuickLink object',1,''),(146,'2013-11-17 10:11:49',1,19,'7','QuickLink object',1,''),(147,'2013-11-17 10:12:21',1,19,'8','QuickLink object',1,''),(148,'2013-11-17 10:13:20',1,19,'9','QuickLink object',1,''),(149,'2013-11-17 10:30:55',1,19,'9','QuickLink object',2,'Changed link_name.'),(150,'2013-11-17 10:34:32',1,19,'5','QuickLink object',2,'Changed link_name and url.'),(151,'2013-11-17 11:08:48',1,19,'9','QuickLink object',2,'Changed color.'),(152,'2013-11-17 11:11:48',1,19,'8','QuickLink object',2,'Changed color.'),(153,'2013-11-17 11:11:54',1,19,'2','QuickLink object',2,'Changed color.'),(154,'2013-11-17 11:12:17',1,19,'7','QuickLink object',2,'Changed color.'),(155,'2013-11-17 11:12:50',1,19,'5','QuickLink object',2,'Changed color.'),(156,'2013-11-17 11:13:25',1,19,'5','QuickLink object',2,'Changed color.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'devinfo','hosts','devinfo'),(9,'check_ devinfo','hosts','check_devinfo'),(10,'idc','hosts','idc'),(11,'group','hosts','group'),(12,'ip','hosts','ip'),(13,'remote user','hosts','remoteuser'),(14,'triaquae user','hosts','triaquaeuser'),(15,'auth by ip and remote user','hosts','authbyipandremoteuser'),(16,'server status','hosts','serverstatus'),(17,'ops log','hosts','opslog'),(18,'ops log temp','hosts','opslogtemp'),(19,'quick link','hosts','quicklink'),(20,'migration history','south','migrationhistory');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('orngnkci8mzz14i1m0qwu96ebhtseo5v','Y2Q0YmZlMjU0NDNjZWNlNTliNTY5YmY2OGUzNzJkOTRmYTg1ZGU4YjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==','2013-10-04 11:56:10'),('oo1luu4f7fgfrnu1o6tibk22f9fn8jo2','Y2Q0YmZlMjU0NDNjZWNlNTliNTY5YmY2OGUzNzJkOTRmYTg1ZGU4YjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==','2013-12-01 10:30:06'),('b1s5zk55cvvt7jxvnuu53fvq35yizamf','Y2Q0YmZlMjU0NDNjZWNlNTliNTY5YmY2OGUzNzJkOTRmYTg1ZGU4YjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==','2013-12-01 09:17:41');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_authbyipandremoteuser`
--

DROP TABLE IF EXISTS `hosts_authbyipandremoteuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_authbyipandremoteuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(1024) NOT NULL,
  `authtype` varchar(100) NOT NULL,
  `ip_id` int(11) DEFAULT NULL,
  `remoteUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip_id` (`ip_id`,`remoteUser_id`),
  KEY `hosts_authbyipandremoteuser_6259660e` (`ip_id`),
  KEY `hosts_authbyipandremoteuser_7d22bda5` (`remoteUser_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_authbyipandremoteuser`
--

LOCK TABLES `hosts_authbyipandremoteuser` WRITE;
/*!40000 ALTER TABLE `hosts_authbyipandremoteuser` DISABLE KEYS */;
INSERT INTO `hosts_authbyipandremoteuser` VALUES (1,'1','ssh',3,3),(2,'dAE9w2','ssh',3,2);
/*!40000 ALTER TABLE `hosts_authbyipandremoteuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_check_devinfo`
--

DROP TABLE IF EXISTS `hosts_check_devinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_check_devinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Triaquae_Hostname` varchar(50) NOT NULL,
  `Change_Type` varchar(64) NOT NULL,
  `Old_Value` varchar(64) NOT NULL,
  `New_Value` varchar(64) NOT NULL,
  `Change_Time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_check_devinfo`
--

LOCK TABLES `hosts_check_devinfo` WRITE;
/*!40000 ALTER TABLE `hosts_check_devinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `hosts_check_devinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_devinfo`
--

DROP TABLE IF EXISTS `hosts_devinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_devinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Triaquae_Hostname` varchar(50) NOT NULL,
  `System_Hostname` varchar(50) NOT NULL,
  `System_Ip` varchar(64) NOT NULL,
  `Device_Type` varchar(64) NOT NULL,
  `Device_Model` varchar(64) NOT NULL,
  `System_Kernel` varchar(256) NOT NULL,
  `System_Version` varchar(64) NOT NULL,
  `System_Mac` varchar(256) NOT NULL,
  `Physical_Memory` varchar(64) NOT NULL,
  `System_Swap` varchar(64) NOT NULL,
  `Memory_Slots_Number` varchar(30) NOT NULL,
  `Memory_Slots_All` varchar(2000) NOT NULL,
  `Logical_Cpu_Cores` varchar(64) NOT NULL,
  `Physical_Cpu_Cores` varchar(64) NOT NULL,
  `Physical_Cpu_Model` varchar(64) NOT NULL,
  `Physical_Cpu_MHz` varchar(256) NOT NULL,
  `Hard_Disk` varchar(64) NOT NULL,
  `Ethernet_Interface` varchar(364) NOT NULL,
  `System_Hostid` varchar(30) NOT NULL,
  `Device_Sn` varchar(164) NOT NULL,
  `Asset_Number` varchar(164) NOT NULL,
  `Note1` varchar(256) NOT NULL,
  `Note2` varchar(256) NOT NULL,
  `Note3` varchar(256) NOT NULL,
  `Check_Time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_devinfo`
--

LOCK TABLES `hosts_devinfo` WRITE;
/*!40000 ALTER TABLE `hosts_devinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `hosts_devinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_group`
--

DROP TABLE IF EXISTS `hosts_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_group`
--

LOCK TABLES `hosts_group` WRITE;
/*!40000 ALTER TABLE `hosts_group` DISABLE KEYS */;
INSERT INTO `hosts_group` VALUES (1,'TestGroup'),(2,'BJ');
/*!40000 ALTER TABLE `hosts_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_idc`
--

DROP TABLE IF EXISTS `hosts_idc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_idc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_idc`
--

LOCK TABLES `hosts_idc` WRITE;
/*!40000 ALTER TABLE `hosts_idc` DISABLE KEYS */;
/*!40000 ALTER TABLE `hosts_idc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_ip`
--

DROP TABLE IF EXISTS `hosts_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(50) NOT NULL,
  `ip` char(15) NOT NULL,
  `idc_id` int(11) DEFAULT NULL,
  `port` int(11) NOT NULL,
  `os` varchar(20) NOT NULL,
  `alert_limit` int(11) NOT NULL,
  `snmp_alert_limit` int(11) NOT NULL,
  `asset_collection` tinyint(1) NOT NULL,
  `status_monitor_on` tinyint(1) NOT NULL,
  `snmp_on` tinyint(1) NOT NULL,
  `snmp_version` varchar(10) NOT NULL,
  `snmp_community_name` varchar(50) NOT NULL,
  `snmp_security_level` varchar(50) NOT NULL,
  `snmp_auth_protocol` varchar(50) NOT NULL,
  `snmp_user` varchar(50) NOT NULL,
  `snmp_pass` varchar(50) NOT NULL,
  `system_load_warning` int(11) NOT NULL,
  `system_load_critical` int(11) NOT NULL,
  `cpu_idle_warning` int(11) NOT NULL,
  `cpu_idle_critical` int(11) NOT NULL,
  `mem_usage_warning` int(11) NOT NULL,
  `mem_usage_critical` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  UNIQUE KEY `ip` (`ip`),
  KEY `hosts_ip_7f604875` (`idc_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_ip`
--

LOCK TABLES `hosts_ip` WRITE;
/*!40000 ALTER TABLE `hosts_ip` DISABLE KEYS */;
INSERT INTO `hosts_ip` VALUES (1,'localhost','127.0.0.1',NULL,22,'linux',5,5,1,1,1,'2c','public','auth','MD5','triaquae_snmp','my_pass',0,0,0,0,0,0),(2,'www.baidu.com','61.135.169.105',NULL,22,'linux',5,5,1,1,1,'2c','public','auth','MD5','triaquae_snmp','my_pass',0,0,0,0,0,0),(3,'testServer1','10.98.33.226',NULL,22,'linux',5,5,1,0,1,'2c','public','auth','MD5','triaquae_snmp','my_pass',0,0,0,0,0,0),(4,'liuyuleihost','192.168.1.106',NULL,22,'linux',5,5,1,1,1,'2c','public','auth','MD5','triaquae_snmp','my_pass',0,0,0,0,0,0);
/*!40000 ALTER TABLE `hosts_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_ip_group`
--

DROP TABLE IF EXISTS `hosts_ip_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_ip_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip_id` (`ip_id`,`group_id`),
  KEY `hosts_ip_group_6259660e` (`ip_id`),
  KEY `hosts_ip_group_5f412f9a` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_ip_group`
--

LOCK TABLES `hosts_ip_group` WRITE;
/*!40000 ALTER TABLE `hosts_ip_group` DISABLE KEYS */;
INSERT INTO `hosts_ip_group` VALUES (1,1,1),(2,2,1),(4,3,2),(5,4,2);
/*!40000 ALTER TABLE `hosts_ip_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_opslog`
--

DROP TABLE IF EXISTS `hosts_opslog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_opslog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_date` datetime NOT NULL,
  `finish_date` datetime DEFAULT NULL,
  `log_type` varchar(50) NOT NULL,
  `tri_user` varchar(30) NOT NULL,
  `run_user` varchar(30) NOT NULL,
  `cmd` longtext NOT NULL,
  `total_task` int(11) NOT NULL,
  `success_num` int(11) NOT NULL,
  `failed_num` int(11) NOT NULL,
  `track_mark` int(11) NOT NULL,
  `note` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `track_mark` (`track_mark`)
) ENGINE=MyISAM AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_opslog`
--

LOCK TABLES `hosts_opslog` WRITE;
/*!40000 ALTER TABLE `hosts_opslog` DISABLE KEYS */;
INSERT INTO `hosts_opslog` VALUES (1,'2013-09-20 10:42:33','2013-09-20 10:41:46','Initial value','0','0','0',0,0,0,0,'');
/*!40000 ALTER TABLE `hosts_opslog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_opslogtemp`
--

DROP TABLE IF EXISTS `hosts_opslogtemp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_opslogtemp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `user` varchar(30) NOT NULL,
  `ip` char(15) NOT NULL,
  `event_type` varchar(50) NOT NULL,
  `cmd` longtext NOT NULL,
  `event_log` longtext NOT NULL,
  `result` varchar(30) NOT NULL,
  `track_mark` int(11) NOT NULL,
  `note` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=87 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_opslogtemp`
--

LOCK TABLES `hosts_opslogtemp` WRITE;
/*!40000 ALTER TABLE `hosts_opslogtemp` DISABLE KEYS */;
/*!40000 ALTER TABLE `hosts_opslogtemp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_quicklink`
--

DROP TABLE IF EXISTS `hosts_quicklink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_quicklink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `link_name` varchar(50) NOT NULL,
  `url` varchar(200) NOT NULL,
  `color` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_quicklink`
--

LOCK TABLES `hosts_quicklink` WRITE;
/*!40000 ALTER TABLE `hosts_quicklink` DISABLE KEYS */;
INSERT INTO `hosts_quicklink` VALUES (1,'baidu','http://www.baidu.com/','0'),(2,'google','http://www.google.com/','btn-success'),(3,'sina','http://www.sina.cn/','0'),(4,'weibo','http://weibo.com/','0'),(5,'TriAquae Support','http://118.244.168.45:3000/','btn-info'),(6,'TriAquae Official site','http://triweb.sinaapp.com/','0'),(7,'ChinaUnix','http://www.chinaunix.net/','btn-warning'),(8,'51cto','http://www.51cto.com/','btn-primary'),(9,'老男孩Linux','http://oldboy.blog.51cto.com/','btn-danger');
/*!40000 ALTER TABLE `hosts_quicklink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_remoteuser`
--

DROP TABLE IF EXISTS `hosts_remoteuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_remoteuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_remoteuser`
--

LOCK TABLES `hosts_remoteuser` WRITE;
/*!40000 ALTER TABLE `hosts_remoteuser` DISABLE KEYS */;
INSERT INTO `hosts_remoteuser` VALUES (1,'root'),(2,'triaquae'),(3,'coral');
/*!40000 ALTER TABLE `hosts_remoteuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_serverstatus`
--

DROP TABLE IF EXISTS `hosts_serverstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_serverstatus` (
  `host` char(15) NOT NULL,
  `hostname` varchar(100) NOT NULL,
  `host_status` varchar(10) NOT NULL,
  `ping_status` varchar(100) NOT NULL,
  `last_check` varchar(100) NOT NULL,
  `host_uptime` varchar(50) NOT NULL,
  `attempt_count` int(11) NOT NULL,
  `breakdown_count` int(11) NOT NULL,
  `up_count` int(11) NOT NULL,
  `snmp_alert_count` int(11) NOT NULL,
  `availability` varchar(20) NOT NULL,
  PRIMARY KEY (`host`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_serverstatus`
--

LOCK TABLES `hosts_serverstatus` WRITE;
/*!40000 ALTER TABLE `hosts_serverstatus` DISABLE KEYS */;
INSERT INTO `hosts_serverstatus` VALUES ('127.0.0.1','localhost','UP','rtt min/avg/max/mdev = 0.029/0.030/0.033/0.006 ms','2013_11_17 17:41:58','Unkown',0,0,245,27,'100'),('61.135.169.105','www.baidu.com','UP','rtt min/avg/max/mdev = 18.476/20.345/22.463/1.637 ms','2013_11_17 17:41:58','Unkown',0,0,243,12,'100'),('10.98.33.226','testServer1','UP','rtt min/avg/max/mdev = 0.211/0.749/1.021/0.381 ms','2013_09_20 18:48:17','Unkown',0,0,1,12,'100'),('192.168.1.106','liuyuleihost','UP','rtt min/avg/max/mdev = 3.111/3.854/4.691/0.648 ms','2013_11_17 17:41:58','2013_11_17 16:51:46',0,0,94,0,'100');
/*!40000 ALTER TABLE `hosts_serverstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_triaquaeuser`
--

DROP TABLE IF EXISTS `hosts_triaquaeuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_triaquaeuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `email` varchar(75) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hosts_triaquaeuser_6340c63c` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_triaquaeuser`
--

LOCK TABLES `hosts_triaquaeuser` WRITE;
/*!40000 ALTER TABLE `hosts_triaquaeuser` DISABLE KEYS */;
INSERT INTO `hosts_triaquaeuser` VALUES (1,1,'admin@gmail.com'),(2,2,'tri_user01@gmail.com');
/*!40000 ALTER TABLE `hosts_triaquaeuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_triaquaeuser_group`
--

DROP TABLE IF EXISTS `hosts_triaquaeuser_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_triaquaeuser_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `triaquaeuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `triaquaeuser_id` (`triaquaeuser_id`,`group_id`),
  KEY `hosts_triaquaeuser_group_01383dc4` (`triaquaeuser_id`),
  KEY `hosts_triaquaeuser_group_5f412f9a` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_triaquaeuser_group`
--

LOCK TABLES `hosts_triaquaeuser_group` WRITE;
/*!40000 ALTER TABLE `hosts_triaquaeuser_group` DISABLE KEYS */;
INSERT INTO `hosts_triaquaeuser_group` VALUES (1,1,1),(2,2,1),(3,2,2);
/*!40000 ALTER TABLE `hosts_triaquaeuser_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_triaquaeuser_ip`
--

DROP TABLE IF EXISTS `hosts_triaquaeuser_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_triaquaeuser_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `triaquaeuser_id` int(11) NOT NULL,
  `ip_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `triaquaeuser_id` (`triaquaeuser_id`,`ip_id`),
  KEY `hosts_triaquaeuser_ip_01383dc4` (`triaquaeuser_id`),
  KEY `hosts_triaquaeuser_ip_6259660e` (`ip_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_triaquaeuser_ip`
--

LOCK TABLES `hosts_triaquaeuser_ip` WRITE;
/*!40000 ALTER TABLE `hosts_triaquaeuser_ip` DISABLE KEYS */;
INSERT INTO `hosts_triaquaeuser_ip` VALUES (2,2,2);
/*!40000 ALTER TABLE `hosts_triaquaeuser_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hosts_triaquaeuser_remoteuser`
--

DROP TABLE IF EXISTS `hosts_triaquaeuser_remoteuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hosts_triaquaeuser_remoteuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `triaquaeuser_id` int(11) NOT NULL,
  `remoteuser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `triaquaeuser_id` (`triaquaeuser_id`,`remoteuser_id`),
  KEY `hosts_triaquaeuser_remoteuser_01383dc4` (`triaquaeuser_id`),
  KEY `hosts_triaquaeuser_remoteuser_29e729b2` (`remoteuser_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hosts_triaquaeuser_remoteuser`
--

LOCK TABLES `hosts_triaquaeuser_remoteuser` WRITE;
/*!40000 ALTER TABLE `hosts_triaquaeuser_remoteuser` DISABLE KEYS */;
INSERT INTO `hosts_triaquaeuser_remoteuser` VALUES (1,1,1),(2,1,2),(3,1,3),(5,2,2),(6,2,3);
/*!40000 ALTER TABLE `hosts_triaquaeuser_remoteuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'hosts','0001_initial','2013-11-17 10:55:43'),(2,'hosts','0002_auto__add_field_quicklink_color','2013-11-17 10:56:31');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-11-17 19:15:53
