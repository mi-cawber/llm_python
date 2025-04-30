import random #this will allow us to generate random numbers
from ollama import chat
from ollama import ChatResponse

def generate_phrase():
  #reads in text file
  with open('phrase_bank.txt', 'r') as file: #returns file object and assigns it to "file" variable
      phrases = file.read()

  # creating the prompt environment using chat()
  response: ChatResponse = chat(model='llama3.2', messages=[ #passes list of dictionaries
    {
       'role': 'system',
       'content': '''You are a very careful assistant which pays close attention to user prompts
       and executes details precisely.'''
    },
    {
      'role': 'user',
      # prompt
      'content': f'''In the game Elder Scrolls IV: Oblivion, you are presented with a motiviational phrase upon leveling up. 
      The text file attached to this prompt contains all of the motivational phrases in the game. I want you to generate 10
      additional phrases that capture the same style and tone as the ones found in Oblivion. For ease of data manipulation,
      your output for this prompt should only include the phrases themselves. Do not number the phrases. Do not put hyphens
      before the phrases. Do not put any other explanatory sentences. Just only put new phrases. Here are the phrases: {phrases}'''
    },
  ])

  # 'a' to append to existing content
  with open('phrase_bank.txt', 'a') as file:
      model_response = file.write(response.message.content + '\n')

# this is a function to print a random phrase from the file
def print_phrase():

  # this reads the file and assigns the contents to lines variable
  with open('phrase_bank.txt', 'r') as file:
    lines = file.readlines()
  
  random_number = random.randint(0, len(lines))
  
  print(lines[random_number])
