-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: 22-Jun-2018 às 19:29
-- Versão do servidor: 5.7.21
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `controla_saldo`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `abastecimentos`
--

DROP TABLE IF EXISTS `abastecimentos`;
CREATE TABLE IF NOT EXISTS `abastecimentos` (
  `id_abastecimento` int(11) NOT NULL AUTO_INCREMENT,
  `id_produto` int(11) DEFAULT NULL,
  `id_transportadora` int(11) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `placa` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `km` int(11) DEFAULT NULL,
  `km_ant` int(11) DEFAULT NULL,
  `media` double DEFAULT NULL,
  `litros` int(11) DEFAULT NULL,
  `num_cont` int(11) DEFAULT NULL,
  `sinc` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_abastecimento`),
  KEY `fk_abastecimentos_produtos_idx` (`id_produto`),
  KEY `fk_abastecimentos_transportadoras1_idx` (`id_transportadora`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `abastecimentos`
--

INSERT INTO `abastecimentos` (`id_abastecimento`, `id_produto`, `id_transportadora`, `data`, `hora`, `placa`, `km`, `km_ant`, `media`, `litros`, `num_cont`, `sinc`) VALUES
(4, 1, 1, '2018-06-14', '05:10:00', 'ARZ1150', 824358, 822294, 20.64, 100, 1962, 1),
(3, 1, 1, '2018-06-14', '10:46:00', 'ADZ0907', 1326416, 326070, 7358.73, 136, 2016, 1),
(5, 1, 1, '2018-06-14', '17:45:00', 'AUR5835', 632983, 632485, 4.53, 110, 1987, 1),
(6, 1, 1, '2018-06-14', '05:15:00', 'BAU8904', 197663, 196600, 28.96, 37, 1961, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `abastecimentos_auditoria`
--

DROP TABLE IF EXISTS `abastecimentos_auditoria`;
CREATE TABLE IF NOT EXISTS `abastecimentos_auditoria` (
  `id_abastecimento` int(11) NOT NULL AUTO_INCREMENT,
  `id_produto` int(11) DEFAULT NULL,
  `id_transportadora` int(11) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `placa` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `km` int(11) DEFAULT NULL,
  `km_ant` int(11) DEFAULT NULL,
  `media` double DEFAULT NULL,
  `litros` int(11) DEFAULT NULL,
  `num_cont` int(11) DEFAULT NULL,
  `sinc` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_abastecimento`),
  KEY `fk_abastecimentos_produtos_idx` (`id_produto`),
  KEY `fk_abastecimentos_transportadoras1_idx` (`id_transportadora`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `compras`
--

DROP TABLE IF EXISTS `compras`;
CREATE TABLE IF NOT EXISTS `compras` (
  `id_compras` int(11) NOT NULL AUTO_INCREMENT,
  `id_produto` int(11) DEFAULT NULL,
  `id_transportadora` int(11) DEFAULT NULL,
  `litros` int(11) DEFAULT NULL,
  `numero_documento` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `data` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `fornecedor` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `chave` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sinc` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_compras`),
  KEY `fk_compras_produtos1_idx` (`id_produto`),
  KEY `fk_compras_transportadoras1_idx` (`id_transportadora`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `compras`
--

INSERT INTO `compras` (`id_compras`, `id_produto`, `id_transportadora`, `litros`, `numero_documento`, `data`, `hora`, `fornecedor`, `chave`, `sinc`) VALUES
(4, 1, 1, 5000, '000314807', '2018-06-14', '08:29:00', 'IPIRANGA', '1406201800001000314807', 1),
(3, 1, 1, 5000, '000314809', '2018-06-14', '11:00:00', 'IPIRANGA', '1406201800004000314809', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `produtos`
--

DROP TABLE IF EXISTS `produtos`;
CREATE TABLE IF NOT EXISTS `produtos` (
  `id_produto` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `codigo` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_produto`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `produtos`
--

INSERT INTO `produtos` (`id_produto`, `nome`, `codigo`) VALUES
(1, 'etanol', '1');

-- --------------------------------------------------------

--
-- Estrutura da tabela `temp_del_compras`
--

DROP TABLE IF EXISTS `temp_del_compras`;
CREATE TABLE IF NOT EXISTS `temp_del_compras` (
  `id_temp_del_compras` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `chave` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_temp_del_compras`),
  UNIQUE KEY `id_temp_del_compras` (`id_temp_del_compras`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tmp_abastec`
--

DROP TABLE IF EXISTS `tmp_abastec`;
CREATE TABLE IF NOT EXISTS `tmp_abastec` (
  `id_abastecimento` int(11) NOT NULL AUTO_INCREMENT,
  `id_produto` int(11) DEFAULT NULL,
  `id_transportadora` int(11) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `placa` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `km` int(11) DEFAULT NULL,
  `km_ant` int(11) DEFAULT NULL,
  `media` double DEFAULT NULL,
  `litros` int(11) DEFAULT NULL,
  `num_cont` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_abastecimento`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tmp_cmp`
--

DROP TABLE IF EXISTS `tmp_cmp`;
CREATE TABLE IF NOT EXISTS `tmp_cmp` (
  `id_compras` int(11) NOT NULL AUTO_INCREMENT,
  `id_produto` int(11) DEFAULT NULL,
  `id_transportadora` int(11) DEFAULT NULL,
  `litros` int(11) DEFAULT NULL,
  `numero_documento` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `data` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `fornecedor` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `chave` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_compras`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `transportadoras`
--

DROP TABLE IF EXISTS `transportadoras`;
CREATE TABLE IF NOT EXISTS `transportadoras` (
  `id_transportadora` int(11) NOT NULL AUTO_INCREMENT,
  `nome_fantasia` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cnpj` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `telefone` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cod_pes` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_transportadora`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `transportadoras`
--

INSERT INTO `transportadoras` (`id_transportadora`, `nome_fantasia`, `cnpj`, `telefone`, `cod_pes`) VALUES
(1, '21', '1231', '56', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `transportadoras_saldo`
--

DROP TABLE IF EXISTS `transportadoras_saldo`;
CREATE TABLE IF NOT EXISTS `transportadoras_saldo` (
  `id_transportadora_saldo` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_produto` int(11) DEFAULT NULL,
  `id_transportadora` int(11) DEFAULT NULL,
  `saldo` int(11) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  PRIMARY KEY (`id_transportadora_saldo`),
  KEY `fk_transportadoras_saldo_transportadoras1_idx` (`id_transportadora`),
  KEY `fk_transportadoras_saldo_produtos1_idx` (`id_produto`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `transportadoras_saldo`
--

INSERT INTO `transportadoras_saldo` (`id_transportadora_saldo`, `id_produto`, `id_transportadora`, `saldo`, `data`, `hora`) VALUES
(22, 1, 1, 9617, '2018-06-14', '05:15:00');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int(10) UNSIGNED NOT NULL,
  `nome` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `login` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `senha` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
