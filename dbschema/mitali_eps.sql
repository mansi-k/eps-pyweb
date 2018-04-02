
CREATE TABLE registration (
r_id NUMBER(10) NOT NULL,
r_uid NUMBER(10),
r_eid NUMBER(10),
r_is_approved VARCHAR2(5),
PRIMARY KEY (r_id)
);

insert into registration values (1,4,1,'yes');
insert into registration values (2,10,1,'yes');
insert into registration values (3,11,1,'yes');
insert into registration values (4,5,2,'yes');
insert into registration values (5,13,2,'yes');
insert into registration values (6,6,3,'yes');
insert into registration values (7,12,3,'yes');

create table phfexcityb as select * from mansi.exhibition where ex_city='banglore';

create table dhfregexb as (select a.*, b.ex_city from registration a, phfexcityb b where a.r_eid=b.ex_id);

CREATE OR REPLACE TRIGGER VFREG_INSERT
AFTER INSERT ON REGISTRATION
FOR EACH ROW
DECLARE
D VARCHAR2(50);
BEGIN
SELECT EX_CITY INTO D FROM mansi.EXHIBITION WHERE EX_ID = :NEW.R_EID;
IF D='mumbai'  THEN
INSERT INTO reshma.dhfregexm VALUES( :NEW.R_ID,:NEW.R_UID,:NEW.R_EID,:NEW.R_IS_APPROVED,D);
ELSIF D='banglore'  THEN
INSERT INTO dhfregexb VALUES( :NEW.R_ID,:NEW.R_UID,:NEW.R_EID,:NEW.R_IS_APPROVED,D);
ELSIF D='delhi' THEN
INSERT INTO sarthak.dhfregexd VALUES( :NEW.R_ID,:NEW.R_UID,:NEW.R_EID,:NEW.R_IS_APPROVED,D);
ELSE
INSERT INTO mansi.dhfregexo VALUES( :NEW.R_ID,:NEW.R_UID,:NEW.R_EID,:NEW.R_IS_APPROVED,D);
END IF;
END;
/

Create or replace trigger vfreg_delete
After delete on registration
For each row
Begin
Delete from dhfregexb where dhfregexb.r_id = :old.r_id;
Delete from reshma.dhfregexm where reshma.dhfregexm.r_id = :old.r_id;
Delete from sarthak.dhfregexd where sarthak.dhfregexd.r_id = :old.r_id;
Delete from mansi.dhfregexo where mansi.dhfregexo.r_id = :old.r_id;
end;
/

insert into registration values (8,13,3,'yes');

commit;