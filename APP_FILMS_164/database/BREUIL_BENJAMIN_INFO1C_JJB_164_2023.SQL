-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour BREUIL_BENJAMIN_INFO1C_JJB_164_2023
DROP DATABASE IF EXISTS `BREUIL_BENJAMIN_INFO1C_JJB_164_2023`;
CREATE DATABASE IF NOT EXISTS `BREUIL_BENJAMIN_INFO1C_JJB_164_2023` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `BREUIL_BENJAMIN_INFO1C_JJB_164_2023`;

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_adresse
DROP TABLE IF EXISTS `t_adresse`;
CREATE TABLE IF NOT EXISTS `t_adresse` (
  `id_adresse` int NOT NULL AUTO_INCREMENT,
  `npa` varchar(10) DEFAULT NULL,
  `rue` varchar(200) DEFAULT NULL,
  `numero_rue` varchar(10) DEFAULT NULL,
  `ville` varchar(100) DEFAULT NULL,
  `pays` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_adresse`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_adresse : ~6 rows (environ)
INSERT INTO `t_adresse` (`id_adresse`, `npa`, `rue`, `numero_rue`, `ville`, `pays`) VALUES
	(1, '1200', 'Rue de la Gare', '15', 'Genève', 'Suisse'),
	(2, '1234', 'Rue du Paradis', '1', 'Genève', 'Suisse'),
	(3, '5678', 'Avenue des Fleurs', '10', 'Lausanne', 'Suisse'),
	(4, '9012', 'Rue de la Liberté', '5', 'Zurich', 'Suisse'),
	(5, '3456', 'Boulevard de la Paix', '7', 'Berne', 'Suisse'),
	(6, '7890', 'Rue de la Gare', '15', 'Bâle', 'Suisse');

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_avoir_niveau_personne
DROP TABLE IF EXISTS `t_avoir_niveau_personne`;
CREATE TABLE IF NOT EXISTS `t_avoir_niveau_personne` (
  `id_avoir_niveau_personne` int NOT NULL AUTO_INCREMENT,
  `fk_niveau` int DEFAULT NULL,
  `fk_personne` int DEFAULT NULL,
  PRIMARY KEY (`id_avoir_niveau_personne`),
  KEY `fk_niveau` (`fk_niveau`),
  KEY `fk_personne` (`fk_personne`),
  CONSTRAINT `t_avoir_niveau_personne_ibfk_1` FOREIGN KEY (`fk_niveau`) REFERENCES `t_niveau` (`id_niveau`),
  CONSTRAINT `t_avoir_niveau_personne_ibfk_2` FOREIGN KEY (`fk_personne`) REFERENCES `t_personne` (`id_personne`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_avoir_niveau_personne : ~0 rows (environ)

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_avoir_niveau_technique_niveau
DROP TABLE IF EXISTS `t_avoir_niveau_technique_niveau`;
CREATE TABLE IF NOT EXISTS `t_avoir_niveau_technique_niveau` (
  `id_avoir_niveau_technique_niveau` int NOT NULL AUTO_INCREMENT,
  `fk_niveau` int DEFAULT NULL,
  `fk_technique` int DEFAULT NULL,
  PRIMARY KEY (`id_avoir_niveau_technique_niveau`),
  KEY `fk_niveau` (`fk_niveau`),
  KEY `fk_technique` (`fk_technique`),
  CONSTRAINT `t_avoir_niveau_technique_niveau_ibfk_1` FOREIGN KEY (`fk_niveau`) REFERENCES `t_niveau` (`id_niveau`),
  CONSTRAINT `t_avoir_niveau_technique_niveau_ibfk_2` FOREIGN KEY (`fk_technique`) REFERENCES `t_technique` (`id_technique`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_avoir_niveau_technique_niveau : ~3 rows (environ)
INSERT INTO `t_avoir_niveau_technique_niveau` (`id_avoir_niveau_technique_niveau`, `fk_niveau`, `fk_technique`) VALUES
	(5, 3, 1),
	(12, 4, 2),
	(14, 9, 1);

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_avoir_niveau_technique_personne
DROP TABLE IF EXISTS `t_avoir_niveau_technique_personne`;
CREATE TABLE IF NOT EXISTS `t_avoir_niveau_technique_personne` (
  `id_avoir_niveau_technique_personne` int NOT NULL AUTO_INCREMENT,
  `fk_niveau` int DEFAULT NULL,
  `fk_personne` int DEFAULT NULL,
  `date` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_avoir_niveau_technique_personne`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_avoir_niveau_technique_personne : ~0 rows (environ)

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_categories
DROP TABLE IF EXISTS `t_categories`;
CREATE TABLE IF NOT EXISTS `t_categories` (
  `id_categories` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_categories`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_categories : ~0 rows (environ)

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_echauffement
DROP TABLE IF EXISTS `t_echauffement`;
CREATE TABLE IF NOT EXISTS `t_echauffement` (
  `id_echauffement` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `description` text,
  `temps_moyen` int DEFAULT NULL,
  PRIMARY KEY (`id_echauffement`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_echauffement : ~15 rows (environ)
INSERT INTO `t_echauffement` (`id_echauffement`, `name`, `description`, `temps_moyen`) VALUES
	(1, 'Jogging', 'Course lente sur place ou en déplacement pour échauffer les muscles et augmenter la circulation sanguine', 10),
	(2, 'Shrimping', 'Mouvement de reptation sur le dos pour se déplacer rapidement sur le sol', 5),
	(3, 'Hip escape', 'Mouvement de base pour se déplacer rapidement sur le sol en utilisant la hanche', 5),
	(4, 'Forward roll', 'Roulade avant pour échauffer le cou et les épaules', 5),
	(5, 'Backward roll', 'Roulade arrière pour échauffer le cou et les épaules', 5),
	(6, 'Bear crawl', 'Mouvement à quatre pattes pour échauffer les jambes et les bras', 5),
	(7, 'Crab walk', 'Mouvement à quatre pattes pour échauffer les jambes et les bras', 5),
	(8, 'Cartwheel', 'Mouvement acrobatique pour échauffer le corps et les épaules', 5),
	(9, 'Sprawl', 'Mouvement pour se défendre contre les takedowns et échauffer le corps', 5),
	(10, 'Jumping jacks', 'Exercice cardiovasculaire pour échauffer le corps', 5),
	(11, 'Mountain climbers', 'Exercice cardiovasculaire pour échauffer le corps', 5),
	(12, 'Squats', 'Exercice pour échauffer les jambes et les fessiers', 5),
	(13, 'Lunges', 'Exercice pour échauffer les jambes et les fessiers', 5),
	(14, 'Burpees', 'Exercice cardiovasculaire pour échauffer le corps et renforcer la musculature', 10),
	(15, 'Jumping rope', 'Exercice cardiovasculaire pour échauffer le corps et améliorer la coordination', 5);

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_email
DROP TABLE IF EXISTS `t_email`;
CREATE TABLE IF NOT EXISTS `t_email` (
  `id_email` int NOT NULL AUTO_INCREMENT,
  `adresse_email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_email : ~6 rows (environ)
INSERT INTO `t_email` (`id_email`, `adresse_email`) VALUES
	(1, 'benjaminbreuil2005@gmail.com'),
	(2, 'john.doe@example.com'),
	(3, 'mary.smith@example.com'),
	(4, 'robert.johnson@example.com'),
	(5, 'emily.wilson@example.com'),
	(6, 'david.brown@example.com');

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_niveau
DROP TABLE IF EXISTS `t_niveau`;
CREATE TABLE IF NOT EXISTS `t_niveau` (
  `id_niveau` int NOT NULL AUTO_INCREMENT,
  `name_niveau` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_niveau`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_niveau : ~5 rows (environ)
INSERT INTO `t_niveau` (`id_niveau`, `name_niveau`) VALUES
	(1, 'white'),
	(3, 'purple'),
	(4, 'brown'),
	(5, 'black'),
	(9, 'blue');

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_num_tel
DROP TABLE IF EXISTS `t_num_tel`;
CREATE TABLE IF NOT EXISTS `t_num_tel` (
  `id_num_tel` int NOT NULL AUTO_INCREMENT,
  `num_tel` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_num_tel`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_num_tel : ~6 rows (environ)
INSERT INTO `t_num_tel` (`id_num_tel`, `num_tel`) VALUES
	(1, '+41791234567'),
	(2, '+41782345678'),
	(3, '+41773456789'),
	(4, '+41764567890'),
	(5, '+41755678901'),
	(6, '+41746789012');

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_personne
DROP TABLE IF EXISTS `t_personne`;
CREATE TABLE IF NOT EXISTS `t_personne` (
  `id_personne` int NOT NULL AUTO_INCREMENT,
  `prenom` varchar(100) DEFAULT NULL,
  `nom` varchar(100) DEFAULT NULL,
  `fk_email` int DEFAULT NULL,
  `fk_num_tel` int DEFAULT NULL,
  `fk_adresse` int DEFAULT NULL,
  PRIMARY KEY (`id_personne`),
  KEY `fk_email` (`fk_email`),
  KEY `fk_num_tel` (`fk_num_tel`),
  KEY `fk_adresse` (`fk_adresse`),
  CONSTRAINT `t_personne_ibfk_1` FOREIGN KEY (`fk_email`) REFERENCES `t_email` (`id_email`),
  CONSTRAINT `t_personne_ibfk_2` FOREIGN KEY (`fk_num_tel`) REFERENCES `t_num_tel` (`id_num_tel`),
  CONSTRAINT `t_personne_ibfk_3` FOREIGN KEY (`fk_adresse`) REFERENCES `t_adresse` (`id_adresse`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_personne : ~7 rows (environ)
INSERT INTO `t_personne` (`id_personne`, `prenom`, `nom`, `fk_email`, `fk_num_tel`, `fk_adresse`) VALUES
	(1, 'Benjamin', 'Breuil', 1, 1, 1),
	(2, 'Alexandre', 'Breuil', NULL, NULL, NULL),
	(3, 'ddd', NULL, NULL, NULL, NULL),
	(4, 'asfasf', NULL, NULL, NULL, NULL),
	(5, 'fasf', NULL, NULL, NULL, NULL),
	(6, NULL, 'asfasf', NULL, NULL, NULL),
	(7, 'rqwr', 'qwrq', NULL, NULL, NULL);

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_role
DROP TABLE IF EXISTS `t_role`;
CREATE TABLE IF NOT EXISTS `t_role` (
  `id_role` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_role : ~0 rows (environ)

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_technique
DROP TABLE IF EXISTS `t_technique`;
CREATE TABLE IF NOT EXISTS `t_technique` (
  `id_technique` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id_technique`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_technique : ~18 rows (environ)
INSERT INTO `t_technique` (`id_technique`, `name`, `description`) VALUES
	(1, 'Jiu-jitsu basics', 'Ensemble de techniques de base du Jiu-jitsu Brésilien'),
	(2, 'Guard pass', 'Techniques pour passer la garde de l\'adversaire'),
	(3, 'Sweeps', 'Techniques pour renverser l\'adversaire depuis la garde'),
	(4, 'Takedowns', 'Techniques pour amener l\'adversaire au sol'),
	(5, 'Submissions', 'Techniques pour soumettre l\'adversaire'),
	(6, 'Triangle choke', 'Le Triangle choke est une technique d\'étranglement qui consiste à coincer la tête et un bras de l\'adversaire entre ses jambes pour ensuite bloquer le cou et l\'artère carotide avec le bras libre.'),
	(7, 'Armbar', 'L\'Armbar est une technique de soumission qui consiste à hyper-extensionner le coude de l\'adversaire en bloquant son bras entre ses jambes et en appliquant une pression sur le bras.'),
	(8, 'Kimura', 'Le Kimura est une technique de soumission qui consiste à bloquer le bras de l\'adversaire en plaçant sa propre jambe sur le torse de l\'adversaire, puis en saisissant son poignet et en le tournant vers l\'arrière.'),
	(9, 'Omoplata', 'L\'Omoplata est une technique de soumission qui consiste à bloquer le bras de l\'adversaire en plaçant ses jambes en forme de ciseaux autour de son bras, puis en appliquant une pression sur l\'omoplate de l\'adversaire.'),
	(10, 'Rear naked choke', 'Le Rear naked choke est une technique d\'étranglement qui consiste à entourer le cou de l\'adversaire avec ses bras en appliquant une pression sur l\'artère carotide.'),
	(11, 'Guillotine choke', 'La Guillotine choke est une technique d\'étranglement qui consiste à coincer la tête de l\'adversaire sous son bras et à bloquer le cou en appliquant une pression sur l\'artère carotide.'),
	(12, 'Berenbolo', 'Le Berenbolo est une technique de soumission qui consiste à saisir la cheville de l\'adversaire et à pivoter sur son dos pour obtenir une position dominante.'),
	(13, 'De la Riva guard', 'La De la Riva guard est une position de garde qui consiste à enrouler sa jambe autour de la jambe de l\'adversaire pour ensuite bloquer sa hanche et prendre le contrôle de la situation.'),
	(14, 'Spider guard', 'La Spider guard est une position de garde qui consiste à utiliser ses jambes pour bloquer les bras de l\'adversaire et prendre le contrôle de la situation.'),
	(15, 'X-guard', 'La X-guard est une position de garde qui consiste à enrouler ses jambes autour de la jambe de l\'adversaire pour ensuite le basculer et prendre le contrôle de la situation.'),
	(16, 'Half guard', 'La Half guard est une position de garde qui consiste à bloquer une jambe de l\'adversaire en passant une jambe en dessous et en mettant son poids sur sa hanche.'),
	(17, 'Mount', 'Le Mount est une position dominante qui consiste à monter sur le torse de l\'adversaire en prenant appui sur ses jambes.'),
	(18, 'Side control', 'Le Side control est une position dominante qui consiste à se placer sur le côté de l\'adversaire en bloquant ses bras et ses jambes.');

-- Listage de la structure de table BREUIL_BENJAMIN_INFO1C_JJB_164_2023. t_zone_echauffer
DROP TABLE IF EXISTS `t_zone_echauffer`;
CREATE TABLE IF NOT EXISTS `t_zone_echauffer` (
  `id_zone_echauffer` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_zone_echauffer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table BREUIL_BENJAMIN_INFO1C_JJB_164_2023.t_zone_echauffer : ~0 rows (environ)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
