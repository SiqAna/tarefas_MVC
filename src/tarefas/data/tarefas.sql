DROP TABLE IF EXISTS `tarefas`;

CREATE DATABASE IF NOT EXISTS `tarefas`;

USE `tarefas`;

DROP TABLE IF EXISTS `tarefas`;

CREATE TABLE IF NOT EXISTS `tarefas`(
    `id_tarefas` INT NOT NULL PRIMARY KEY,
    `titulo_tarefa` VARCHAR(100) NOT NULL,
    `data_conclusão` DATETIME NULL
)