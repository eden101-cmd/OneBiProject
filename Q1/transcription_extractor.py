import docx
import re
# שכל ההערות על הםונקציה יהיו אחידות
def extract_transcripts_from_docx(file_path):
    """
    Extracts transcripts from a DOCX file.
    Args:
        file_path (str): The path to the DOCX file.
    Returns:
        list: A list of tuples, where each tuple contains a transcript title
              and its content.
    """
    doc = docx.Document(file_path)

    transcripts = []
    current_transcript = ""
    current_transcript_number = 0

    for paragraph in doc.paragraphs:
        if re.match(r"Transcript \d+:", paragraph.text):
            if current_transcript and current_transcript_number != 0:
                transcripts.append((f"Transcript {current_transcript_number}:", current_transcript.strip()))
            current_transcript = ""
            current_transcript_number += 1
        else:
            current_transcript += paragraph.text + '\n'

    if current_transcript and current_transcript_number != 0:
        transcripts.append((f"Transcript {current_transcript_number}:", current_transcript.strip()))

    return transcripts

def format_combined_transcripts(transcripts):
    """
    Combines transcripts into a single formatted string.
    Args:
        transcripts (list): A list of tuples, where each tuple contains a
                            transcript title and its content.
    Returns:
        str: A formatted string combining all transcripts.
    """
    result = ""
    for transcript_number, (transcript_title, transcript_content) in enumerate(transcripts, 1):
        result += f"{transcript_title}\n{transcript_content}\n\n"
    return result
