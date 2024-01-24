import smtplib
import os
from email.message import EmailMessage

ruta_env = '.env'

# Lee las variables de entorno desde el archivo .env
with open(ruta_env, 'r') as archivo:
    for linea in archivo:
        # Ignora líneas que comienzan con '#' (comentarios) o están en blanco
        if not linea.strip().startswith('#') and '=' in linea:
            nombre, valor = linea.strip().split('=', 1)
            os.environ[nombre] = valor

emailText = os.getenv('email')
password = os.getenv('password')


email = EmailMessage()
email['From'] = 'correosmijel@gmail.com'
# xiomaraarias257@gmail.com
email['To'] = 'xiomaraarias257@gmail.com'
email['Subject'] = 'Mensaje de amor'
email.set_content('Te amo con todo mi corazón.')


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(emailText, password)
server.send_message(email)
server.quit()
