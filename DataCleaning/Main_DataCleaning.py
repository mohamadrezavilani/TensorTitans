import os
import pandas as pd
import re
from DataCleaning.DataCleaningFunctions_Persian import PersianTextPreprocessor
from DataCleaning.DataCleaningFunctions_English import EnglishTextPreprocessor
from setup import WordCharacterCount

# Define the directory containing the data files
directory_path = "DataLoading/DataSource"

# List of files in the directory
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

        # Apply the custom cleaning function
        df = delete_records_with_brackets(df, farsi_column)
        df = delete_records_with_brackets(df, 'English')

        # Drop rows with any blank cells after processing
        df = df.dropna(how='any', ignore_index=True)

        # Remove rows where any cell contains only spaces or is an empty string
        df = df[~df.apply(lambda x: x.str.strip().eq('').any(), axis=1)]
        df = df[~df.apply(lambda x: x.str.strip().eq(' ').any(), axis=1)]

        # Filter rows where cleaned columns differ
        df_filtered = df[df['Cleaned_English'] != df[f'Cleaned_{farsi_column}']]

        # Select relevant columns
        df_final = df_filtered[['Cleaned_English', f'Cleaned_{farsi_column}', 'Source']]
        df_final.columns = ['English', 'Persian', 'Source']

        # Save the cleaned dataframe
        cleaned_file_path = os.path.join(directory_path, f"cleaned_{os.path.basename(file_path)}")
        df_final.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned and saved: {cleaned_file_path}")

        return df_final

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

        word_character_count.word_count(df_new['Persian'], f'{file_name}_Farsi')
        word_character_count.word_count(df_new['English'], f'{file_name}_English')

        word_character_count.character_count(df_new['Persian'], f'{file_name}_Farsi')
        word_character_count.character_count(df_new['English'], f'{file_name}_English')

    print("Data cleaning completed for all files!")


if __name__ == "__main__":
    main()
