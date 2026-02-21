import easyocr
import re

reader = easyocr.Reader(['en'])

def extract_text(image_path):
    result = reader.readtext(image_path)
    text_list = [item[1].lower() for item in result]
    return text_list

def clean_text(text_list):
    cleaned = []
    for text in text_list:
        text = re.sub(r'[^a-zA-Z ]', '', text)
        text = text.strip()
        if len(text) > 3:  # ignore very small garbage
            cleaned.append(text)
    return cleaned

def detect_medicine_name(text_list, medicine_database):
    
    for text in text_list:
        for medicine in medicine_database:
            if medicine in text:
                return medicine
    
    return None