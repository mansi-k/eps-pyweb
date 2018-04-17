
CREATE TABLE cat (
cat_id NUMBER(10) NOT NULL,
cat_name VARCHAR2(20) NOT NULL,
PRIMARY KEY (cat_id)
);

insert into cat values (1,'technology');
insert into cat values(2,'art');
insert into cat values(3,'automobile');

CREATE TABLE exhibition (
ex_id NUMBER(10) NOT NULL,
ex_name VARCHAR2(20) NOT NULL,
ex_cat_id NUMBER(10),
ex_address VARCHAR2(100) NOT NULL,
ex_city VARCHAR2(20),
ex_start_date TIMESTAMP DEFAULT(NULL),
ex_end_date TIMESTAMP DEFAULT(NULL),
ex_creator_id NUMBER(10), 
ex_doc VARCHAR2(50),
ex_is_verified VARCHAR2(5),
ex_is_vrr VARCHAR2(5),
ex_note VARCHAR2(100),
PRIMARY KEY (ex_id)
);      

ALTER TABLE exhibition ADD FOREIGN KEY (ex_creator_id) REFERENCES reshma.useracc (u_id) ON DELETE CASCADE;

ALTER TABLE exhibition ADD FOREIGN KEY (ex_cat_id) REFERENCES cat (cat_id) ON DELETE CASCADE;

INSERT INTO EXHIBITION VALUES (1,'AI Robos',1,'Tech mall 5','delhi',TIMESTAMP '2018-04-26 09:00:00.00',TIMESTAMP '2018-04-28 18:00:00.00',2,'ex1.pdf',null,'yes','');
INSERT INTO EXHIBITION VALUES (2,'Electric Auto Expo',3,'Auto Expo mall 2','mumbai',TIMESTAMP '2018-05-07 10:00:00.00',TIMESTAMP '2018-05-08 17:00:00.00',3,'ex2.pdf',null,'yes','');
INSERT INTO EXHIBITION VALUES (3,'books by weight',2,'Book mall 3','banglore',TIMESTAMP '2018-04-16 09:00:00.00',TIMESTAMP '2018-04-21 18:00:00.00',1,'ex3.pdf',null,'yes','');
INSERT INTO EXHIBITION VALUES (4,'Instant services',1,'Tech mall 2','banglore',TIMESTAMP '2018-05-7 09:00:00.00',TIMESTAMP '2018-05-10 18:00:00.00',3,'ex4.pdf',null,'yes','');
INSERT INTO EXHIBITION VALUES (5,'self driving autos',3,'auto hub 6','delhi',TIMESTAMP '2018-05-21 09:00:00.00',TIMESTAMP '2018-05-24 18:00:00.00',2,'ex5.pdf',null,'yes','');
INSERT INTO EXHIBITION VALUES (6,'Novels Expo',2,'Global library 1','mumbai',TIMESTAMP '2018-05-28 09:00:00.00',TIMESTAMP '2018-05-31 18:00:00.00',1,'ex6.pdf',null,'yes','');

update cat set cat_name='books' where cat_id=2;

create table phfexcityo as select * from mansi.exhibition where ex_city!='delhi' and ex_city!='banglore' and ex_city!='mumbai';

