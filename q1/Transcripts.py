import docx
import re

def extract_transcriptions(file_path):
    # Load the Word document
    doc = docx.Document(file_path)

    transcriptions = []
    current_transcript = ""
    current_transcript_number = 0

    # Iterate through paragraphs and extract content
    for paragraph in doc.paragraphs:
        # Check if the paragraph starts a new transcript
        if re.match(r"Transcript \d+:", paragraph.text):
            # If a previous transcript is not empty and not the unwanted title, add it to the list
            if current_transcript and current_transcript_number != 0:
                transcriptions.append((f"Transcript {current_transcript_number}:", current_transcript.strip()))
            # Start a new transcript
            current_transcript = ""
            current_transcript_number += 1
        else:
            # Append the current paragraph to the current transcript
            current_transcript += paragraph.text + '\n'

    # Add the last transcript to the list if it's not the unwanted title
    if current_transcript and current_transcript_number != 0:
        transcriptions.append((f"Transcript {current_transcript_number}:", current_transcript.strip()))

    return transcriptions

# Replace the file path with your actual file path
file_path = r'C:\Users\cohen\Downloads\תמלולי שיחות.docx'

# Extract transcriptions
transcriptions = extract_transcriptions(file_path)

# Print or process the transcriptions
def make_Transcript(transcriptions):
    result = ""  # Initialize an empty string to store the formatted transcripts
    for transcript_number, (transcript_title, transcript_content) in enumerate(transcriptions, 1):
        result += f"{transcript_title}\n{transcript_content}\n\n"  # Append each transcript to the result string
    return result  # Return the final formatted transcripts as a single string

make_Transcript(transcriptions)