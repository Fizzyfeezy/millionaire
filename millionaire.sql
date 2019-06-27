
CREATE TABLE if not exists question_bank(
        id varchar(40) not null unique primary key,
        question MEDIUMTEXT not null);