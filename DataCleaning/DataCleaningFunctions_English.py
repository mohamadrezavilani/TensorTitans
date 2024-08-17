import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from Dictionaries import english_dict, sign_dict, num_dict


class EnglishTextPreprocessor:
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        self.sign_dict = sign_dict
        self.num_dict = num_dict
        self.english_dict = english_dict

    def remove_url(self, text):
        text = re.sub(r'http[s]?://\S+', '', text)
        return text

    def remove_elements(self, text):
        if isinstance(text, float):
            return ''
        text = re.sub(r'@(\w+\.)*\w+', '', text)
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'#\w+', '', text)
        text = text.replace('\n', ' ')
        text = re.sub('\s+', ' ', text)
        text = text.lower()
        return text.strip()

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

    def remove_consecutive_duplicates(self, text):
        pattern = r'(\w)\1{1,}'
        return re.sub(pattern, r'\1\1', text)

    def normalize_and_stem(self, text):
        text = text.lower()
        text = word_tokenize(text)
        text = [self.stemmer.stem(word) for word in text if word not in self.stopwords]
        text = ' '.join(text)

        dictionaries = [self.sign_dict, self.num_dict, self.english_dict]

        for dictionary in dictionaries:
            for key, value in dictionary.items():
                text = re.sub(re.escape(key), value, text)

        text = re.sub("\s+", ' ', text)
        return text.strip()

    def process_column(self, column):
        column = column.apply(self.remove_elements)
        column = column.apply(self.remove_url)
        column = column.apply(self.separate_cases)
        column = column.apply(self.remove_consecutive_duplicates)
        column = column.apply(self.normalize_and_stem)
        return column
