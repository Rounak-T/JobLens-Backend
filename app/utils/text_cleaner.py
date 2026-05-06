import re

def text_cleaner(text):
    text= re.sub(r'[^\w\s]', '', text)
    text= text.lower()
    text= text.replace('\xa0', ' ')

    return text