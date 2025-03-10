# BookMyShow 

This is a clone of the popular online ticketing platform, **BookMyShow**, built with **Flask** (Python) and **SQLite** for the backend. The project allows users to register, login, view movies, events, plays, and sports, as well as book tickets and manage bookings.

## Features

- **User Authentication**:
  - User Registration and Login.
  - Password hashing using `pbkdf2:sha256`.

- **Booking System**:
  - View movies, events, plays, sports, and offers.
  - Book tickets for events, movies, and other activities.
  - View and manage bookings (update or cancel).

- **Responsive Design**:
  - Mobile and desktop friendly design using CSS for styling.
  - Dynamic content rendering using Flask templates.

## Project Structure

/bookmyshow /static /css - styles.css # Main styling file /js - script.js # Main JavaScript file /templates - index.html # Homepage - movies.html # Movies page - events.html # Events page - sports.html # Sports page - plays.html # Plays page - offers.html # Offers page - register.html # User registration page - login.html # User login page - book.html # Booking form - view_bookings.html # View and manage bookings page - update_booking.html # Update booking page app.py # Flask app file

