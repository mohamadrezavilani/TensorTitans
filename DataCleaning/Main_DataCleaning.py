import os
import pandas as pd
import re
from DataCleaning.DataCleaningFunctions_Persian import PersianTextPreprocessor
from DataCleaning.DataCleaningFunctions_English import EnglishTextPreprocessor
from setup import WordCharacterCount

# Define the directory containing the data files
directory_path = "DataLoading/DataSource"

# List of files in the directory to be processed
files = [
    "ELRC_2922-fa.csv",
    "Ubuntu-fa.csv",
    "tldr-pages-fa.csv",
    "tico-19-fa.csv",
    "GNOME-fa.csv",
    "infopankki-fa.csv",
    "QED-fa.csv",
    "NeuLab-TedTalks-fa.csv",
    "Sentence pairs in Persian-English - 2024-08-15.csv",
    "TEP-fa.csv",
    "TED2020-fa.csv",
    "WikiMatrix-fa.csv",
    "wikimedia-fa.csv",
    "XLEnt-fa.csv",
    "LinguaTools-WikiTitles-fa.csv",
    "MIZAN-fa.csv",
    "Tanzil-fa.csv",
    "OpenSubtitles-fa.csv",
]

# Instantiate text processors for Persian and English
persian_processor = PersianTextPreprocessor()
english_processor = EnglishTextPreprocessor()


# Function to delete records containing content within brackets in a specific column
def delete_records_with_brackets(df, column_name):
    try:
        # Compile regex pattern to detect content within brackets
        pattern = re.compile(r'\[.*?\]')  # Use raw string to avoid escape issues

        # Filter out rows where the column contains the unwanted patterns
        cleaned_df = df[~df[column_name].str.contains(pattern, na=False)].copy()

        return cleaned_df
    except re.error as e:
        # Print regex error and return the original DataFrame if an error occurs
        print(f"Regex error: {e}")
        return df


# Function to process a single file
def process_file(file_path):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Check for columns containing Persian (Farsi) or English text
        if 'Farsi' in df.columns or 'Persian' in df.columns:
            # Determine the correct column name for Persian text
            farsi_column = 'Farsi' if 'Farsi' in df.columns else 'Persian'
            # Clean the Persian text column using the Persian text processor
            df[f"Cleaned_{farsi_column}"] = persian_processor.process_column(df[farsi_column])

        # Clean the English text column if it exists
        if 'English' in df.columns:
            df['Cleaned_English'] = english_processor.process_column(df['English'])

        # Apply the custom cleaning function to remove records with bracketed content
        df = delete_records_with_brackets(df, farsi_column)
        df = delete_records_with_brackets(df, 'English')

        # Drop rows with any blank cells after processing
        df = df.dropna(how='any', ignore_index=True)

        # Remove rows where any cell contains only spaces or is an empty string
        df = df[~df.apply(lambda x: x.str.strip().eq('').any(), axis=1)]
        df = df[~df.apply(lambda x: x.str.strip().eq(' ').any(), axis=1)]

        # Filter rows where cleaned columns differ (i.e., English and Persian translations do not match)
        df_filtered = df[df['Cleaned_English'] != df[f'Cleaned_{farsi_column}']]

        # Select relevant columns for the final DataFrame
        df_final = df_filtered[['Cleaned_English', f'Cleaned_{farsi_column}', 'Source']]
        df_final.columns = ['English', 'Persian', 'Source']  # Rename columns

        # Save the cleaned DataFrame to a new CSV file
        cleaned_file_path = os.path.join(directory_path, f"cleaned_{os.path.basename(file_path)}")
        df_final.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned and saved: {cleaned_file_path}")

        return df_final

    except Exception as e:
        # Print any errors that occur during processing
        print(f"Error processing {file_path}: {e}")


# Main function to process all files
def main():
    # Process each file in the directory
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        df_new = process_file(file_path)

        # Skip file if processing returned None
        if df_new is None:
            print(f"Skipping file {file_name} due to processing error.")
            continue

        # # Instantiate the WordCharacterCount object
        # word_character_count = WordCharacterCount()
        #
        # # Perform word and character count for Persian and English columns
        # word_character_count.word_count(df_new['Persian'], f'{file_name}_Farsi')
        # word_character_count.word_count(df_new['English'], f'{file_name}_English')
        #
        # word_character_count.character_count(df_new['Persian'], f'{file_name}_Farsi')
        # word_character_count.character_count(df_new['English'], f'{file_name}_English')

    print("Data cleaning completed for all files!")


# Execute the main function when the script is run
if __name__ == "__main__":
    main()
