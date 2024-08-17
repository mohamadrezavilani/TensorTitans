# Dictionaries

english_dict = {
    'ᴀ': 'a',
    'b': 'b',
    'ʙ': 'b',
    'c': 'c',
    'ᴄ': 'c',
    'd': 'd',
    'ᴅ': 'd',
    'e': 'e',
    'ᴇ': 'e',
    'f': 'f',
    'ꜰ': 'f',
    'g': 'g',
    'ɢ': 'g',
    'ʜ': 'h',
    'i': 'i',
    'ɪ': 'i',
    'ᴊ': 'j',
    'j': 'j',
    'k': 'k',
    'ᴋ': 'k',
    'l': 'l',
    'ʟ': 'l',
    'm': 'm',
    'ᴍ': 'm',
    'n': 'n',
    'ɴ': 'n',
    'o': 'o',
    'ᴏ': 'o',
    'ᴘ': 'p',
    'p': 'p',
    'q': 'q',
    'r': 'r',
    'ʀ': 'r',
    's': 's',
    'ꜱ': 's',
    't': 't',
    'ᴛ': 't',
    'u': 'u',
    'ᴜ': 'u',
    'v': 'v',
    'ᴠ': 'v',
    'w': 'w',
    'ᴡ': 'w',
    'x': 'x',
    'y': 'y',
    'ʏ': 'y',
    'z': 'z'
}

num_dict = {
    '۹': '9',
    '٩': '9',
    '9': '9',
    '۸': '8',
    '٨': '8',
    '8': '8',
    '۷': '7',
    '٧': '7',
    '7': '7',
    '۶': '6',
    '٦': '6',
    '6': '6',
    '۵': '5',
    '٥': '5',
    '5': '5',
    '۴': '4',
    '٤': '4',
    '4': '4',
    '۳': '3',
    '٣': '3',
    '3': '3',
    '۲': '2',
    '٢': '2',
    '2': '2',
    '۱': '1',
    '١': '1',
    '1': '1',
    '۰': '0',
    '٠': '0',
    '0': '0'
}

arabic_dict = {
    'ك': 'ک',
    'ڪ': 'ک',
    'ک': 'ک',
    'ئ': 'ی',
    'ی': 'ی',
    'ێ': 'ی',
    'ي': 'ی',
    'ى': 'ی',
    'ۆ': 'و',
    'ؤ': 'و',
    'و': 'و',
    'ڕ': 'ر',
    'ر': 'ر',
    'ة': 'ه',
    'ه': 'ه',
    'ہ': 'ه',
    'آ': 'ا',
    'أ': 'ا',
    'إ': 'ا',
    'ا': 'ا',
    'ء': 'ا',
    'ً': ' ',
    'ٌ': ' ',
    'ٍ': ' ',
    'َ': ' ',
    'ُ': ' ',
    'ِ': ' '
}

contractions_dict = {
    "I'm": "I am",
    "you're": "you are",
    "he's": "he is",
    "she's": "she is",
    "it's": "it is",
    "we're": "we are",
    "they're": "they are",
    "aren't": "are not",
    "can't": "cannot",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'll": "he will",
    "he's": "he is",
    "I'd": "I would",
    "I'll": "I will",
    "I'm": "I am",
    "I've": "I have",
    "isn't": "is not",
    "let's": "let us",
    "mightn't": "might not",
    "mustn't": "must not",
    "shan't": "shall not",
    "she'd": "she would",
    "she'll": "she will",
    "she's": "she is",
    "shouldn't": "should not",
    "that's": "that is",
    "there's": "there is",
    "they'd": "they would",
    "they'll": "they will",
    "they're": "they are",
    "they've": "they have",
    "we'd": "we would",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "where's": "where is",
    "who's": "who is",
    "who'll": "who will",
    "who're": "who are",
    "who's": "who is",
    "who've": "who have",
    "won't": "will not",
    "wouldn't": "would not",
    "you'd": "you would",
    "you'll": "you will",
    "you're": "you are",
    "you've": "you have"
}

