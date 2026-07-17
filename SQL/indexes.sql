CREATE TABLE account (
account_id INT PRIMARY KEY,
name VARCHAR(50),
balance DECIMAL(10, 2),
branch VARCHAR(50)
);

INSERT INTO account VALUES
(1, 'Adam', 500.00, 'Mumbai'),
(2, 'Bob', 300.00, 'Delhi'),
(3, 'Charlie', 700.00, 'Bangalore'),
(4, 'David', 1000.00, 'Noida');

select * from account;


CREATE INDEX idx_branch ON account(branch);

show index from account;

drop index idx2 on account;

-- composite index

CREATE INDEX idx2 ON account(branch, balance);