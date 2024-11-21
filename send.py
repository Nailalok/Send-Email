import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(remetente, senha, destinatario, assunto, mensagem):
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(remetente, senha)
        server.send_message(msg)

remetente = input("Digite seu email: ")
senha = input("Digite sua senha: ")
destinatario = input("Digite o email do destinatário: ")
assunto = input("Digite o assunto do email: ")
mensagem = input("Digite o corpo do email: ")

enviar_email(remetente, senha, destinatario, assunto, mensagem)
