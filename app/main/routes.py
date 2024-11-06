from app.main import bp
import requests
from flask import jsonify, request, render_template, redirect, url_for, current_app
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables

# Use the API_KEY securely from the environment
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.thecatapi.com/v1'

@bp.route('/')
def index():
    # get three cats, and render the template
    cats = redirect(url_for('main.get_cats', amount=3))
    return render_template('index.html', cats=cats)

@bp.route('/get_cats/<int:amount>', methods=['GET'])
def get_cats(amount):
    """Fetches a list of random cats from The Cat API"""
    try:
        headers = {'x-api-key': API_KEY}
        response = requests.get(f'{BASE_URL}/images/search?limit={amount}', headers=headers)
        if response.status_code == 200:
            cats_data = response.json()  # Extract the JSON data from the response
            return cats_data
        else:
            return jsonify({'error': 'Failed to fetch data from The Cat API'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
