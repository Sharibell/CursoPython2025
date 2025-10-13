from flask import Flask
from login import login #importa el blueprint desde login.py


app = Flask(__name__)
app.register_blueprint(login) #registra el blueprint
@app.route('/')
def home():
    return 'Holaa, Unidaaa expertos en Python!'
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0') #Favor poner la ip de su maquina local