import docx #
import re

def extract_transcriptions(file_path):
    doc = docx.Document(file_path)

    transcriptions = []
    current_transcript = ""
    current_transcript_number = 0
    """ Iterate through paragraphs and extract content by 
    looking for a string that starts with "Transcript " followed by one or more digits,
    the beginning of the string, and if it is true then we will access 
    to text content of each paragraph and will add them to the list.
    """
    for paragraph in doc.paragraphs:
        if re.match(r"Transcript \d+:", paragraph.text):
            if current_transcript and current_transcript_number != 0:
                transcriptions.append((f"Transcript {current_transcript_number}:", current_transcript.strip()))
            current_transcript = ""
            current_transcript_number += 1
        else:
            current_transcript += paragraph.text + '\n'

    if current_transcript and current_transcript_number != 0:
        transcriptions.append((f"Transcript {current_transcript_number}:", current_transcript.strip()))

    return transcriptions

file_path = r'/Downloads/תמלולי שיחות.docx'


def make_Transcript(transcriptions):
    """For each transcription, it appends a string to the result variable,
    consisting of the transcript title followed by the transcript content, separated by newline characters"""
    result = ""
    for transcript_number, (transcript_title, transcript_content) in enumerate(transcriptions, 1):
        result += f"{transcript_title}\n{transcript_content}\n\n"
    return result

