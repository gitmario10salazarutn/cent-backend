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
                        "id_person": user[3],
                        "card_id_person": user[4],
                        "first_name": user[5],
                        "last_name": user[6],
                        "phone": user[7],
                        "address": user[8],
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
                        "id_rol": user[19],
                        "rol_name": user[20]
                    },
                }
            }
        else:
            return None

    @classmethod
    def ListUsers(self, users) -> list:
        return [self.entityUser(user) for user in users]


link = "https://cloud2.utn.edu.ec/ords/f?p=128%3ALOGIN_DESKTOP&fbclid=IwAR3lUpdzdn0b8J31pDg3CtOw8VkRmDdDgNM4VyqdNvhOOLBmiHEccGwGU1I"
