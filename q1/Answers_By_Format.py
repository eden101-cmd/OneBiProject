import time
import openai

def chat_gpt(prompt):
    """This will be like a bridge between my application and the OpenAI GPT-3.5-turbo model,
    allowing me to obtain generated text based on a user-provided prompt in a chat-like format."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()



def answers(list_of_transactions):
    """ this function will help us to get the  answers to the prompt we entered to the chat."""
    prompt_questions = [
        "Extract the requested details from the customer service call transcript that will always be in this format: 1.Customer's full name:if you cant find the customer name please answer:'Unspecified' 2.Address: if you cant find the address please answer 'Unspecified' 3.The problem: please shortly explain the probelm 4.Customer satisfaction level: Please start your response with lowercase letters and avoid using capitals. Consider reading the transcript, thinking, and then determine the customer satisfaction level by providing answers in the format 'low', 'medium', or 'high'.",
        "Please carefully review the customer service call transcript that will always be in this format: 1.Customer's full name:if you cant find the customer name please answer:'Unspecified' 2.Address: if you cant find the address please answer 'Unspecified' 3.The problem: please shortly explain the problem 4.Customer satisfaction level:Begin your responses using lowercase letters, and avoid the use of capitals. Please stick to providing only the essential information without any additional content. now answer this question by following this instructions: please read the transcript, think and then determine the customer satisfaction level by those exact answers: 'low','medium' or 'high'. have the answers numbered in the same way of the format you got.",
        "Your task is to examine the customer service call transcript that will always be in this format: 1.Customer's full name: 2.Address: f you cant find the address please answer 'Unspecified' 3.The problem: please shortly explain the problem 4.Customer satisfaction level:Please ensure that your responses begin with lowercase letters rather than capitalas and don't add any other information. now answer this question by following this instructions: please read the transcript, think and then determine the customer satisfaction level by those exact answers: 'low','medium' or 'high'. please don't mention any notes,reasoning or any other kind of more information. please have the answers numbered in the same way of the format you got.",
        "Please extract the specified details from the customer service call transcript that will always be in this format: :1.Customer's full name: if you cant find the customer name please answer:'Unspecified' and don't add more information 2.Address:  if you can't find the address please answer 'Unspecified' 3.The problem: please shortly explain the problem 4.Customer satisfaction level: Please start your responses with lowercase letters and avoid using capitals. Consider reading the transcript, thinking, and then determine the customer satisfaction level by providing answers in the format 'low', 'medium', or 'high'."
    ]

    for i in range(0, len(list_of_transactions)):
        """ the answer will be in a format of: transcript number: plus the format that
        was requested."""
        if i != 0:
            time.sleep(20)
            conversation = f"{list_of_transactions[i]}\n\n{prompt_questions[i]}"
            response = chat_gpt(conversation)
            print(f"Transcript {i + 1}:")
            print(response + "\n")
        else:
            conversation = f"{list_of_transactions[i]}\n\n{prompt_questions[i]}"
            response = chat_gpt(conversation)
            print(f"Transcript {i + 1}:")
            print(response + "\n")
