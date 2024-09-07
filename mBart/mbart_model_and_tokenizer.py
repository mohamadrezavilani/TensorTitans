# -*- coding: utf-8 -*-
"""mBART Model and Tokenizer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tTLSHIsqJeDOeuMhTWMFMfoAYJ4oI-to
"""

# !pip install transformers torch pandas

import pandas as pd
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import torch

# Load data from CSV
file_path = 'cleaned_infopankki-fa.csv'
data = pd.read_csv(file_path)

# Display the first few rows to verify the structure
print(data.head())

# Assuming the columns are 'English' and 'Persian'
english_texts = data['English'].tolist()
persian_texts = data['Persian'].tolist()

# Load the mBART tokenizer and model
model_name = 'facebook/mbart-large-50-many-to-many-mmt'
tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

# Set the target language (Persian)
tokenizer.src_lang = "en_XX"
target_lang = "fa_IR"


def translate_text(text, model, tokenizer, target_lang):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt")

    # Generate translation using the model
    translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id[target_lang])

    # Decode the generated tokens into a string
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return translated_text

# Translating English sentences to Persian
translations = []
for sentence in english_texts:
    translated_sentence = translate_text(sentence, model, tokenizer, target_lang)
    translations.append(translated_sentence)

# Adding translations to the dataframe
data['mBART_Persian'] = translations

# Save the dataframe to a new CSV
data.to_csv('translated_infopankki.csv', index=False)