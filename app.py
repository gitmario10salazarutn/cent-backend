# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:56:16 2023

@author: Mario
"""

from flask import Flask, jsonify, render_template, request
from flask_login import login_required, login_user, LoginManager, logout_user
from flask_cors import CORS
from models import models as model
import jwt
import json

app = Flask(__name__)
CORS(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(id):
    print(id)
    user = model.Model.get_userbyusername(
        username=id) or model.Model.get_userbyemail(email=id)
    return user


def Page_Not_Found(error):
    return '<h1>Page Not Found</h1>', 404


@app.route('/users/delete_user/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        data = request.json
        row_affect = model.Model.delete_user(id=id, data=data)
        if row_affect == 1:
            return jsonify({
                'message': 'Delete user Successfully!',
                'token': row_affect
            })
        elif row_affect == -1:
            return jsonify({
                'message': 'Confirm password failed!',
                'token': row_affect
            })
        else:
            return jsonify({
                'message': 'Delete user failed!',
                'token': row_affect
            })
    except Exception as ex:
        return jsonify({"message": "Error {0}".format(ex)})


@app.route('/users/delete_language/<id>', methods=['DELETE'])
def delete_language(id):
    try:
        row_affect = model.Model.delete_language(id=id)
        if row_affect == 1:
            return jsonify({
                'message': 'Delete language Successfully!',
                'token': row_affect
            })
        else:
            return jsonify({
                'message': 'Delete language failed!',
                'token': row_affect
            })
    except Exception as ex:
        return jsonify({"message": "Error {0}".format(ex)})


@app.route('/users/setenable_user/<id>', methods=['POST'])
def setenable_user(id):
    try:
        row_affect = model.Model.setenable_user(id=id)
        if row_affect == 1:
            return jsonify({
                'message': 'Change user state Successfully!',
                'token': row_affect
            })
        else:
            return jsonify({
                'message': 'Change user state failed!',
                'token': row_affect
            })
    except Exception as ex:
        return jsonify({"message": "Error {0}".format(ex)})


@app.route('/users/get_users', methods=['GET'])
def get_users():
    try:
        users = model.Model.get_users()
        if users is None:
            return [None]
        else:
            return users
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/get_languages', methods=['GET'])
def get_languages():
    try:
        languages = model.Model.get_languages()
        if languages is None:
            return [None]
        else:
            return languages
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/get_languagebyuser/<username>', methods=['GET'])
def get_languagebyuser(username):
    try:
        language = model.Model.get_languagesbyuser(username=username)
        if language:
            return jsonify({
                'message': 'Languages found Successfully!',
                'token': language
            })
        else:
            return jsonify({
                'message': 'Language not found!',
                'token': None
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/get_educationbyid/<id>', methods=['GET'])
def get_educationbyid(id):
    try:
        eduaction = model.Model.get_educationbyid(id=id)
        if eduaction:
            return jsonify({
                'message': 'Education found Successfully!',
                'token': eduaction
            })
        else:
            return jsonify({
                'message': 'Language not found!',
                'token': None
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/get_educationbyuser/<id>', methods=['GET'])
def get_educationbyuser(id):
    try:
        eduaction = model.Model.get_educationbyuser(username=id)
        if eduaction:
            return jsonify({
                'message': 'Education found Successfully!!',
                'token': eduaction
            })
        else:
            return jsonify({
                'message': 'Language not found!',
                'token': None
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/create_educationl', methods=['POST'])
def create_education():
    try:
        data = request.json
        education = model.Model.create_education(data)
        print(education)
        if education is None:
            return jsonify({'message': 'Insert education failed!', 'token': None}), 404
        else:
            return jsonify({
                'message': 'Education created successfully!',
                'token': education
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/update_education/<id>', methods=['PUT'])
def update_education(id):
    try:
        data = request.json
        education = model.Model.update_education(id=id, data=data)
        if education is None:
            return jsonify({'message': 'Education not found!', 'token': None}), 404
        elif education == 0:
            return jsonify({'message': 'Update education failed!', 'token': None})
        else:
            return jsonify({
                'message': 'Education Update successfully!',
                'token': education
            })
    except Exception as ex:
        return jsonify({'error': 'Error {0}'.format(ex),
                        'message': 'Error!'}), 500


@app.route('/users/delete_education/<id>', methods=['DELETE'])
def delete_education(id):
    try:
        row_affect = model.Model.delete_education(id=id)
        if row_affect == 1:
            return jsonify({
                'message': 'Delete education Successfully!',
                'token': row_affect
            })
        else:
            return jsonify({
                'message': 'Delete education failed!',
                'token': row_affect
            })
    except Exception as ex:
        return jsonify({"message": "Error {0}".format(ex)})


@app.route('/users/get_genders', methods=['GET'])
def get_genders():
    try:
        genders = model.Model.get_genders()
        if genders is None:
            return [None]
        else:
            return genders
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/get_languagebyid/<id>', methods=['GET'])
def get_languagebyid(id):
    try:
        language = model.Model.get_languagebyid(id=id)
        if language:
            return jsonify({
                'message': 'Language found Successfully!',
                'token': language
            })
        else:
            return jsonify({
                'message': 'Language not found!',
                'token': None
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/create_language', methods=['POST'])
def create_language():
    try:
        data = request.json
        language = model.Model.create_language(data)
        print(language)
        if language is None:
            return jsonify({'message': 'Insert language failed!', 'token': None}), 404
        elif language == -1:
            return jsonify({
                'message': 'Language exist on database!',
                'token': None
            })
        else:
            return jsonify({
                'message': 'Language created successfully!',
                'token': language
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/update_languagelearn/<id>', methods=['POST'])
def update_languagelearn(id):
    try:
        data = request.json
        language = model.Model.update_languagelearn(id=id, data=data)
        if language is None:
            return jsonify({'message': 'Language not found!', 'token': None}), 404
        elif language == 0:
            return jsonify({'message': 'Update language failed!', 'token': None})
        else:
            return jsonify({
                'message': 'Language Update successfully!',
                'token': language
            })
    except Exception as ex:
        return jsonify({'error': 'Error {0}'.format(ex),
                        'message': 'Card id or email exist on database!'}), 500


@app.route('/users/get_knowledgelevels', methods=['GET'])
def get_knowledgelevels():
    try:
        kl = model.Model.get_knowledgwlevels()
        if kl is None:
            return [None]
        else:
            return kl
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/get_LanguagesProgramming', methods=['GET'])
def get_LanguagesProgramming():
    try:
        kl = model.Model.get_LanguagesProgramming()
        if kl is None:
            return [None]
        else:
            return kl
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/get_rols', methods=['GET'])
def get_rols():
    try:
        rols = model.Model.get_rols()
        if rols is None:
            return [None]
        else:
            return rols
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/get_userbyusername/<username>', methods=['GET'])
def get_userbyusername(username):
    try:
        user = model.Model.get_userbyusername(username=username)
        if user:
            return jsonify({
                'message': 'User found Successfully!',
                'token': user
            })
        else:
            return jsonify({
                'message': 'User not found!',
                'token': None
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/get_userbyemail/<email>', methods=['GET'])
@login_required
def get_userbyemail(email):
    try:
        user = model.Model.get_userbyemail(email=email)
        if user:
            return jsonify({
                'message': 'User found Successfully!',
                'token': user
            })
        else:
            return jsonify({
                'message': 'User not found!',
                'token': None
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/login_user', methods=['GET', 'POST'])
def login_user():
    try:
        data = request.json
        user = model.Model.login_user(data=data)
        if user == 2 or user == -1:
            return jsonify({
                'message': 'Username or password are incorrect!',
                'token': None
            })
        elif user == 1:
            return jsonify({
                'message': 'User Inactive!',
                'token': None
            })
        else:
            a = load_user(data['id_user'])
            encode_jwt = jwt.encode(user, "mario10salazar", algorithm="HS256")
            return jsonify({
                'message': 'Login Successfully!',
                'token': json.dumps(encode_jwt)
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/change_password/<id>', methods=['PUT'])
def change_password(id):
    try:
        data = request.json
        row = model.Model.change_password(id=id, data=data)
        if row == 1:
            return jsonify({'message': 'Change password',
                            'token': 1})
        elif row == 3:
            return jsonify({'message': 'Password incorrect!',
                            'token': None})
        elif row == 2:
            return jsonify({'message': 'Confirm password incorrect!',
                            'token': None})
        elif row == 4:
            return jsonify({'message': 'Enter a key different at the old password!',
                            'token': None})
        else:
            return jsonify({'message': 'User not found!',
                            'token': None})
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

# ? Warning it is a warning or info...
# ! Danger, it is a danger...
# TODO What is it?


@app.route('/users/create_user', methods=['POST'])
def create_user():
    try:
        data = request.json
        usuario = model.Model.create_user(data)
        if usuario is None:
            return jsonify({'message': 'Data not found!', 'token': None}), 404
        elif usuario == -1:
            return jsonify({
                'message': 'User exist on database!',
                'token': None
            })
        else:
            return jsonify({
                'message': 'User created successfully!',
                'token': usuario
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@app.route('/users/update_user/<id>', methods=['POST'])
def update_user(id):
    try:
        data = request.json
        user = model.Model.update_user(data=data, id_user=id)
        print(user)
        if user is None:
            return jsonify({'message': 'Data not found!', 'token': None}), 404
        elif user == -1:
            return jsonify({'message': 'User not found!', 'token': None})
        elif user == -2:
            return jsonify({'message': 'User with email exist on database!', 'token': None})
        else:
            return jsonify({
                'message': 'User created successfully!',
                'token': user
            })
    except Exception as ex:
        return jsonify({'error': 'Error {0}'.format(ex),
                        'message': 'Card id or email exist on database!'}), 500


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.register_error_handler(404, Page_Not_Found)
    app.run(debug=True, host="0.0.0.0")

    """
    Buenos días
El martes fui para ver si podía ayudarme a matricularme en octavo nivel, ya que no me permite tomar materias y quería saber si ya puedo elegir, de ser así para que por favor me ayude para poder imprimir el formulario e ir a cancelar una materia de segunda matricula que tengo o necesariamente tengo que presentarme en la universidad para realizar el trámite.
Por su ayuda, muchas gracias
Att: Mario Salazar


    """
