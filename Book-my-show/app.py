from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.secret_key = 'your_secret_key'
db = SQLAlchemy(app)

# Database model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Database model for Bookings
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='bookings')

# Initialize the database
with app.app_context():
    db.create_all()

# Home Page
@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

# User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful!", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home'))

        flash("Login Failed. Check your username and/or password.", "danger")

    return render_template('login.html')

# User Logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# Create Booking
@app.route('/book', methods=['GET', 'POST'])
def book():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        movie_name = request.form['movie_name']
        date = request.form['date']
        user_id = session['user_id']

        new_booking = Booking(movie_name=movie_name, date=date, user_id=user_id)
        db.session.add(new_booking)
        db.session.commit()

        flash("Booking Created!", "success")
        return redirect(url_for('view_bookings'))

    return render_template('book.html')

# View Bookings
@app.route('/view_bookings')
def view_bookings():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_bookings = Booking.query.filter_by(user_id=session['user_id']).all()
    return render_template('view_bookings.html', bookings=user_bookings)

# Update Booking
@app.route('/update_booking/<int:booking_id>', methods=['GET', 'POST'])
def update_booking(booking_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != session['user_id']:
        return redirect(url_for('view_bookings'))

    if request.method == 'POST':
        booking.movie_name = request.form['movie_name']
        booking.date = request.form['date']
        db.session.commit()

        flash("Booking Updated!", "success")
        return redirect(url_for('view_bookings'))

    return render_template('update_booking.html', booking=booking)

# Delete Booking
@app.route('/delete_booking/<int:booking_id>')
def delete_booking(booking_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != session['user_id']:
        return redirect(url_for('view_bookings'))

    db.session.delete(booking)
    db.session.commit()

    flash("Booking Canceled!", "success")
    return redirect(url_for('view_bookings'))

# Running the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
