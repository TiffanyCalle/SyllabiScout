import re  

def find_dates(text):
    print("--- Looking for dates... ---")
    
    # \d means "digit" (number)
    # [a-zA-Z] means "letter"
    
    patterns = [
        # Pattern 1: "09/12" or "9/12" or "09-12"
        r'\d{1,2}[/-]\d{1,2}',
        
        # Pattern 2: "Sep 12" or "September 12" or "Sept. 12"
        # We look for the month name (short or long), a space, then a number.
        r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z.]* \d{1,2}',
        
        # Pattern 3: "12th of September"
        r'\d{1,2}(?:st|nd|rd|th)? of (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*'
    ]
    
    