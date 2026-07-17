CREATE DATABASE prime;

use prime;

select @@autocommit;
set autocommit =0;

CREATE TABLE accounts (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
balance DECIMAL(10, 2)
);

INSERT INTO accounts (name, balance) VALUES
('Adam', 500.00),
('Bob', 300.00),
('Charlie', 1000.00);

select * from accounts;

START TRANSACTION;
UPDATE accounts SET balance=balance-100 WHERE id=1;
UPDATE accounts SET balance=balance+100 WHERE id=2;
COMMIT;

-- START TRANSACTION;
-- UPDATE accounts SET balance=balance-100 WHERE id=1;
-- UPDATE accounts SET balance=balan ce+100 WHERE id=2;
-- ROLLBACK;


-- SAVE POINTS-----------------

START TRANSACTION;

UPDATE accounts SET balance = balance + 1000 WHERE id = 1;
SAVEPOINT after_wallet_topup;

UPDATE accounts SET balance = balance + 10 WHERE id = 1;

ROLLBACK TO after_wallet_topup;

COMMIT;