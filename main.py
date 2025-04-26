from ollama import chat
from ollama import ChatResponse


with open('test.txt', 'r') as file:
    prompt = file.read()
# response: Chatresponse is a "type annotation," meaning that I am saying
# the "response" variable should hold data of the "ChatResponse" type
# we are using chat() function to generate a response and hold it in response variable
response: ChatResponse = chat(model='llama3.2', messages=[ #passes list of dictionaries
  {
    'role': 'user',
    'content': 'Why is the sky blue?', #this is the actual question the model will respond to. we
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)