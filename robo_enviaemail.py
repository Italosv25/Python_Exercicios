import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

Email_Origem = "italosvidigal@gmail.com"
senha = "abcd efgh ijkl mnop"
Emails_Destino = ["italosvidigal1@gmail.com", "outro@gmail.com", "mais_um@gmail.com"]


mensagem = MIMEMultipart()
mensagem["from"] = Email_Origem
mensagem["to"] = ", ".join(Emails_Destino)
mensagem["Subject"] = "Robô Enviando E-mail"

corpo = f"""
Teste robô, 

Teste de envio de e-mail pelo python.

Atenciosamente,
Italo Vidigal
"""
mensagem.attach(MIMEText(corpo, "plain"))

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(Email_Origem, senha)
        servidor.sendmail(Email_Origem, Emails_Destino, mensagem.as_string())
        print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")