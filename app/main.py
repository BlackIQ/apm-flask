from flask import Flask, redirect, render_template, request, flash, session
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
import csv
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345678'
app.config['UPLOAD_FOLDER'] = './app/uploads'


class GetUser(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    password = PasswordField('id', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'status' in session:
        if request.method == 'POST':
            try:
                upload_file = request.files['file']
                filename = secure_filename(upload_file.filename)
                format = filename.split('.')
                upload_file.save(os.path.join(app.config['UPLOAD_FOLDER'], f'last.{format[1]}'))
                return render_template('upload-ok.html', file=filename)
            except Exception as e:
                return render_template('upload-error.html', error=str(e))
        else:
            with open('app/uploads/last.csv', newline='') as csvfile:
                rows = csv.DictReader(csvfile)
                irows = []
                for row in rows:
                    irows.append(row)
            return render_template('index.html', data=irows)
    else:
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'status' not in session:
        get_user = GetUser(request.form)
        if request.method == 'POST':
            try:
                if get_user.validate():
                    id = get_user.id.data
                    password = get_user.password.data
                    if id == 'x' and password == 'y':
                        session['status'] = True
                        return redirect('/')
                    else:
                        flash('رمز عبور یا آیدی پیدا نشد')
            except:
                return 'bye'
        return render_template('login.html', form=get_user)
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    if 'status' in session:
        session.pop('status', default=None)
        return redirect('/login')
    else:
        return redirect('/login')
