from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5c2076a50b18f9c38141dd43a14a570d'

@app.route("/", methods=['GET', 'POST'])
def home():
    form = LoginForm()
    return render_template('index.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Fill This Out', form=form)

if __name__ == '__main__':
    app.run(debug=True)
