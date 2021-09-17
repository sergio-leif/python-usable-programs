import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Sergio Leiva'
email['to'] = '<email.example@account.com>
email['subject'] = 'Hey! I am so glad to send you an email!'

email.set_content(html.substitute({'name': 'Usuario'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('<email.example@account.com>', '<password>')
  smtp.send_message(email)
  print('Everything is done!')