show databases;
create database BANKATM_PROJECT;
use BANKATM_PROJECT;
show tables;
create table mogappair_bank(name text,account int,balance int);
insert into mogappair_bank(name,account,balance) values("thrisha",525252,1000);
insert into mogappair_bank values("nayanthara",525253,2000);
select * from mogappair_bank;
select name from mogappair_bank;
select name AS NAME,account AS ACCOUNT,balance AS BALANCE from mogappair_bank;
select * from mogappair_bank;
insert into mogappair_bank 
values("dhanush",525254,3000),
      ("vijay",525255,4000),
	  ("simbu",525256,5000);
select * from mogappair_bank;
select account from mogappair_bank;
select * from mogappair_bank order by account desc;
select * from mogappair_bank where name like 'v_s%';
select * from mogappair_bank where name like 'r%n';
select mogappair_bank.name,mogappair_bank.balance from mogappair_bank;
select mogappair_bank.name,
       BankATM.name 
from mogappair_bank inner join BankATM on mogappair_bank.name=BankATM.name;
delete 
from 
mogappair_bank where name='rithvin';
select * from mogappair_bank;










