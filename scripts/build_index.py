import os
import json
from collections import defaultdict

# Path to cleaned & deduplicated documents
UNIQUE_DIR = 'data/unique_files'
INDEX_DIR = 'index'
INVERTED_INDEX_PATH = os.path.join(INDEX_DIR, 'inverted_index.json')
COMPRESSED_VOCAB_PATH = os.path.join(INDEX_DIR, 'compressed_vocab.txt')

# Ensure the index directory exists
try:
    os.makedirs(INDEX_DIR, exist_ok=True)
except OSError as e:
    print(f"Error creating directory {INDEX_DIR}: {e}")


def front_coding(words):
    words.sort()
    compressed = []
    for i in range(len(words)):
        if i == 0:
            compressed.append(f"0|{words[i]}")
        else:
            prev = words[i - 1]
            curr = words[i]
            prefix_len = 0
            while prefix_len < min(len(prev), len(curr)) and prev[prefix_len] == curr[prefix_len]:
                prefix_len += 1
            suffix = curr[prefix_len:]
            compressed.append(f"{prefix_len}|{suffix}")
    return compressed


def build_inverted_index(input_dir):
    inverted_index = defaultdict(set)

    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            doc_id = filename
            try:
                with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
                    words = set(content.split())  # unique words
                    for word in words:
                        inverted_index[word].add(doc_id)
            except IOError as e:
                print(f"Error reading file {filename}: {e}")

    # Convert sets to lists for JSON serialization
    final_index = {word: list(doc_ids) for word, doc_ids in inverted_index.items()}

    # Save full inverted index
    try:
        with open(INVERTED_INDEX_PATH, 'w', encoding='utf-8') as f:
            json.dump(final_index, f, indent=2)
    except IOError as e:
        print(f"Error writing to {INVERTED_INDEX_PATH}: {e}")

    # Apply front coding to the vocabulary
    vocab = list(final_index.keys())
    compressed_vocab = front_coding(vocab)

    # Save compressed vocabulary
    try:
        with open(COMPRESSED_VOCAB_PATH, 'w', encoding='utf-8') as f:
            for entry in compressed_vocab:
                f.write(entry + '\n')
    except IOError as e:
        print(f"Error writing to {COMPRESSED_VOCAB_PATH}: {e}")

    print(f"✅ Inverted index saved to {INVERTED_INDEX_PATH}")
    print(f"✅ Compressed vocabulary saved to {COMPRESSED_VOCAB_PATH}")


# Run it
if __name__ == '__main__':
    build_inverted_index(UNIQUE_DIR)
