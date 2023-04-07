# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:53:57 2023

@author: Mario
"""


class Entity:

    @classmethod
    def entityUser(self, user) -> dict:
        if dict:
            return {
                "user": {
                    "person": {
                        "gender": {
                            "id_gender": user[0],
                            "gender_name": user[1]
                        },
                        "id_person": user[2],
                        "card_id_person": user[3],
                        "first_name": user[4],
                        "last_name": user[5],
                        "phone": user[6],
                        "address": user[7],
                        "date_born": user[9].strftime('%d/%m/%Y')
                    },
                    "id_user": user[10],
                    "user_name": user[11],
                    "email": user[12],
                    "password": user[13],
                    "login_code": user[14],
                    "user_state": user[15],
                    "register_date": user[16].strftime('%d/%m/%Y'),
                    "rol_user": {
                        "id_rol": user[20],
                        "rol_name": user[21]
                    },
                    "user_delete": user[19]
                }
            }
        else:
            return None

    @classmethod
    def ListUsers(self, users) -> list:
        return [self.entityUser(user) for user in users]


link = "https://cloud2.utn.edu.ec/ords/f?p=128%3ALOGIN_DESKTOP&fbclid=IwAR3lUpdzdn0b8J31pDg3CtOw8VkRmDdDgNM4VyqdNvhOOLBmiHEccGwGU1I"

us = {
    "user": {
        "email": "melany@gmail.com",
        "id_user": 14,
        "login_code": "0",
        "password": "pbkdf2:sha256:260000$NkXdhWjNPupY07Sm$36596080961191de121edbdbcec6658a06f27fd17855e536aa64d241211dd33b",
        "person": {
            "address": "El Tejar - Ibarra",
            "card_id_person": "1001590651",
            "date_born": "02/02/1999",
            "first_name": "Melany",
            "gender": {
                "gender_name": "Female",
                "id_gender": 2
            },
            "id_person": 14,
            "last_name": "Escobar",
            "phone": "0983645875"
        },
        "register_date": "28/03/2023",
        "rol_user": {
            "id_rol": 2,
            "rol_name": "Rol user Employed"
        },
        "user_delete": "True",
        "user_name": "EMP-1001590651",
        "user_state": "False"
    }
}

print((us.get('user')['person'])['card_id_person'])
