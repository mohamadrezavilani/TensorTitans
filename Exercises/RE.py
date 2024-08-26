import re

def is_date(input_text):
    # Pattern 1: Dates in the format YYYY/MM/DD or YYYY-MM-DD
    pattern1 = r'\b\d{4}[/-]\d{2}[/-]\d{2}\b'

    # Pattern 2: Dates in the format DD/Month/YYYY
    pattern2 = r'\b\d{1,2}\s*/\s*[\u0600-\u06FF]+\s*/\s*\d{4}\b'

    # Pattern 3: Textual dates with optional extra spaces
    pattern3 = r'\b(?:یکم|دوم|سوم|چهارم|پنجم|ششم|هفتم|هشتم|نهم|دهم|یازدهم|دوازدهم|سیزدهم|چهاردهم|پانزدهم|شانزدهم|هفدهم|هجدم|نوزدهم|بیستم|بیست و یکم|بیست و دوم|بیست و سوم|بیست و چهارم|بیست و پنجم|بیست و ششم|بیست و هفتم|بیست و هشتم|بیست و نهم|سی‌ام|یک|دو|سه|چهار|پنج|شش|هفت|هشت|نه|ده|یازده|دوازده|سیزده|چهارده|پانزده|شانزده|هفده|هجده|نوزده|بیست|سی)\s+[\u0600-\u06FF]+\s*(?:ماه\s*)?(?:سال\s*)?\d{4}\b'

    # Combine all patterns
    combined_pattern = f'({pattern1})|({pattern2})|({pattern3})'

    # Check if the input matches any of the patterns
    if re.match(combined_pattern, input_text):
        return True
    else:
        return False


while True:
    # Get input from the user
    user_input = input("Please enter a text: ")

    # Check and display the result
    if is_date(user_input):
        print("This is a valid date.")
    else:
        print("This is not a valid date.")
