from openai import OpenAI
from decouple import config
from createformat import read_transcript

api_key = config("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def replace_role(conversation, old_role, new_role):
    new_conversation = []
    for message in conversation:
        new_message = message.copy()
        if message['role'] == old_role:
            new_message['role'] = new_role
        new_conversation.append(new_message)
    return new_conversation

def get_concise_info(response):
    lines = response.split('\n')
    concise_info = lines[0].strip() if lines else 'Unspecified'
    return concise_info

def get_chat_response(existing_conversation, user_input):
    existing_conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=existing_conversation
    )

    chat_response = response.choices[0].message.content.strip() if response.choices else 'Unspecified'
    return chat_response

def get_concise_responses(existing_conversation, questions):
    concise_responses = []

    for question in questions:
        response = get_chat_response(existing_conversation, question)
        concise_info = get_concise_info(response)
        concise_responses.append(concise_info)

    return concise_responses

# Given conversation
conversation = read_transcript("C:\\Users\\cohen\\Transcripts\\Transcript1.docx")

# Replace 'service representative' with 'system' in the conversation
formed_conversation = replace_role(conversation, 'service representative', 'system')

# Add system message for context
formed_conversation.insert(0, {"role": "system", "content": "You are an assistant that helps with customer inquiries."})

# Example questions
questions_to_ask = [
    "What details were mentioned about the customer's full name?",
    "What details were mentioned about the user's location or residence?",
    "What problem did the customer mention?",
    "How satisfied is the customer—low, medium, or high?"
]

# Get concise responses to the questions
concise_responses = get_concise_responses(formed_conversation, questions_to_ask)

# Print or use the concise responses
formatted_responses = [
    f"1. Customer's full name: {concise_responses[0]}",
    f"2. Address: {concise_responses[1]}",
    f"3. The problem: {concise_responses[2]}",
    f"4. Customer satisfaction: {concise_responses[3]}"
]

for formatted_response in formatted_responses:
    print(formatted_response)