sign_dict_en = {
    '...': '…',  # Replace triple periods with a single ellipsis
    '..': '…',  # Replace double periods with a single ellipsis
    '. . .': '…',  # Replace spaced triple periods with a single ellipsis
    '…': '.',  # Convert ellipsis back to a period if needed for standardization
    '"': '"',  # Replace straight double quotes with consistent quotes (adjust based on context)
    '“': '"',  # Replace left double quotation marks with straight double quotes
    '”': '"',  # Replace right double quotation marks with straight double quotes
    '‘': '"',  # Replace left single quotation mark with straight double quote
    '’': '"',  # Replace right single quotation mark with straight double quote
    '""': '"',
    '-': ' - ',  # Replace hyphen with an em dash for proper punctuation
    '—': ' — ',  # Replace hyphen with an em dash for proper punctuation
    '_': ' ',  # Replace underscores with a space
    '%': ' percent ',  # Replace percentage sign with the Persian percentage sign
    '@': '',  # Remove unwanted character '@'
    '#': '',  # Remove unwanted character '#'
    '$': '',  # Remove unwanted character '$'
    '^': '',  # Remove unwanted character '^'
    '&': '',  # Remove unwanted character '&'
    '*': '',  # Remove unwanted character '*'
    '{': '',  # Remove unwanted character '{'
    '}': '',  # Remove unwanted character '}'
    '\\': '',  # Remove unwanted backslash '\'
    '`': '',  # Remove unwanted backtick '`'
    '|': '',  # Remove unwanted pipe '|'
    '/': '',  # Remove forward slash '/'
    '•': ' ',  # Replace bullet point with a space
    '。': ' ',  # Remove full stop in CJK (Chinese, Japanese, Korean) languages
    '¡': ' ',  # Remove inverted exclamation mark
    '¿': ' ',  # Remove inverted question mark
    '¨': ' ',  # Remove diaeresis (two dots above a letter)
    '¯': ' ',  # Remove macron (a horizontal line above a letter)
    '°': ' ',  # Remove degree sign
    '±': ' ',  # Remove plus-minus sign
    '²': ' ',  # Remove superscript two
    '³': ' ',  # Remove superscript three
    '´': ' ',  # Remove acute accent
    'µ': ' ',  # Remove micro sign
    '¶': ' ',  # Remove pilcrow sign (paragraph mark)
    '·': ' ',  # Remove middle dot
    '¸': ' ',  # Remove cedilla (a hook under certain letters)
    '¹': ' ',  # Remove superscript one
    '☑': ' ',  # Remove ballot box with check
    '↓': ' ',  # Remove downwards black arrow
    '➡': ' ',  # Remove right arrow
    '⬅': ' ',  # Remove left arrow
    '▫': ' ',  # Remove white small square
    '⃣': ' ',  # Remove combining enclosing keycap
    '»': '"',  # Ensure space before closing Persian quotation mark
    '«': '"',  # Ensure space after opening Persian quotation mark
    '<': ' ',  # Remove less-than sign
    '>': ' ',  # Remove greater-than sign
    '+': ' ',  # Remove plus sign
    '~': ' ',  # Remove tilde
    '=': ' ',  # Remove equals sign
    '×': ' ',  # Remove multiplication sign
    '《': ' ',  # Remove left double angle quotation mark in CJK languages
    '》': ' ',  # Remove right double angle quotation mark in CJK languages
    '「': ' ',  # Remove Japanese corner bracket (left)
    '」': ' ',  # Remove Japanese corner bracket (right)
    '、': ' ',  # Remove Japanese comma
    '｀': ' ',  # Remove Japanese half-width katakana comma
    'ً': ' ',  # Remove Arabic fathatan (a diacritical mark)
    '〜': ' ',  # Remove Japanese wave dash
    'ヽ': ' ',  # Remove Japanese iteration mark
    '\n': ' ',  # Replace newline with space
    '\r': ' ',  # Replace carriage return with space
}


