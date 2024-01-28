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

prompt_questions = [
    "Extract the requested details from the customer service call transcript dated January 26, 2024 will always be in this format: 1.Customer's full name:if you cant find the customer name please answer:'Unspecified' 2.Address: if you cant find the address please answer 'Unspecified' 3.The problem: 4.Customer satisfaction level: please asses the customer satisfaction level and then answer one of the follwing answers:'low','medium' or 'high', no more information will be given. I need you 2 keep in mind 2 important things: the format that I presented to you need to be in every answer and I need from you to asses the customer statisfaction level from the transcript. please dont mention any other notes or titles .",
    "Please carefully review the customer service call transcript from January 26, 2024 will always be in this format: : 1.Customer's full name:if you cant find the customer name please answer:'Unspecified' 2.Address: if you cant find the address please answer 'Unspecified' 3.The problem: 4.Customer satisfaction level:the only answers to this question can be :'low', 'medium' or 'high' , no more information will be given. please asses the customer statisfaction level from the transcript.please don't mention any other information from what requested",
    "Your task is to examine the customer service call transcript from January 26, 2024 will always be in this format: : 1.Customer's full name: 2.Address: f you cant find the address please answer 'Unspecified' 3.The problem: 4.Customer satisfaction level:the only answers to this question can be :'low', 'medium' or 'high'. please asses the customer statisfaction level from the transcript. please don't mention any other information except those 4 answers",
    "Please extract the specified details from the customer service call transcript recorded on January 26, 2024 will always be in this format: :1.Customer's full name: if you cant find the customer name please answer:'Unspecified' 2.Address:  if you cant find the address please answer 'Unspecified' 3.The problem: 4.Customer satisfaction level:['low', 'medium', 'high'] If any data is not available, note it as Unspecified.' I need you 2 keep in mind 2 important things: the format that I presented to you need to be in every answer and I need from you to asses the customer statisfaction level from the transcript.please don't mention any other information from what requested"
]


for i in range(0,len(list_of_transactions)):
    if i != 0:
        time.sleep(20)
        conversation = f"{list_of_transactions[i]}\n\n{prompt_questions[i]}"
        response = chat_gpt(conversation)
        print(response + "\n")
    else:
        conversation = f"{list_of_transactions[i]}\n\n{prompt_questions[i]}"
        response = chat_gpt(conversation)
        print(response + "\n")



