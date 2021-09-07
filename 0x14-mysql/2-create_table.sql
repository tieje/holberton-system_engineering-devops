create table rando(
    id int not null AUTO_INCREMENT,
    name varchar(100) not null,
    primary key (id)
);

insert into rando (id, name)
values (
    1, 'jeff'
);
