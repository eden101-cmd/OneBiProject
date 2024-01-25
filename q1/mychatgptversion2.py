from openai import OpenAI
from decouple import config
from createformat import read_transcript

api_key = config("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Given conversation
conversation = read_transcript("C:\\Users\\cohen\\Transcripts\\Transcript1.docx")

def get_response_chat_with_info(conversation, questions):
    # Call the OpenAI API to generate completions for the given messages
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation + [{"role": "user", "content": question} for question in questions]
    )

    # Extract and return the generated response from the API response
    return response.choices[0].message.content.strip()


questions_to_ask = [
    "How can I improve my internet connection?",
    "What should I do if restarting doesn't solve my network issue?",
    "How do I change the wireless channel on my router?",
    "What steps should I take if I still can't connect after changing the wireless channel?"
]

# Get the response based on the existing conversation and questions
response = get_response_chat_with_info(conversation, questions_to_ask)

# checking : Print or use the generated response
print(response)






