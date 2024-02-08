import openai
from decouple import config
from transcription_extractor import extract_transcripts_from_docx, format_combined_transcripts
from transcript_separator import separate_transcripts
from oneBIproject.Q1.gpt_chat_processing import answers

def set_openai_api_key():
    """
    Set OpenAI API key from the environment variable.
    Args:
        None
    Returns:
        None
    """
    api_key = config("OPENAI_API_KEY")
    openai.api_key = api_key

file_path = 'prompt_questions.txt'

# Open the file and read its content into a string
with open(file_path, 'r') as file:
    prompt_question = file.read()

def process_transcriptions(file_path):
    """
    Process transcriptions and obtain answers.
    Args:
        file_path (str): The file path to the document containing transcriptions.
    Returns:
        None
    """
    # Extract and make transcripts
    transcripts_tuples = extract_transcripts_from_docx(file_path)
    ordered_transcriptions = format_combined_transcripts(transcripts_tuples)

    # Separate transcripts
    separated_transcripts = separate_transcripts(ordered_transcriptions)

    # Get answers
    answers(separated_transcripts, prompt_question)

def main():
    """
    Main function to set up OpenAI API key and process transcriptions.
    Args:
        None
    Returns:
        None
    """
    # Set OpenAI API key
    set_openai_api_key()

    # Specify the file path for transcriptions
    file_path = r'C:\Users\cohen\Downloads\תמלולי שיחות.docx'

    # Process transcripts and obtain answers
    process_transcriptions(file_path)

if __name__ == "__main__":
    main()
