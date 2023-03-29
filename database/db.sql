create table entity(
    id serial not null,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    
);

-- Usuarios
-- Clientes
-- Transporte
-- Documentos
-- Egresos
-- Ingresos
-- Multas
-- Pagos Mensuales
-- Reuniones 
-- Pago de servicios
-- 

create table gender(
    id_gender serial not null,
    gender_name varchar(50) not null,
    constraint pk_gender primary key(id_gender)
);

insert into gender(gender_name) values('Male');
insert into gender(gender_name) values('Female');

create table person(
    id_person serial not null,
    card_id_person varchar(13) not null unique,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    phone varchar(15) not null,
    address varchar(100) not null,
    gender integer not null,
    date_born date not null,
    constraint pk_person primary key(id_person),
    constraint fk_gender_person foreign key(gender) references gender(id_gender) 
);

insert into person(card_id_person, first_name, last_name, phone, address, gender, date_born) values('1003938410', 'Mario', 'Salazar', '0979432426', 'Ibarra - El Tejar', 1, '02/02/1995');

insert into person(card_id_person, first_name, last_name, phone, address, gender, date_born) values('1003938477', 'Elenita', 'Rueda', '0979432410', 'Ibarra - San Francisco del Tejar', 1, '12/02/2012');

create table rol_user(
    id_rol serial not null,
    rol_name varchar(100) not null,
    constraint pk_rol_user primary key(id_rol)
);

insert into rol_user(rol_name) values('Rol user Manager');
insert into rol_user(rol_name) values('Rol user Employed');
insert into rol_user(rol_name) values('Rol user Secretary');

create table users(
    id_user serial not null,
    user_name varchar(100) not null unique,
    email varchar(100) not null unique,
    password varchar(200) not null,
    login_code varchar(10) not null,
    user_state boolean not null,
    register_date date not null,
    person integer not null,
    constraint pk_user primary key(id_user),
    constraint fk_person_user foreign key(person) references person(id_person)
);

insert into users(user_name, email, password, login_code, user_state, register_date, person) values('ADM-1003938410', 'elenitarueda@gmail.com', 'password-elenita', '0000', 'True', '', '1003938410');


alter table users add column rol_user integer;
update users set rol_user = 1;

alter table users 
add constraint fk_rol_users foreign key(rol_user) references rol_user(id_rol);

/*

conda create -n nombreenv python=x.x
source activate nombreenv
conda env list
Para instalar paquetes dentro de nuestro entorno virtual podemos hacerlo mediante pip o con el instalador de anaconda.

pip install nombredelpaquete
o bien

conda install nombredelpaquete
De igual manera podemos ver los paquetes y la versión que tiene instalado nuestro entorno

conda list -n nombreenv

*/