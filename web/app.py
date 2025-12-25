from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Add scripts directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from search import search

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # ✅ Enable CORS

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/search', methods=['POST'])
def search_endpoint():
    logging.debug('Search endpoint called')
    data = request.get_json()
    query = data.get('query', '')
    logging.debug(f'Received query: {query}')
    results = search(query)
    logging.debug(f'Search results: {results}')
    return jsonify(results=[doc for doc in results])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # ✅ Render port
    app.run(host='0.0.0.0', port=port)
