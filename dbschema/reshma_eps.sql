
CREATE TABLE usertype(
ut_id  NUMBER(10) NOT NULL,
ut_type VARCHAR(20) NOT NULL,
PRIMARY KEY (ut_id)
);

insert into usertype values (1, 'exhibitor');
insert into usertype values (2, 'enterprise');
insert into usertype values (3, 'visitor');

CREATE TABLE useracc(
u_id NUMBER(10) NOT NULL ,
u_type NUMBER(10),
u_name VARCHAR(20) NOT NULL,
u_mobno NUMBER(10) NOT NULL,
u_address VARCHAR(100) NOT NULL,
u_city VARCHAR(20) NOT NULL,
u_email VARCHAR(20),
u_documents VARCHAR(50),
u_is_verified VARCHAR(5),
u_password VARCHAR(20),
PRIMARY KEY (u_id)
);


ALTER TABLE useracc ADD FOREIGN KEY (u_type) REFERENCES usertype (ut_id) ON DELETE CASCADE;


insert into useracc values (1, 1, 'grand exhibitors', '999999888', 'grand corporate sector', 'delhi', 'grand.ex@gmail.com', 'gex.doc', 'yes', 'pswd123');
insert into useracc values (2, 1, 'vision exhibitors', '779999888', 'vision corporate sector 2', 'mumbai', 'vision.ex@gmail.com', 'vex.doc', 'yes', 'pswd123');
insert into useracc values (3, 1, 'global exhibitors', '995599888', 'global-exchange corporate sector', 'banglore', 'global.ex@gmail.com', 'glex.doc', 'yes', 'pswd123');

insert into useracc values (4, 2, 'Good AI Lab', '888888888', 'AI Tech Park', 'banglore', 'good.ai@gmail.com', 'gail.doc', 'yes', 'pswd123');
insert into useracc values (5, 2, 'Honda autos', '888877788', 'Honda auto Park', 'delhi', 'honda.auto@gmail.com', 'ha.doc', 'yes', 'pswd123');
insert into useracc values (6, 2, 'JJ arts', '789588888', 'JJ school of arts', 'mumbai', 'jj.arts@gmail.com', 'jj.doc', 'yes', 'pswd123');
insert into useracc values (7, 2, 'Clusterone AI Lab', '888888222', 'cluster Tech Park', 'delhi', 'clusterone@gmail.com', 'c.doc', 'yes', 'pswd123');
insert into useracc values (8, 2, 'Bajaj autos', '888888555', 'bajaj auto Park', 'banglore', 'bajaj.auto@gmail.com', 'ba.doc', 'yes', 'pswd123');
insert into useracc values (9, 2, 'DSK arts', '733888888', 'DSK school', 'mumbai', 'dsk@gmail.com', 'd.doc', 'yes', 'pswd123');

insert into useracc values (10, 3, 'mansi khamkar', '8692023065', 'R.C.F. Colony', 'mumbai', 'kmansi@gmail.com', '', '', 'pswd123');
insert into useracc values (11, 3, 'reshma khot', '959595959', 'kamothe', 'mumbai', 'kreshma@gmail.com', '', '', 'pswd123');
insert into useracc values (12, 3, 'mital ochani', '828282828', 'gulab park', 'delhi', 'omitali@gmail.com', '', '', 'pswd123');
insert into useracc values (13, 3, 'sathak khanna', '959595000', 'basant park', 'banglore', 'ksarthak@gmail.com', '', '', 'pswd123');

grant all privilege to mansi;

create table phfexcitym as select * from mansi.exhibition where ex_city='mumbai';

create table dhfregexm as (select a.*, b.ex_city from mitali.registration a, phfexcitym b where a.r_eid=b.ex_id);

commit;





