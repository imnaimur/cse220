import smtplib

def verify_email(email_address):
    try:
        server = smtplib.SMTP('smtp.example.com')
        server.helo()
        server.mail('example@example.com')
        code, message = server.rcpt(email_address)
        server.quit()
        if code == 250:
            print(f'{email_address} is valid.')
        else:
            print(f'{email_address} is not valid.')
    except:
        print(f'{email_address} is not valid.')

email_list = ['valid@example.com', 'invalid@example.com', 'test@example.com']

for email in email_list:
    verify_email(email)
