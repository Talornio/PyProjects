from flask import *
# -*- coding: utf-8 -*-

app = Flask(__name__, template_folder='C:/Users/Utente/Desktop/Projects/PyProjects/FlaskWebServer/resources')
app.config["DEBUG"] = True

regolamento = "C:/Users/Utente/Desktop/Projects/PyProjects/FlaskWebServer/resources/index.html"

def read_file(filename, charset='utf-8'):
    with open(filename, 'r') as f:
        return f.read() #.decode(charset)


@app.route('/regolamento', methods=['GET'])
def home():
    return 'ciao sono Mattia'

if __name__ == "__main__":
    app.run()       