# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:54:16 2023

@author: Mario
"""

from .entities import entities as entity
from database import connectdb as conn
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


class Model:

    @classmethod
    def delete_user(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "update users_centenario set user_delete = 'False' where user_name = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return 1
                else:
                    return 0
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def setenable_user(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                user = self.get_userbyusername(id)
                if user:
                    user_state = user.get('user')['user_state']
                    cursor.execute(
                        "update users_centenario set user_state = '{0}' where user_name = '{1}'".format(not user_state, id))
                    row_affects = cursor.rowcount
                    connection.commit()
                    if row_affects > 0:
                        return 1
                    else:
                        return 0
                else:
                    return -1
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_genders(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select * from gender order by id_gender asc;")
            rows = cursor.fetchall()
            if rows:
                return entity.Entity.genderList(rows)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_rols(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select * from rol_user order by id_rol asc;")
            rows = cursor.fetchall()
            if rows:
                return entity.Entity.rolList(rows)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_users(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from gender g inner join person p on p.gender = g.id_gender inner join users_centenario u on u.person = p.id_person inner join rol_user ru on ru.id_rol = u.rol_user where u.user_delete = 'True' order by u.id_user desc;")
            rows = cursor.fetchall()
            if rows:
                return entity.Entity.ListUsers(rows)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_userbyusername(self, username):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from gender g inner join person p on p.gender = g.id_gender inner join users_centenario u on u.person = p.id_person inner join rol_user ru on ru.id_rol = u.rol_user where u.user_name = '{0}' and u.user_delete = 'True';".format(username))
            row = cursor.fetchone()
            if row:
                return entity.Entity.entityUser(row)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_userbyemail(self, email):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from gender g inner join person p on p.gender = g.id_gender inner join users_centenario u on u.person = p.id_person inner join rol_user ru on ru.id_rol = u.rol_user where u.email = '{0}' and u.user_delete = 'True';;".format(email))
            row = cursor.fetchone()
            if row:
                return entity.Entity.entityUser(row)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_userbyid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from gender g inner join person p on p.gender = g.id_gender inner join users_centenario u on u.person = p.id_person inner join rol_user ru on ru.id_rol = u.rol_user where u.id_user = '{0}' and u.user_delete = 'True';;".format(id))
            row = cursor.fetchone()
            if row:
                return entity.Entity.entityUser(row)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login_user(self, data):
        try:
            user = self.get_userbyemail(
                data['id_user']) or self.get_userbyusername(data['id_user'])
            if user:
                if check_password_hash(user.get('user')['password'], data['password']) and user.get('user')['user_state']:
                    return user
                elif check_password_hash(user.get('user')['password'], data['password']) is False:
                    return 2
                elif user.get('user')['user_state'] is False:
                    return 1
            else:
                return -1
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def change_password(self, id, data):
        try:
            connection = conn.get_connection()
            user = self.get_userbyemail(id) or self.get_userbyusername(id)
            rows_affect = -1
            if user:
                if check_password_hash(user.get('user')['password'], data['password']):
                    hash_pwd = generate_password_hash(data['new_password'])
                    if check_password_hash(hash_pwd, data['confirm_password']):
                        cursor = connection.cursor()
                        cursor.execute("update users_centenario set password = '{0}' where id_user  = {1};".format(
                            hash_pwd, user.get('user')['id_user']))
                        connection.commit()
                        rows_affect = cursor.rowcount
                    else:
                        rows_affect = 2
                else:
                    rows_affect = 3
            return rows_affect
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_user(self, data):
        try:
            us = self.get_userbyemail(
                data['email']) or self.get_userbyusername('ADM-{0}'.format(data['card_id_person'])) or self.get_userbyusername('PRE-{0}'.format(data['card_id_person'])) or self.get_userbyusername('EMP-{0}'.format(data['card_id_person'])) or self.get_userbyusername('SEC-{0}'.format(data['card_id_person'])) or self.get_userbyusername('CUS-{0}'.format(data['card_id_person']))
            if us:
                return -1
            else:
                connection = conn.get_connection()
                with connection.cursor() as cursor:
                    f = datetime.datetime.now()
                    fecha = "{0}/{1}/{2}".format(f.month, f.day, f.year)
                    cursor.execute("insert into person(card_id_person, first_name, last_name, phone, address, gender, date_born) values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}') returning id_person;".format(
                        data['card_id_person'], data['first_name'], data['last_name'], data['phone'], data['address'], data['gender'], data['date_born']))
                    id_person = cursor.fetchone()[0]
                    iduser = ''
                    if int(data['id_rol']) == 1:
                        iduser = 'PRE-' + data['card_id_person']
                    if int(data['id_rol']) == 2:
                        iduser = 'EMP-' + data['card_id_person']
                    if int(data['id_rol']) == 3:
                        iduser = 'SEC-' + data['card_id_person']
                    if int(data['id_rol']) == 4:
                        iduser = 'CUS-' + data['card_id_person']
                    # fecha = datetime.strptime(data['user_fecha'], '%d/%m/%Y')
                    password = data['password']
                    hashed = generate_password_hash(password)
                    query = "INSERT INTO users_centenario(user_name, email, password, login_code, user_state, register_date,person, rol_user, user_delete) values('{0}', '{1}', '{2}','{3}', '{4}', '{5}', '{6}', '{7}', 'True')".format(
                        iduser, data['email'], hashed, '0', 'True', fecha, id_person, data['id_rol'])
                    cursor.execute(query)
                    """
                    if int(data['rol_idrol']) == 1:
                        cursor.execute(
                            "INSERT INTO presidente(user_idusuario) values('{0}')".format(iduser))
                    if int(data['rol_idrol']) == 2:
                        cursor.execute(
                            "INSERT INTO secretario(user_idusuario) values('{0}')".format(iduser))
                    if int(data['rol_idrol']) == 3:
                        cursor.execute(
                            "INSERT INTO tesorero(user_idusuario) values('{0}')".format(iduser))
                    if int(data['rol_idrol']) == 4:
                        cursor.execute(
                            "INSERT INTO condomino(user_idusuario) values('{0}')".format(iduser))
                    """
                    rows_affects = cursor.rowcount
                    connection.commit()
                    """
                    da = {
                        "user_idusuario": iduser,
                        "user_password": hashed,
                        "user_estado": 0,
                        "user_email": data['pers_email']
                    }
                    """
                    if rows_affects > 0:
                        # print(self.create_users(da))
                        user = self.get_userbyusername(iduser)
                        return user
                    else:
                        return {'message': 'Error, Insert user failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(self, data, id_user):
        try:
            us = self.get_userbyid(id_user)
            if us:
                connection = conn.get_connection()
                with connection.cursor() as cursor:
                    cursor.execute(
                        "update person set first_name = '{0}', card_id_person = '{1}', last_name = '{2}', phone = '{3}', address = '{4}', gender = '{5}', date_born = '{6}' where card_id_person = '{7}';".format(data['first_name'], data['card_id_person'], data['last_name'], data['phone'], data['address'], data['gender'], data['date_born'], (us.get('user')['person'])['card_id_person']))
                    username = ''
                    if int(data['id_rol']) == 1:
                        username = 'PRE-' + data['card_id_person']
                    if int(data['id_rol']) == 2:
                        username = 'EMP-' + data['card_id_person']
                    if int(data['id_rol']) == 3:
                        username = 'SEC-' + data['card_id_person']
                    if int(data['id_rol']) == 4:
                        username = 'CUS-' + data['card_id_person']
                    cursor.execute(
                        "update users_centenario set email = '{0}', rol_user = '{1}', user_name = '{2}' where id_user = '{3}';".format(data['email'], data['id_rol'], username, id_user))
                    connection.commit()
                    row_affects = cursor.rowcount
                    if row_affects > 0:
                        us = self.get_userbyid(id_user)
                        return us
                    else:
                        return None
            else:
                return -1
        except Exception as ex:
            raise Exception(ex)
