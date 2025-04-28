
# Importing the required library (ollama)
import ollama

# Setting up the model, enabling streaming responses, and defining the input messages
ollama_response = ollama.chat(model='llama3.2', messages=[
   {
     'role': 'system',
     'content': 'You are a helpful assistant with sound philosophical knowledge.',
   },
   {
     'role': 'user',
     'content': 'Explain to me the meaning of life?',
   }],

   options =
   {
       'temperature': 1.5 #supposedly acts as a creativity meter (from 0-1)
   }
)
# Printing out of the generated response
print(ollama_response['message']['content'])
