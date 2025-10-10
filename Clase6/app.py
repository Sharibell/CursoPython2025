from flask import Flask
from login import login #importamos el blueprint desde login.py

app = Flask(__name__)
app.register_blueprint(login) #registramos el blueprint
@app.route('/')
def hom():
    return "Hola UNIDA, expertos en Python"
if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
    