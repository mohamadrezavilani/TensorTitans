import csv
import re

# English sentence endings
sentence_endings = [".", "?", "!"]

# Persian sentence endings
sentence_endings_persian = [".", "؟", "!"]

# Function to split sentences based on punctuation marks
def split_sentences(text, endings):
    # Remove URLs (links)
    text = re.sub(r'http\S+|www\S+', '', text)
    # Replace "..." with "."
    text = text.replace("…", ".")
    text = text.replace("...", ".")    # Create a regex pattern to split on the punctuation marks
    pattern = '|'.join(re.escape(mark) for mark in endings)
    # Split the text, then add back the punctuation to each sentence
    sentences = [sentence.strip() + mark for sentence, mark in re.findall(f'(.+?)([{pattern}])', text)]
    # If no sentence ending is found, return the text as a single sentence
    if not sentences:
        sentences = [text.strip()]
    return sentences


# Open the input CSV file
with open('TLoU1-UI-File-03-5000.csv', 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Skip the header row
    data = list(reader)  # Read the rest of the file

# Process the data and split sentences
processed_data = []
for row in data:
    id_column, english, persian, sth = row  # Unpack the ID, English, and Persian columns
    english_sentences = split_sentences(english, sentence_endings)
    persian_sentences = split_sentences(persian, sentence_endings_persian)
    
    # Determine the max number of sentences between the two languages to align rows correctly
    max_sentences = max(len(english_sentences), len(persian_sentences))
    
    # Extend the shorter list with empty strings to match the length
    english_sentences.extend([''] * (max_sentences - len(english_sentences)))
    persian_sentences.extend([''] * (max_sentences - len(persian_sentences)))
    
    # Add rows to processed_data
    for eng, per in zip(english_sentences, persian_sentences):
        processed_data.append([eng, per])

# Write the processed data to a new CSV file
with open('processed_sentences2.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["English", "Persian"])  # Header row
    writer.writerows(processed_data)

print("CSV file processed and created successfully.")