sign_dict_fa = {
    ',': '،',  # Replace English comma with Persian comma
    ';': '؛',  # Replace English semicolon with Persian semicolon
    '?': '؟',  # Replace English question mark with Persian question mark
    '!': '!',  # Ensure exclamation marks are consistent with Persian usage
    ':': ':',  # Ensure colons are consistent (no change needed for Persian)
    '...': '…',  # Replace triple periods with a single ellipsis
    '..': '…',  # Replace double periods with a single ellipsis
    '. . .': '…',  # Replace spaced triple periods with a single ellipsis
    '…': '.',  # Convert ellipsis back to a period if needed for standardization
    '"': '"',  # Replace straight double quotes with consistent quotes (adjust based on context)
    '“': '"',  # Replace left double quotation marks with straight double quotes
    '”': '"',  # Replace right double quotation marks with straight double quotes
    "'": '‘’',  # Replace single quotes with Persian-style single quotation marks
    '‘': '"',  # Replace left single quotation mark with straight double quote
    '’': '"',  # Replace right single quotation mark with straight double quote
    '(': ' ( ',  # Replace left parenthesis with Persian-style left quotation mark (optional)
    ')': ' ) ',  # Replace right parenthesis with Persian-style right quotation mark (optional)
    '-': '—',  # Replace hyphen with an em dash for proper punctuation
    '—': ' — ',  # Replace hyphen with an em dash for proper punctuation
    '_': ' ',  # Replace underscores with a space
    '@': '',  # Remove unwanted character '@'
    '#': '',  # Remove unwanted character '#'
    '$': '',  # Remove unwanted character '$'
    '%': '٪',  # Replace percentage sign with the Persian percentage sign
    '٪': ' درصد ',  # Replace percentage sign with the Persian percentage sign
    '^': '',  # Remove unwanted character '^'
    '&': '',  # Remove unwanted character '&'
    '*': '',  # Remove unwanted character '*'
    # '[': '',  # Remove unwanted character '['
    # ']': '',  # Remove unwanted character ']'
    '{': '',  # Remove unwanted character '{'
    '}': '',  # Remove unwanted character '}'
    '\\': '',  # Remove unwanted backslash '\'
    '`': '',  # Remove unwanted backtick '`'
    '|': '',  # Remove unwanted pipe '|'
    '/': '',  # Remove forward slash '/'
    '•': ' ',  # Replace bullet point with a space
    '。': ' ',  # Remove full stop in CJK (Chinese, Japanese, Korean) languages
    '¡': ' ',  # Remove inverted exclamation mark
    '¿': ' ',  # Remove inverted question mark
    '¨': ' ',  # Remove diaeresis (two dots above a letter)
    '¯': ' ',  # Remove macron (a horizontal line above a letter)
    '°': ' ',  # Remove degree sign
    '±': ' ',  # Remove plus-minus sign
    '²': ' ',  # Remove superscript two
    '³': ' ',  # Remove superscript three
    '´': ' ',  # Remove acute accent
    'µ': ' ',  # Remove micro sign
    '¶': ' ',  # Remove pilcrow sign (paragraph mark)
    '·': ' ',  # Remove middle dot
    '¸': ' ',  # Remove cedilla (a hook under certain letters)
    '¹': ' ',  # Remove superscript one
    '☑': ' ',  # Remove ballot box with check
    '↓': ' ',  # Remove downwards black arrow
    '➡': ' ',  # Remove right arrow
    '⬅': ' ',  # Remove left arrow
    '▫': ' ',  # Remove white small square
    '⃣': ' ',  # Remove combining enclosing keycap
    '»': '"',  # Ensure space before closing Persian quotation mark
    '«': '"',  # Ensure space after opening Persian quotation mark
    '<': ' ',  # Remove less-than sign
    '>': ' ',  # Remove greater-than sign
    '+': ' ',  # Remove plus sign
    '~': ' ',  # Remove tilde
    '=': ' ',  # Remove equals sign
    '×': ' ',  # Remove multiplication sign
    '《': ' ',  # Remove left double angle quotation mark in CJK languages
    '》': ' ',  # Remove right double angle quotation mark in CJK languages
    'ّ': ' ',  # Remove Arabic shadda (mark indicating gemination)
    'ٔ': ' ',  # Remove Arabic small high sign
    '「': ' ',  # Remove Japanese corner bracket (left)
    '」': ' ',  # Remove Japanese corner bracket (right)
    '、': ' ',  # Remove Japanese comma
    '｀': ' ',  # Remove Japanese half-width katakana comma
    'ً': ' ',  # Remove Arabic fathatan (a diacritical mark)
    '〜': ' ',  # Remove Japanese wave dash
    'ヽ': ' ',  # Remove Japanese iteration mark
    '\n': ' ',  # Replace newline with space
    '\r': ' ',  # Replace carriage return with space
    '‎': ' ',  # Replace invisible empty space character with a regular space
    '‌': ' ',  # Replace Zero Width Non-Joiner with a regular space
    '\u00A0': ' ',  # Replace non-breaking spaces with regular space
}


