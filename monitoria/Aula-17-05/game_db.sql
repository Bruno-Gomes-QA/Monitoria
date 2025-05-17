CREATE DATABASE game_db;
USE game_db;

CREATE TABLE personagens (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  classe VARCHAR(50),
  nivel INT
);