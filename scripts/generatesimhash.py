import os
from simhash import Simhash

# Directory containing cleaned files
cleaned_dir = 'data/cleaned'
unique_dir = 'data/unique_files'
try:
    os.makedirs(unique_dir, exist_ok=True)
except OSError as e:
    print(f"Error creating directory {unique_dir}: {e}")

simhashes = []

def get_features(text):
    return text.split()

for filename in os.listdir(cleaned_dir):
    if filename.endswith('.txt'):
        path = os.path.join(cleaned_dir, filename)

        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                current_hash = Simhash(get_features(content))

                is_duplicate = False
                for existing_hash in simhashes:
                    distance = current_hash.distance(existing_hash)
                    if distance < 5:  # threshold: tune for strictness
                        is_duplicate = True
                        break

                if not is_duplicate:
                    simhashes.append(current_hash)
                    print(f" Unique: {filename}")
                    # Copy to unique folder
                    with open(os.path.join(unique_dir, filename), 'w', encoding='utf-8') as out:
                        out.write(content)
                else:
                    print(f" Duplicate: {filename}")
        except IOError as e:
            print(f"Error processing file {filename}: {e}")
