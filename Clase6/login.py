from flask import Blueprint, request, jsonify

login= Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def login_user():
    print ("Headers: ", request.headers)