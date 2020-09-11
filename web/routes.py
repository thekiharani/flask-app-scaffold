from flask import Blueprint
from flask import render_template, url_for, redirect, flash
from app.forms import RegistrationForm, LoginForm, PasswordRequestForm, PasswordResetForm

web = Blueprint('web', __name__, template_folder='templates', static_folder='static')


@web.route("/")
def home():
    return render_template('web/home.html', title='Welcome')


@web.route("/about_us")
def about():
    return render_template('web/about.html', title='About Us')


@web.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # registration logic
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('web/auth/register.html', title='Register', form=form)


@web.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login logic
        if form.email.data == 'thekiharani@gmail.com' and form.password.data == 'Password':
            flash(f'Login Successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Invalid email or password', 'danger')
    return render_template('web/auth/login.html', title='Login', form=form)


@web.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    form = PasswordRequestForm()
    if form.validate_on_submit():
        # request reset logic
        flash(f'A reset link has been sent to your email!', 'success')
        return redirect(url_for('login'))
    return render_template('web/auth/forgot_password.html', title='Forgot Password', form=form)


@web.route("/reset_password", methods=['GET', 'POST'])
def reset_password():
    form = PasswordResetForm()
    if form.validate_on_submit():
        # reset password logic
        flash(f'Password reset successful!', 'success')
        return redirect(url_for('login'))
    return render_template('web/auth/reset_password.html', title='Reset Password', form=form)
