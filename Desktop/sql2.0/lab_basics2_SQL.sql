SELECT * FROM client;
SELECT * FROM account;

-- Get the id values of the first 5 clients from district_id with a value equals to 1.

select district_id, client_id from client
where district_id = 1
group by client_id; 
-- the first clients in district 1 were the clients IDs 2,3,22,23,28

-- In the client table, get an id value of the last client where the district_id equals to 72.

select client_id, district_id from client
where district_id = 72
group by client_id;
-- ID of last client of district 72: 49. Newest client in this district: 13576

-- Get the 3 lowest amounts in the loan table:

select * from loan;

select min(amount) from loan
limit 3; -- this way gives only the minimum

select amount from loan
order by amount asc
limit 3;
-- The 3 lowest quantities are 4980, 5148, 7656

-- What are the possible values for status, ordered alphabetically in ascending order in the loan table?

select status from loan
order by status asc;

select distinct status from loan
order by status asc;

-- What is the loan_id of the highest payment received in the loan table?

select loan_id, amount from loan
order by amount desc;

-- 6534

-- What is the loan amount of the lowest 5 account_ids in the loan table? Show the account_id and the corresponding amount?

select account_id, amount from loan
order by account_id asc
limit 5;

select account_id from loan;

--

