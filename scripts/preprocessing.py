import nltk
nltk.download('punkt')       # for word_tokenize
nltk.download('stopwords')   # for stopwords

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re
import os

# Read the Text File
def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

# Remove UI elements and boilerplate text
def remove_boilerplate(text):
    patterns = [
        r'Jump to content', r'Main menu', r'Navigation', r'Create account', r'Log in',
        r'Edit links', r'View history', r'Tools', r'Search', r'Appearance',
        r'Download as PDF', r'Languages?\n.*', r'Print/export', r'ArticleTalk',
        r'\d+ languages', r'Contents\n.*?(?=\d+ )',  # table of contents block
        r'^\s*$',  # empty lines
        r'\[edit\]', r'\(edit\)', r'\[citation needed\]'
    ]
    for pat in patterns:
        text = re.sub(pat, '', text, flags=re.IGNORECASE | re.MULTILINE)
    return text

# Normalize Text (Lowercase + Remove Punctuation)
def normalize_text(text):
    text = text.lower()  # Lowercase everything
    text = re.sub(r'[^a-z\s]', '', text)  # Keep only letters and spaces
    return text

# Tokenize into Words and filter stopwords
def tokenize_and_filter(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

# Save output
def save_cleaned_file(tokens, output_path):
    try:
        with open(output_path, 'w') as f:
            f.write(' '.join(tokens))
    except IOError as e:
        print(f"Error writing to file {output_path}: {e}")

# Full preprocessing pipeline
def preprocess_text_file(input_path, output_path):
    raw_text = read_text_file(input_path)
    clean_text = remove_boilerplate(raw_text)
    normalized = normalize_text(clean_text)
    tokens = tokenize_and_filter(normalized)
    save_cleaned_file(tokens, output_path)

input_dir = 'data/'       # Your raw text files
output_dir = 'data/cleaned/'   # Preprocessed outputs

try:
    os.makedirs(output_dir, exist_ok=True)
except OSError as e:
    print(f"Error creating directory {output_dir}: {e}")

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace('.txt', '_clean.txt'))
        preprocess_text_file(input_path, output_path)
