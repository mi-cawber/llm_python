from ollama import chat
from ollama import ChatResponse

def generate_phrase():
  #reads in text file
  with open('phrase_bank.txt', 'r') as file:
      phrases = file.read()

  # creating the prompt environment using chat()
  response: ChatResponse = chat(model='llama3.2', messages=[ #passes list of dictionaries
    {
      'role': 'user',
      # prompt
      'content': f'''In the game Elder Scrolls IV: Oblivion, you are presented with a motiviational phrase upon leveling up. 
      The text file attached to this prompt contains all of the motivational phrases in the game. I want you to generate 10
      additional phrases that capture the same style and tone as the ones found in Oblivion. For ease of data manipulation,
      your output for this prompt should only include the phrases themselves. Do not number the phrases. Do not put hyphens
      before the phrases Here are the phrases: {phrases}'''
    },
  ])

  # 'a' to append to existing content
  with open('phrase_bank.txt', 'a') as file:
      model_response = file.write(response.message.content + '\n')