from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
load_dotenv()
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ruta2")
def ruta2():
    return "<p>Acceso a la ruta 2</p>"

@app.route("/personas/<persona>")
def personas(persona):
    return "Bienvenido " + persona

@app.route("/plantilla")
def plantilla():
    return render_template("pagina1.html")

@app.route("/envio-correo")
def email():
    destino = request.args.get('correo_destino')
    asunto = request.args.get('asunto')
    mensaje = request.args.get('contenido')
    message = Mail(
        from_email='andresmogollob@gmail.com',
        to_emails=destino,
        subject=asunto,
        html_content=mensaje)
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return 'Correo electrónico enviado'
    except Exception as e:
        print(e.message)
        return 'Error enviando el mensaje'