CREATE OR REPLACE TRIGGER HFEX_INSERT
AFTER INSERT ON EXHIBITION
FOR EACH ROW
BEGIN
IF(:NEW.EX_CITY='mumbai') THEN
INSERT INTO reshma.phfexcitym
VALUES(:NEW.EX_ID,
:NEW.EX_NAME,
:NEW.EX_CAT_ID,
:NEW.EX_ADDRESS,
:NEW.EX_CITY,
:NEW.EX_START_DATE,
:NEW.EX_END_DATE,
:NEW.EX_CREATOR_ID,
:NEW.EX_DOC,
:NEW.EX_IS_VERIFIED,
:NEW.EX_IS_VRR,
:NEW.EX_NOTE);
ELSIF(:NEW.EX_CITY='delhi') THEN
INSERT INTO sarthak.phfexcityd
VALUES(:NEW.EX_ID,
:NEW.EX_NAME,
:NEW.EX_CAT_ID,
:NEW.EX_ADDRESS,
:NEW.EX_CITY,
:NEW.EX_START_DATE,
:NEW.EX_END_DATE,
:NEW.EX_CREATOR_ID,
:NEW.EX_DOC,
:NEW.EX_IS_VERIFIED,
:NEW.EX_IS_VRR,
:NEW.EX_NOTE);
ELSIF(:NEW.EX_CITY='banglore') THEN
INSERT INTO mitali.phfexcityb
VALUES(:NEW.EX_ID,
:NEW.EX_NAME,
:NEW.EX_CAT_ID,
:NEW.EX_ADDRESS,
:NEW.EX_CITY,
:NEW.EX_START_DATE,
:NEW.EX_END_DATE,
:NEW.EX_CREATOR_ID,
:NEW.EX_DOC,
:NEW.EX_IS_VERIFIED,
:NEW.EX_IS_VRR,
:NEW.EX_NOTE);
ELSE
INSERT INTO phfexcityo
VALUES(:NEW.EX_ID,
:NEW.EX_NAME,
:NEW.EX_CAT_ID,
:NEW.EX_ADDRESS,
:NEW.EX_CITY,
:NEW.EX_START_DATE,
:NEW.EX_END_DATE,
:NEW.EX_CREATOR_ID,
:NEW.EX_DOC,
:NEW.EX_IS_VERIFIED,
:NEW.EX_IS_VRR,
:NEW.EX_NOTE);
END IF;
END;
/

INSERT INTO EXHIBITION VALUES (7,'Cloud computing',1,'Cloud center mall 8','mumbai',TIMESTAMP '2018-06-06 09:00:00.00',TIMESTAMP '2018-06-08 18:00:00.00',2,'ex7.pdf',null,'yes','');

create or replace trigger hfex_update
after update
on exhibition
for each row
begin
update reshma.phfexcitym
set ex_id=:new.ex_id, 
ex_name=:new.ex_name,
ex_cat_id=:new.ex_cat_id,
ex_address=:new.ex_address,
ex_start_date=:new.ex_start_date,
ex_end_date=:new.ex_end_date,
ex_is_verified=:new.ex_is_verified,
ex_is_vrr=:new.ex_is_vrr,
ex_note=:new.ex_note
where ex_id=:old.ex_id;
update mitali.phfexcityb
set ex_id=:new.ex_id, 
ex_name=:new.ex_name,
ex_cat_id=:new.ex_cat_id,
ex_address=:new.ex_address,
ex_start_date=:new.ex_start_date,
ex_end_date=:new.ex_end_date,
ex_is_verified=:new.ex_is_verified,
ex_is_vrr=:new.ex_is_vrr,
ex_note=:new.ex_note
where ex_id=:old.ex_id;
update sarthak.phfexcityd
set ex_id=:new.ex_id, 
ex_name=:new.ex_name,
ex_cat_id=:new.ex_cat_id,
ex_address=:new.ex_address,
ex_start_date=:new.ex_start_date,
ex_end_date=:new.ex_end_date,
ex_is_verified=:new.ex_is_verified,
ex_is_vrr=:new.ex_is_vrr,
ex_note=:new.ex_note
where ex_id=:old.ex_id;
update phfexcityo
set ex_id=:new.ex_id, 
ex_name=:new.ex_name,
ex_cat_id=:new.ex_cat_id,
ex_address=:new.ex_address,
ex_start_date=:new.ex_start_date,
ex_end_date=:new.ex_end_date,
ex_is_verified=:new.ex_is_verified,
ex_is_vrr=:new.ex_is_vrr,
ex_note=:new.ex_note
where ex_id=:old.ex_id;
end;
/

update exhibition set ex_name='cloud computing expo' where ex_id=7;

create or replace trigger hfex_delete
after delete on exhibition
for each row
begin
delete from reshma.phfexcitym
where ex_id=:old.ex_id;
delete from mitali.phfexcityb
where ex_id=:old.ex_id;
delete from sarthak.phfexcityd
where ex_id=:old.ex_id;
delete from phfexcityo
where ex_id=:old.ex_id;
end;
/

create table dhfregexo as (select a.*, b.ex_city from mitali.registration a, phfexcityo b where a.r_eid=b.ex_id);

select * from exhibition;

delete from exhibition where ex_id=10;

update exhibition set ex_id=8 where ex_id=10;

select * from exhibition e left join cat c on ex_cat_id = cat_id left join mitali.registration on r_eid = ex_id and r_uid = 10 order by ex_id;

select * from phfexcityo;

select * from reshma.useracc;

commit;
