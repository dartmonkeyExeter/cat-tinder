from app.main import bp
import requests
from flask import jsonify, request, render_template, redirect, url_for, current_app
from dotenv import load_dotenv
from app.models.cats import Cat
from app.models.favourite import Favourite
import os
from app.extensions import db

load_dotenv()  # Load environment variables

# Use the API_KEY securely from the environment
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.thecatapi.com/v1'

@bp.route('/')
def index():
    # get cat, and render the template
    cat = get_cats(1)
    print(cat)
    return render_template('index.html', cat=cat, key=API_KEY)

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

@bp.route('/vote', methods=['POST'])
def vote():
    amount = int(request.form.get('amount'))
    cat_id = request.form.get('cat_id')
    vote_type = 'up' if amount == 1 else 'down'
    
    # Try to get the cat or create it if it doesn't exist
    cat = Cat.query.get(cat_id)
    if not cat:
        # Create and add cat if it does not exist
        cat = Cat(id=cat_id, upvotes=0, downvotes=0)
        db.session.add(cat)
        db.session.commit()  # Commit the new cat to persist in the database

    # Update votes based on vote_type
    if vote_type == 'up':
        cat.upvotes += 1
    else:
        cat.downvotes += 1

    db.session.commit()  # Commit after modifying votes
    return jsonify({"status": "success", "cat_id": cat_id, "upvotes": cat.upvotes, "downvotes": cat.downvotes})

