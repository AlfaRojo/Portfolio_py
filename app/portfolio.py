from flask import (
    Blueprint, render_template, request, current_app
)
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')

@bp.route('/achievements', methods=['GET'])
def main():
    return render_template('achievements/main.html')

@bp.route('/mail', methods=['GET', 'POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    if request.method == 'POST':
        send_email(name, email, message)
        return render_template('portfolio/sent_mail.html')
    
    return render_template('portfolio/sent_mail.html')

def send_email(name, email, content):
    html_content = F"""
        <p>Kevin! Te hablaron desde tu página web!</p>
        <p>Nombre: {name}</p>
        <p>Email: {email}</p>
        <p>Mensaje: {content}</p>
    """
    try:
        sg = SendGridAPIClient('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')
        message = Mail(from_email="kevin.tec.mat@hotmail.com", to_emails="kevin.tec.mat@gmail.com", subject="URGENTE!!", html_content=html_content)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)