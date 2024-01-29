import pandas as pd # data manipulation and analysis library for Python
from openpyxl.utils.exceptions import IllegalCharacterError # library for reading and writing Excel (xlsx) files

def create_excel(data):
    if not data:
        print('No data to create Excel file.')
        return

    try:
        for entry in data:
            entry['text'] = clean_text(entry['text'])

        df = pd.DataFrame(data, columns=['url', 'title', 'text'])
        df.to_excel('Excel_Web_Crawling.xlsx', index=False)
        print('Excel file created successfully.')

        """ raised when trying to write data to an Excel file
        , and the data contains characters that are not allowed in an Excel file."""

    except IllegalCharacterError:
        print("Error writing to Excel")

def clean_text(text):
    """" preprocess the text data before writing it to an Excel file
    in a way of handling the \n and \r because we won't want the
    new line characters when inserting to an Excel file"""
    cleaned_text = text.replace('\n', '').replace('\r', '')
    return cleaned_text