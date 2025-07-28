from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import requests
import os

frontend = Blueprint('frontend', __name__)

API_URL = os.environ.get('API_URL', 'http://localhost:5000')

@frontend.route('/')
def home():
    if 'access_token' in session:
        return redirect(url_for('frontend.dashboard'))
    return redirect(url_for('frontend.login'))

@frontend.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        resp = requests.post(f'{API_URL}/api/login', json={'username': username, 'password': password})
        if resp.status_code == 200:
            session['access_token'] = resp.json()['access_token']
            return redirect(url_for('frontend.dashboard'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    return render_template('login.html')

@frontend.route('/dashboard')
def dashboard():
    token = session.get('access_token')
    if not token:
        return redirect(url_for('frontend.login'))
    headers = {'Authorization': f'Bearer {token}'}
    bikes = []
    try:
        resp = requests.get(f'{API_URL}/api/bikes', headers=headers)
        if resp.status_code == 200:
            bikes = resp.json()
    except Exception:
        flash('Could not fetch bikes.', 'warning')
    return render_template('dashboard.html', bikes=bikes)

@frontend.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('frontend.login'))
