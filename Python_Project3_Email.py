import smtplib

sender_email = '---@gmail.com'  #input the actual sender email here
password = '*****'  # input the actual password here
receiver_email = '----@gmail.com' #input the actual receiver email here
port = 587  

message = """\
Subject: Hello,

This email is being sent from Python.

Regards,
KN """

try:
    server = smtplib.SMTP('smtp.gmail.com', port)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    print('Access granted. Login successful')

    server.sendmail(sender_email, receiver_email, message)
    print('Email has been successfully sent to:', receiver_email)

except Exception as e:
    print('An error occurred:', str(e))

finally:
    server.quit()
    print('Server has been closed')