punctuation_dict = {
    '\n': ' ',
    '\r':  ' ',
    '‎':  ' ',  # Empty Space
    '‌':  ' ',  # Zero Width Non-Joiner (A character used in text rendering and typography to control the joining behavior of adjacent characters, particularly in scripts such as Arabic and Indic scripts.)
    'ヽ': ' ',
    '、': ' ',
    '｀': ' ',
    'ً': ' ',
    '#': ' ',
    # 'ـ':  ' ',
    '/': ' ',
    ',': '،',
    # '-': ' ',
    '،': '،',
    # '.': ' ',
    '٪': ' درصد ',
    '%': ' درصد ',
    '$':  ' دلار ',
    # '؛': ' ',
     ' ': ' ',
     # '٠': ' ',
     # '_': ' ',
     '؟': '?',
     # '?': ' ',
     '@': ' ',
     ']': ' ',
    '[': ' ',
    # '!': ' ',
    '…': ' ',
    # ')': ' ',
    # '(': ' ',
    # '–': ' ',
    # '"': ' ',
    '&': ' ',
    '*': ' ',
    # ': ': ' ',
    # ';': ' ',
    '|': ' ',
    '¡': ' ',
    '+': ' ',
    '<': ' ',
    '=': ' ',
    '>': ' ',
    # '«': ' ',
    # '»': ' ',
    'ّ': ' ',
    'ٔ': ' ',
    '...': '.',
    '..': '.',
    '”': '"',
    '“': '"',
    "•": " ",  # Bullet
    "☑": " ",  # Ballot Box with Check
    "↓": " ",  # Downwards Black Arrow
    "➡": " ",  # Right Arrow
    "▫": " ",  # White Small Square
    "⬅": " ",  # Left Arrow
    "×": " ",  # Multiplication Sign
    "》": " ",  # Right Double Angle Quotation Mark
    "《": " ",  # Left Double Angle Quotation Mark
    "~": " ",  # Tilde
    "⃣": " ",  # Combining Enclosing Keycap
    "ٕ": " ",  # Arabic Small High Sign Safa
    "�": " ",  # Replacement Character
    "⁩": " ",  # Right Isolate
    "⁧": " "  # Left Isolate
}

