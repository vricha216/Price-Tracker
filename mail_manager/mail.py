import smtplib 
def send_mail(**kwargs):
    '''Function called when the email needs to be sent '''

    if kwargs.get('url'):
        try:
            url = kwargs['url']
            to = kwargs['to']
            server = smtplib.SMTP('smtp.gmail.com', 587) 
            server.ehlo()
            server.starttls() 
            server.ehlo()
        
        
            server.login('trackkbud@gmail.com', 'lol090#@nk')
            
            subject = 'Hey! Price fell down' 
            body = 'Check the link ' + url
            
            msg = f"Subject: {subject}\n\n{body}" 
            server.sendmail('trackkbud@gmail.com', to, msg)
            print('Email Sent')
            
            server.quit() 
            return {"status":True,"done":"ok"}

        except Exception as e:
            print(e)
            return {"status":False,"error":e}

    elif kwargs.get('otp'):
        try:

            otp = kwargs['otp']
            to = kwargs['to']
            server = smtplib.SMTP('smtp.gmail.com', 587) 
            server.ehlo()
            server.starttls() 
            server.ehlo()

            server.login('trackkbud@gmail.com', 'lol090#@nk')

            subject = f"Verify Your OTP: {kwargs['otp']}"
            body = f"Thankyou for signup at xyz.com \n \n pls verify email \n \n Your OTP number = {kwargs['otp']} \n \n - xyz.com \n Thank you"
            msg = f"Subject: {subject}\n\n{body}"         
            server.sendmail('trackkbud@gmail.com', to, msg)
            print('OTP Sent')
            server.quit() 
            return {"status":True,"done":"ok"}
        except Exception as e:
            print(e)
            return {"status":False,"error":e}


