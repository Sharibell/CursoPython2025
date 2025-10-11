from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def login_user():
    user =  request.json.get('user')
    password = request.json.get('password')
    print("Headers:", request.headers)
    print(f"Usuario: {user}, Password: {password}")
    
    codRes,menRes,accion = inicializarVariables (user, password) #LLAMA A LA FUNCION CON PARAMETROS

    salida = {
        "codRes": codRes,  
        "menRes":menRes,
        "user": user,
        "accion":accion
    }
    return jsonify(salida)
def inicializarVariables(user, password):
    userlocal = "shari"
    passlocal = "unida123"
    codRes= "SIN_ERROR"
    menRes= "OKI"
    try:
        print("verificar login")
        if user == userlocal and password == passlocal:
            print("Login exitoso")
            accion = "Succes"
        else:
            print("Usuario o Contraseña incorrectas")
            codRes= "ERROR"
            menRes= "Usuario o Contraseña incorrectas"
            print("Login fallido")
            accion = "No_Succes"
    except Exception as e:
        print("Error", str(e))
        codRes= "ERROR"
        menRes= 'Msg:' +str(e)
        accion = "Error Interno"
    return codRes, menRes, accion