from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'yoursendingemail@gmail.com',
    MAIL_PASSWORD = 'yourpassword'
    )
mail = Mail(app)

@app.route('/send-mail/')
def send_mail():
    try:
        msg = Message("Forgot password - PythonProgramming.net",
            sender="yoursendingemail@gmail.com",
            recipients=["recievingemail@email.com"])
        msg.body = "Yo!\nHave you heard the good word of Python???"
        #msg.html = render_template('/mails/reset-password.html', username=username, link = link)
        mail.send(msg)
        return 'Mail sent!'
    except Exception, e:
        return(str(e))
