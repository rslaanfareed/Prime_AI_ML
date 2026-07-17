
DELIMITER $$

CREATE PROCEDURE check_balance(IN acc_id INT)
BEGIN
SELECT balance
FROM account
WHERE account_id = acc_id;
END $$

DELIMITER ;


-- CALL THE PROCEDURE

CALL check_balance(1);
select * from account;


drop procedure if exists check_balance;


-- returning value

DELIMITER $$

CREATE PROCEDURE check_balance(IN acc_id INT, OUT bal DECIMAL(10, 2))
BEGIN
SELECT balance INTO bal
FROM account
WHERE account_id = acc_id;
END $$

DELIMITER ;

CALL check_balance(1, @balance);
SELECT @balance;