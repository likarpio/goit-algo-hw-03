import re

def normalize_phone(phone_number):
    pattern = r"[^0-9+]"
    cleaned_number = re.sub(pattern, "", phone_number)
    
    if cleaned_number.startswith("380"):
        cleaned_number = "+" + cleaned_number
        
    if not cleaned_number.startswith("+"):
        cleaned_number = "+38" + cleaned_number
        
    return cleaned_number
