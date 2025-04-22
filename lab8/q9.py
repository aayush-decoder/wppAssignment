import re

def tokenizer(text):
    patterns = {
        "punctuation": r'[!?.,;:"\'()\[\]{}]',
        "date": r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b|\b\d{1,2}\s\w+\s\d{4}\b',
        "url":r'https?://\S+|www\.\S+|\b\w+\.\w{2,3}\b',
        "email": r'\b\w+@\w+\.\w+\b',
        "number":r'\b\d{1,3}(?:,\d{2,3})*(?:\.\d+)?\b|\b\d+/\d+\b' ,
        "social_handle": r'@\w+|#\w+',
        "hindi_word": r'[\u0900-\u097F]+'
    } 
    
    tokes = []
    for key, pat in patterns.items():
        tokes.extend(re.findall(pat, text))
    
    return tokes

text = "आज 10/03/2024 को @aayush_droid ने https://google.com पर ३३.१५ रुपये में कुछ खरीदा।"
print(tokenizer(text))
