import json
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')

INDEX_PATH = 'index/inverted_index.json'
UNIQUE_DIR = 'unique_files'

# Load inverted index
try:
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        inverted_index = json.load(f)
except IOError as e:
    print(f"Error loading index from {INDEX_PATH}: {e}")
    inverted_index = {}

stop_words = set(stopwords.words('english'))

def preprocess_query(query):
    # Tokenize the query and remove non-alphabetic characters and stopwords
    tokens = word_tokenize(query.lower())
    return [w for w in tokens if w.isalpha() and w not in stop_words]

def search(query):
    # Preprocess the query to extract relevant terms
    terms = preprocess_query(query)
    result_set = set()

    # Iterate over each term in the query
    for term in terms:
        # Check if the term exists in the inverted index
        if term in inverted_index:
            # If this is the first term, initialize the result set
            if not result_set:
                result_set = set(inverted_index[term])
            # Otherwise, intersect the result set with the current term's documents
            else:
                result_set = result_set.intersection(set(inverted_index[term]))

    # Return the results
    return sorted(result_set) if result_set else []

# CLI usage
if __name__ == '__main__':
    while True:
        q = input("🔍 Enter search query (or 'exit'): ")
        if q.lower() == 'exit':
            break
        results = search(q)
        if results:
            print("✅ Matching documents:")
            for doc in results:
                print(f"• {doc}")
        else:
            print("❌ No matching documents found.")
