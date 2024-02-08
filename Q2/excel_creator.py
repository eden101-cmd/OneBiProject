import pandas as pd
from openpyxl.utils.exceptions import IllegalCharacterError

def create_excel_file(data):
    """
    Creates an Excel file from a list of dictionaries.
    Arg:
    data (list): A list of dictionaries containing information about web pages.
            Each dictionary should include 'url', 'title', and 'text' keys.
    Returns:
        None
    """
    if not data:
        print('No data to create Excel file.')
        return

    try:
        for entry in data:
            entry['text'] = clean_text_data(entry['text'])

        df = pd.DataFrame(data, columns=['title','url', 'text'])
        df.to_excel('Excel_Web_Crawling.xlsx', index=False)
        print('Excel file created successfully.')

    except IllegalCharacterError:
        print("Error writing to Excel")

def clean_text_data(text):
    """
    Preprocesses the text data before writing it to an Excel file,
    handling new line and carriage return characters.
    arg:
        text (str): The text data to be cleaned.
    Returns:
        str: The cleaned text data.
    """
    cleaned_text = text.replace('\n', '').replace('\r', '')
    return cleaned_text

