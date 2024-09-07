import emoji
import re
# from hazm import Normalizer
from num2words import num2words
from Dictionaries import (arabic_dict,
                          num_dict,
                          sign_dict_fa,
                          english_dict,
                          special_char_dict,
                          month_dict)


class PersianTextPreprocessor:
    def __init__(self):
        # Initialize dictionaries for translation or mapping of characters and symbols
        self.arabic_dict = arabic_dict
        self.num_dict = num_dict
        self.sign_dict_fa = sign_dict_fa
        self.english_dict = english_dict
        self.special_char_dict = special_char_dict
        self.month_dict = month_dict

    def find_emoji(self, df):
        # Identify and handle rows containing emojis within a DataFrame column
        for index, row in df['Comment'].items():
            # Check if any character in the row is an emoji
            if any(char in emoji.EMOJI_DATA for char in row):
                continue

            # Skip processing if the length of the text is less than 3 characters
            if len(row.strip()) < 3:
                continue
        return df

    def to_lower_case(self, text):
        text = text.lower()  # Convert text to lowercase

        return text

    def separate_cases(self, text):
        # Separate joined words that mix numbers and letters or different cases
        if len(text) <= 1:
            return ' '

        new_text = ""
        last_char_all_num = text[0].isalnum()  # Check if the first character is alphanumeric

        for char in text:
            # Separate the text when transitioning between numbers/letters or cases
            if char.isalnum() != last_char_all_num and char.isalnum():
                new_text += " " + char
            else:
                new_text += char

            last_char_all_num = char.isalnum()  # Update the last character type

        return new_text

    def remove_url(self, text):
        # Remove URLs starting with http, https, www, or any domain pattern (e.g., example.com)
        text = re.sub(r'http[s]?://\S+', '', text)  # Remove URLs starting with http or https
        text = re.sub(r'www\.\S+', '', text)  # Remove URLs starting with www
        text = re.sub(r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/[^\s]*)?\b', '',
                      text)  # Remove URLs without protocol (e.g., example.com)
        return text

    def remove_html_tags(self, text):
        # Remove HTML tags using a regular expression
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'<.*?>+', '', text)

        return text

    def remove_encoded_email_strings(self, text):
        # Remove email-like strings with non-standard characters
        text = re.sub(r'[^\x00-\x7F]+<[\w\.\-]+@[\w\.\-]+\.[a-zA-Z]{2,}>', '', text)
        text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)

        return text

    def remove_emails(self, text):
        # Remove standard email addresses
        text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '', text)
        text = re.sub(r'[^\x00-\x7F]+<[\w\.\-]+@[\w\.\-]+\.[a-zA-Z]{2,}>', '', text)
        text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)

        return text

    def remove_elements(self, text):
        # Handle and clean different noise elements like mentions, hashtags, newlines, etc.
        if isinstance(text, float):
            return ''

        text = re.sub(r'@\w+', '', text)  # Remove mentions
        text = re.sub(r'#\w+', '', text)  # Remove hashtags
        text = re.sub(r'@(\w+\.)*\w+', '', text)  # Remove mentions followed by a dot
        text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces
        # Remove IP addresses (e.g., 192.168.0.1)
        text = re.sub(r'\b\d{1,3}(?:\.\d{1,3}){3}\b(?:\:\d+)?', '',
                      text)  # Handle IP addresses with optional port numbers

        # text = text.replace('\n', ' ')  # Replace newline characters with a space
        # text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        text = text.lower()  # Convert all text to lowercase

        return text

    def handle_persian_punctuation(self, text):
        """
        This function ensures proper spacing and formatting of Persian punctuation marks.
        """

        # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text)

        # # Ensure no space before Persian comma, and one space after it
        # text = re.sub(r'\s*،\s*', '، ', text)
        #
        # # Ensure no space before periods, question marks, exclamation marks, and one space after them
        # text = re.sub(r'\s*([؟!.…])\s*', r'\1 ', text)
        #
        # # Ensure no space before other common punctuation marks like colon and semicolon
        # text = re.sub(r'\s*([:؛])\s*', r'\1 ', text)
        #
        # # Remove space before punctuation at the end of the text
        # text = re.sub(r'\s+([،؟!.:؛…])$', r'\1', text)
        #
        # # Handle quotes and parentheses (or other adjusted signs from replacements)
        # text = re.sub(r'\s+»', '»', text)  # Remove space before closing quote/parenthesis
        # text = re.sub(r'«\s+', '«', text)  # Remove space after opening quote/parenthesis
        #
        # # Clean any leftover unwanted spaces or characters, while preserving %
        # text = re.sub(r'\s*\.\.\.\s*', '…', text)  # Ensure ellipsis is formatted properly
        # text = re.sub(r'\s*\-\s*', '—', text)  # Ensure em dashes are formatted properly

        # Strip leading and trailing whitespace
        text = text.strip()

        return text

    def clean_farsi_text_punctuation(self, text):
        """
        Cleans Farsi text by handling whitespace and spacing around punctuation.
        """
        # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text)

        # Remove spaces before punctuation marks, except %
        # text = re.sub(r'\s([؟!.،](?:\s|$))', r'\1', text)

        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
        # text = re.sub(r'\s([?.!,":;](?:\s|$))', r'\1', text)  # Remove spaces before punctuation
        text = re.sub(r'\.(?=\S)', '. ', text)  # Ensure space after a period
        text = re.sub(r'\b\d{1,2} [A-Za-z]+ \d{4}\b', '', text)  # Remove dates (e.g., "1 July 1818")
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
        # text = re.sub(r'\s*,\s*', ', ', text)  # Clean up any commas
        # text = re.sub(r'\s*\.\s*', '. ', text)  # Clean up any periods
        # text = re.sub(r'\s*-\s*', '-', text)  # Clean up any hyphens
        text = re.sub(r'\s+', ' ', text).strip()  # Final cleanup of extra spaces

        return text

    import re

    def remove_english_words(self, persian_text):
        # Regular expression pattern to match English words (only alphabetic characters)
        pattern = r'[a-zA-Z]'

        # Replace matched patterns (English words) with an empty string
        cleaned_text = re.sub(pattern, '', persian_text)

        # Clean up extra spaces that may result from the removal
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

        return cleaned_text

    def remove_cyrillic(self, text):
        cyrillic_pattern = r'[\u0400-\u04FF\u0500-\u052F\u2DE0-\u2DFF\uA640-\uA69F]+'
        cleaned_text = re.sub(cyrillic_pattern, '', text)
        return cleaned_text

    def convert_numbers_to_words_fa(self, text):
        # Convert numbers in the text to their word equivalents in Persian
        def convert(match):
            if match:
                number = int(match.group(0))  # Use group(0) to safely extract the full match
                return num2words(number, lang='fa')
            return match.group(0)  # Return the original text if no conversion is done

        return re.sub(r'\d+', convert, text)  # Replace numbers with their word forms

    def pre_process(self, text):
        # Apply dictionary-based substitutions and other standard preprocessing steps
        text = text.lower()  # Convert all text to lowercase

        dictionaries = [
            self.sign_dict_fa,
                        self.arabic_dict,
                        self.num_dict,
                        self.english_dict,
                        self.special_char_dict,
                        ]

        # Replace text based on the provided dictionaries
        for dictionary in dictionaries:
            for key, value in dictionary.items():
                text = re.sub(re.escape(key), value, text)

        # Additional replacements for specific cases
        text = re.sub(r"\s+", ' ', text)  # Replace multiple spaces with a single space
        text = text.strip()  # Trim leading and trailing spaces

        return text

    def normalize_persian(self, text):
        normalizer = Normalizer()

        # Normalize Farsi text
        return normalizer.normalize(text)

    def remove_half_space(self, text):
        # Define a regex pattern to match the half-space followed by specific suffixes
        pattern = r'(\u200C)(ها|می|تر|ترین)'

        # Replace the half-space with a space if followed by the specified suffixes
        text = re.sub(pattern, r' \2', text)

        # Remove any remaining half-space characters
        text = text.replace('\u200C', '')

        return text

    def remove_numbers_only_cells(self, text):
        # Remove any formatting characters
        stripped_text = re.sub(r'[\s,]+', '', text)
        # Check if the text is purely numeric after removing spaces and commas
        if stripped_text.isdigit():
            return ''  # Return empty string if the text is just numbers
        return text


    def process_column(self, column):
        # Apply all preprocessing steps to a DataFrame column
        column = column.apply(self.to_lower_case)
        column = column.apply(self.remove_elements)  # Clean text elements like mentions, hashtags, etc.
        column = column.apply(self.remove_url)  # Remove URLs
        column = column.apply(self.remove_encoded_email_strings)  # Remove encoded email strings
        column = column.apply(self.remove_html_tags)  # Remove HTML tags
        column = column.apply(self.remove_emails)  # Remove email addresses
        column = column.apply(self.pre_process)  # Apply final preprocessing using dictionaries
        column = column.apply(self.separate_cases)  # Separate mixed-case and alphanumeric sequences
        column = column.apply(self.remove_english_words)
        column = column.apply(self.handle_persian_punctuation)  # Clean punctuation spacing
        column = column.apply(self.clean_farsi_text_punctuation)  # Clean punctuation spacing
        column = column.apply(self.remove_cyrillic)
        column = column.apply(self.remove_numbers_only_cells)  # Remove cells containing only numbers
        # column = column.apply(self.convert_numbers_to_words_fa)  # Convert numbers to words in Persian
        # column = column.apply(self.normalize_persian)  # Normalize Farsi text (if needed)
        # column = column.apply(self.remove_consecutive_duplicates)  # Remove consecutive duplicate characters
        column = column.apply(self.remove_half_space)  # Optionally remove half-spaces

        return column