emoji_dict = {
    '🧢':  ' ',
    '🦋':  ' ',
    '🥲':  ' ناراضی ',
    '🥰':  ' عالی ',
    '🥇':  ' ',
    '🥂':  ' خوب',
    '🤬':  ' ناراضی ',
    '🤩':  ' عالی ',
    '🤦':  ' ',
    '🤤':  ' ',
    '🤣':  ' ',
    '🤢':  ' ناراضی ',
    '🤝':  ' ',
    '🤙':  ' ',
    '🤗':  ' خوب ',
    '🤔':  ' ',
    '🤏':  ' ',
    '🤍':  ' عالی ',
    '🟩':  ' ',
    '🚀':  ' ',
    '🙏':  ' ',
    '🙌':  ' ',
    '🙈':  ' ',
    '🙃':  ' ',
    '🙂':  ' عالی',
    '😮':  ' ',
    '😭':  ' غم ',
    '😬':  ' تنفر ',
    '😤':  ' عصبانیت ',
    '😣':  ' درد ',
    '😢':  ' غم ',
    '😡':  ' ناراضی ',
    '😠':  ' ناراضی ',
    '😙':  ' ',
    '😕':  ' ',
    '😔':  ' ناراضی ',
    '😒':  ' ',
    '😐':  ' ',
    '😎':  ' ',
    '😍':  ' عالی ',
    '😌':  ' ',
    '😊':  ' عالی ',
    '😉':  ' ',
    '😃':  ' عالی ',
    '😂':  ' ',
    '😁':  ' ',
    '🖕':  ' ناراضی ',
    '🔥':  ' ',
    '📸':  ' ',
    '📩':  ' ',
    '📌':  ' ',
    '💵':  ' پول ',
    '💰':  ' پول ',
    '💯':  ' عالی ',
    '💪':  ' عالی ',
    '💣':  ' ',
    '💜':  ' ',
    '💚':  ' ',
    '💖':  ' ',
    '💔':  ' ',
    '❤️':  ' ',
    '💐':  ' ',
    '💎':  ' ',
    '💌':  ' ',
    '👑':  ' ',
    '👏':  ' ',
    '👍':  ' ',
    '👌':  ' عالی ',
    '👉':  ' ',
    '👈':  ' ',
    '👇':  ' ',
    '👁':  ' ',
    '🏼':  ' ',
    '🏻':  ' ',
    '🏆':  ' جایزه',
    '🏅':  ' ',
    '🍕':  ' ',
    '🌹':  ' ',
    '🌷':  ' ',
    '🌵':  ' ',
     '️':  ' ',
     '‍':  ' ',
     "'":  ' ',
    '☀':  ' ',
    '☺':  ' عالی ',
    '♂':  ' ',
    '♥':  ' عالی ',
    '✌':  ' عالی ',
    '✓':  ' ',
    '✗':  ' ',
    '❤':  ' عالی ',
    '✋':  ' ',
    '⚠':  ' ',
    '☘':  ' ',
    '⚘':  ' ',
    '⚪':  ' ',
    '⭐':  ' ',
    "✅":  ' ',
    "🟣":  ' ',
    "🤮":  ' ناراضی ',
    "🤷":  ' ',
    "😅":  ' ',
    "🕓":  ' ',
    "🙄":  ' ',
    "☹":  ' ',
    "😳":  ' ',
    "🦍":  ' ',
    "❣":  ' ',
    "🌺":  ' ',
    "🤌":  ' ',
    "🌱":  ' ',
    "🔸":  ' ',
    "😇":  ' خوب ',
    "😀":  ' خوب ',
    "🔻":  ' ',
    "🎁":  ' ',
    "✨":  ' ',
    "🤡":  ' ',
    "👀":  ' ',
    "👎":  " ناراضی ",
    "🥴":  " ناراضی ",
    "⬆":  " ",
    "💥":  " ",
    "🛸":  " ",
    "🤑":  " ",
    "🏽":  " ",
    "🔰":  " ",
    "٫":  " ",
    "🪐":  " ",
    "⚡":  " ",
    "🤨":  " ",
    "😜":  " ",
    "💫":  " ",
    "🩷":  " ",
    "🤘":  " ",
    "％":  " ",
    "💸":  " ",
    "🏵":  " ",
    "🟥":  " ",
    "🎉":  " ",
    "🙋":  " ",
    "🫣":  ' ',
    '🗨':  ' ',
    '💟':  ' ',
    '🧐':  ' ',
    "🐂":  " ",
    "⬇":  " ",
    "ト":  " ",
    "フ":  " ",
    "ム":  " ",
    "ー":  " ",
    "ッ":  " ",
    "ォ":  " ",
    "え":  " ",
    "を":  " ",
    "教":  " ",
    "プ":  " ",
    "て":  " ",
    "く":  " ",
    "だ":  " ",
    "さ":  " ",
    "い":  " ",
    "😄":  " ",
    "ە":  " ",
    "ラ":  " ",
    "😪":  " ",
    "引":  " ",
    "👫":  " ",
    "😘":  " خوب ",
    "💙":  " ",
    "🤲":  " ",
    "♀":  " ",
    "💶":  " ",
    "€":  " ",
    "🌸":  " ",
    "取":  " ",
    "🖤":  " ",
    "🥶":  " ",
    "🦊":  " ",
    "で":  " ",
    "確":  " ",
    "実":  " ",
    "な":  " ",
    '📥':  " ",
    '🌕':  " ",
    '👃':  " ",
    '💋':  " ",
     '😰':  " ",
     '🧿':  " ",
     '‏':  " ",
    '🫶':  ' ',  # Arm Bandage
    '🫤':  ' ',  # Hand with Fingers Splayed
    '🫰':  ' ',  # Head in Clouds
    '🫵':  ' ',  # Person with Crown
    "🫢":  " ",   # Sushi
    "🫡":  " ",   # Dumpling
    "🫠":  " ",   # Tofu
    "🧮":  " ",   # Abacus
    "🦫":  " ",   # Beaver
    "🦥":  " ",   # Sloth
    "🥸":  " ",   # Disguised Face
    "🤯":  " ",   # Exploding Head
    "🤓":  " ",   # Nerd Face
    "🚶":  " ",   # Person Walking
    "😵":  " ",   # Dizzy Face
    "😥":  " ناراضی ",   # Sad but Relieved Face
    "😑":  " ",   # Expressionless Face
    "😆":  " ",   # Grinning Squinting Face
    "🔽":  " ",   # Downwards Button
    "🔹":  " ",   # Small Blue Diamond
    "🔗":  " ",   # Link
    "🔄":  " ",   # Counterclockwise Arrows Button
    "📈":  " ",   # Chart Increasing
    "💗":  " ",   # Growing Heart
    "💕":  " ",   # Two Hearts
    "💀":  " ",   # Skull
    "👋":  " ",   # Waving Hand
    "🌿":  " ",   # Herb
    "🌐":  " ",   # Globe with Meridians
    "•":  " ",   # Bullet
    "☑":  " ",   # Ballot Box with Check
    "↓":  " ",   # Downwards Black Arrow
    "➡":  " ",   # Right Arrow
    "▫":  " ",   # White Small Square
    "⬅":  " ",   # Left Arrow
    "×":  " ",   # Multiplication Sign
    "》":  " ",   # Right Double Angle Quotation Mark
    "《":  " ",   # Left Double Angle Quotation Mark
    "~":  " ",   # Tilde
    "⃣":  " ",   # Combining Enclosing Keycap
    "ٕ":  " ",   # Arabic Small High Sign Safa
    "�":  " ",   # Replacement Character
    "⁩":  " ",   # Right Isolate
    "⁧":  " "   # Left Isolate
}
