import openai
from decouple import config
from Transcripts import extract_transcriptions,make_Transcript
from Transcripts_In_List import separate_transcripts
from oneBIproject.q1.Answers_By_Format import answers

""" "OPENAI_API_KEY" will be equal to my api as environment variable."""
api_key = config("OPENAI_API_KEY")
openai.api_key = api_key

file_path = r'C:\Users\cohen\Downloads\תמלולי שיחות.docx'
transcriptions = extract_transcriptions(file_path)
Transcriptions = make_Transcript(transcriptions)
list_of_transactions = separate_transcripts(Transcriptions)

answers(list_of_transactions)





