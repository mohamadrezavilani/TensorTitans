import re
from num2words import num2words
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from Dictionaries import (english_dict,
                          contractions_dict,
                          sign_dict_en,
                          special_char_dict

                          )


class EnglishTextPreprocessor:
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        self.english_dict = english_dict
        self.contractions_dict = contractions_dict
        self.sign_dict_en = sign_dict_en
        self.special_char_dict = special_char_dict

    def to_lower_case(self, text):
        text = text.lower()  # Convert text to lowercase
        return text

    # Remove URLs and HTML tags
    def remove_url_and_html(self, text):
        text = re.sub(r'http[s]?://\S+', '', text)  # Remove URLs
        text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)  # Remove URLs with newlines
        text = re.sub('<.*?>+', '', text)  # Remove HTML tags
        return text

    # Remove specific elements like mentions, hashtags, and newlines
    def remove_elements(self, text):
        # Handle and clean different noise elements like mentions, hashtags, newlines, etc.
        if isinstance(text, float):
            return ''

        text = re.sub(r'@(\w+\.)*\w+', '', text)  # Remove mentions followed by a dot
        text = re.sub(r'@\w+', '', text)  # Remove mentions
        text = re.sub(r'#\w+', '', text)  # Remove hashtags
        text = text.replace('\n', ' ')  # Replace newline characters with a space
        text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces
        text = re.sub(r'[^\w\s%]', '', text)  # Remove punctuation except for %

        return text

    # Separate alphanumeric cases (e.g., "abc123" -> "abc 123")
    def separate_cases(self, text):
        if len(text) <= 1:
            return ' '
        new_text = ""
        last_char_all_num = text[0].isalnum()

        for char in text:
            if char.isalnum() != last_char_all_num and char.isalnum():
                new_text += " " + char
            else:
                new_text += char
            last_char_all_num = char.isalnum()
        return new_text

    def clean_english_text_punctuation(self, text):
        """
        Cleans English text by handling whitespace and basic punctuation issues.
        """
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
        text = re.sub(r'\s([?.!,":;](?:\s|$))', r'\1', text)  # Remove spaces before punctuation
        text = re.sub(r'\.(?=\S)', '. ', text)  # Ensure space after a period
        text = re.sub(r'\b\d{1,2} [A-Za-z]+ \d{4}\b', '', text)  # Remove dates (e.g., "1 July 1818")
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
        text = re.sub(r'\s*,\s*', ', ', text)  # Clean up any commas
        text = re.sub(r'\s*\.\s*', '. ', text)  # Clean up any periods
        text = re.sub(r'\s*-\s*', '-', text)  # Clean up any hyphens
        text = re.sub(r'\s+', ' ', text).strip()  # Final cleanup of extra spaces

        return text

    def apply_dictionary_replacements(self, text):
        """Apply dictionary replacements."""
        dictionaries_eng = [self.english_dict,
                            self.contractions_dict,
                            self.sign_dict_en,
                            self.special_char_dict
                            ]
        for dictionary in dictionaries_eng:
            for key, value in dictionary.items():
                text = re.sub(re.escape(key), value, text)
        return text


    def convert_numbers_to_words_en(self, text):
        # Convert numbers to words in English
        number = int(text.group())
        return num2words(number, lang='en')

    def normalize_text(self, text):
        """Convert text to lowercase and tokenize it."""
        tokens = word_tokenize(text)
        return tokens

    def remove_stopwords(self, tokens):
        """Remove stopwords from tokenized text."""
        return [word for word in tokens if word not in self.stopwords]

    def apply_stemming(self, tokens):
        """Apply stemming to tokenized text."""
        return [self.stemmer.stem(word) for word in tokens]

    def clean_extra_spaces(self, text):
        """Remove extra spaces."""
        return re.sub(r"\s+", ' ', text).strip()

    # Full text processing pipeline for a column
    def process_column(self, column):
        column = column.apply(self.to_lower_case)
        column = column.apply(self.remove_url_and_html)  # Remove URLs and HTML tags
        column = column.apply(self.remove_elements)  # Remove unwanted elements like mentions and hashtags
        column = column.apply(self.apply_dictionary_replacements)  # Apply dictionary-based replacements
        column = column.apply(self.separate_cases)  # Separate alphanumeric cases
        column = column.apply(self.clean_english_text_punctuation)  # Clean punctuation issues
        # column = column.apply(self.convert_numbers_to_words_en)  # Convert numbers to words (if needed)
        column = column.apply(self.normalize_text)  # Normalize text (tokenize)
        # column = column.apply(self.remove_stopwords)  # Remove stopwords from tokens
        # column = column.apply(self.apply_stemming)  # Apply stemming (if needed)
        column = column.apply(lambda x: ' '.join(x))  # Join tokens back into a single string
        column = column.apply(self.clean_extra_spaces)  # Clean extra spaces
        return column
