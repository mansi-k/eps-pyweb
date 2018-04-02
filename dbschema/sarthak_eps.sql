
CREATE TABLE epsadmin(
a_id NUMBER(10),
a_name VARCHAR(20) NOT NULL,
a_mobno NUMBER(10) NOT NULL,
a_address VARCHAR(100) NOT NULL,
a_city VARCHAR(20) NOT NULL,
a_email VARCHAR(20),
a_password VARCHAR(20)
);

insert into epsadmin values (1,'admin1',7777777777,'Bandra east','mumbai','admin1@gmail.com','admin1');

create table phfexcityd as select * from mansi.exhibition where ex_city='delhi';

create table dhfregexd as (select a.*, b.ex_city from mitali.registration a, phfexcityd b where a.r_eid=b.ex_id);

commit;