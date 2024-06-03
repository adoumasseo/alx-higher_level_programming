-- script that prints the full description of the table first_table
-- The database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);
-- Commande to insert the data
INSERT INTO second_table VALUES 
  (1, "John", 10),
  (2, "Alex", 3),
  (3, "Bob", 14),
  (4, "George", 8);
