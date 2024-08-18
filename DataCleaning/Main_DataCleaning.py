import os
import pandas as pd
import re
from DataCleaning.DataCleaningFunctions_Persian import PersianTextPreprocessor
from DataCleaning.DataCleaningFunctions_English import EnglishTextPreprocessor
from setup import WordCharacterCount

# Define the directory containing the data files
directory_path = "DataSource"

# List of files in the directory
files = [
    "ELRC_2922-fa.csv",
    "GNOME-fa.csv",
    "NeuLab-TedTalks-fa.csv",
    "infopankki-fa.csv",
    "LinguaTools-WikiTitles-fa.csv",
    "QED-fa.csv",
    "Tanzil-fa.csv",
    "TED2020-fa.csv",
    "TEP-fa.csv",
    "tico-19-fa.csv",
    "tldr-pages-fa.csv",
    "MIZAN-fa.csv",
    "Ubuntu-fa.csv",
    "WikiMatrix-fa.csv",
    "wikimedia-fa.csv",
    "XLEnt-fa.csv",
    "OpenSubtitles-fa.csv",
    "Sentence pairs in Persian-English - 2024-08-15.csv",
]

# Instantiate the text processors
persian_processor = PersianTextPreprocessor()
english_processor = EnglishTextPreprocessor()


def delete_records_with_brackets(df, column_name):
    try:
        # Compile regex pattern to detect content in brackets
        pattern = re.compile(r'\[.*?\]')  # Use raw string to avoid escape issues

        # Filter out rows where the column contains the unwanted patterns
        cleaned_df = df[~df[column_name].str.contains(pattern, na=False)].copy()

        return cleaned_df
    except re.error as e:
        print(f"Regex error: {e}")
        return df  # Return the original dataframe if regex fails


def process_file(file_path):
    try:
        # Load the CSV file
        df = pd.read_csv(file_path)
        print(df.columns)

        # Check for columns containing Persian or English text
        if 'Farsi' in df.columns or 'Persian' in df.columns:
            farsi_column = 'Farsi' if 'Farsi' in df.columns else 'Persian'
            df[f"Cleaned_{farsi_column}"] = persian_processor.process_column(df[farsi_column])

        if 'English' in df.columns:
            df['Cleaned_English'] = english_processor.process_column(df['English'])

        df = delete_records_with_brackets(df, 'Farsi')
        df = delete_records_with_brackets(df, 'English')
        df_filtered = df[df['Cleaned_English'] != df['Cleaned_Farsi']]

        cleaned_file_path = os.path.join(directory_path, f"cleaned_{os.path.basename(file_path)}")
        df_filtered.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned and saved: {cleaned_file_path}")

        return df_filtered

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    word_character_count = WordCharacterCount()
    # Process each file in the directory
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        df_new = process_file(file_path)

        if df_new is None:
            print(f"Skipping file {file_name} due to processing error.")
            continue

        word_character_count.word_count(df_new['Cleaned_Farsi'], f'{file_name}_Farsi')
        word_character_count.word_count(df_new['Cleaned_English'], f'{file_name}_English')

        word_character_count.character_count(df_new['Cleaned_Farsi'], f'{file_name}_Farsi')
        word_character_count.character_count(df_new['Cleaned_English'], f'{file_name}_English')

    print("Data cleaning completed for all files!")


if __name__ == "__main__":
    main()
