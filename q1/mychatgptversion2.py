import openai
from decouple import config
from Transcripts import extract_transcriptions,make_Transcript
from createformat import separate_transcripts
import time

file_path = r'C:\Users\cohen\Downloads\תמלולי שיחות.docx'
transcriptions = extract_transcriptions(file_path)
Transcriptions = make_Transcript(transcriptions)

api_key = config("OPENAI_API_KEY")
openai.api_key = api_key

def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use GPT-3.5-turbo
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

list_of_transactions = separate_transcripts(Transcriptions) # list of 4 variables as the number of transactions

prompt_question = "January 26, 2024 I have a transcript of a customer service call. I need specific information extracted from this transcript and no more comments or information other than that please. Please find the following details: • Customer's full name: • Address: • The problem: • Customer satisfaction['low','medium','high']: If you didn't find a certain value, set it as 'Unspecified'."

for i in range(0,len(list_of_transactions)):
    time.sleep(20)
    conversation = f"{list_of_transactions[i]}\n\n{prompt_question}"
    response = chat_gpt(conversation)
    print(response)


# # Combine the transcript and the question
# conversation = f"{Transcriptions}\n\n{prompt_question}"

# Get the response from GPT-3.5-turbo
# response = chat_gpt(conversation)
#
# # Print the generated response
# print(response)