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
    
    found_dates = []

    # Loop through every pattern and see if it matches anything in the text
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE) # ignores upper/lower case means
        found_dates.extend(matches)
        
    return found_dates


# read from file made in reader.py
try:
    with open("collected_info.txt", "r") as f:
        raw_text = f.read()
    
    dates = find_dates(raw_text)
    
    #dates found
    if dates:
        print(f"I found {len(dates)} potential dates:")
        for date in dates:
            print(f" - {date}")
    else:
        print("I couldn't find any dates. The format might be different. Take a closer look.")

# exception handling
except FileNotFoundError:
    print("Error: I can't find 'collected_info.txt'. Did you run reader.py first?")