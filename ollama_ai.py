# 1. Download Ollama from https://ollama.com/
# 2. Install Ollama: pip install ollama
# 3. Run Ollama: ollama pull llama3.1 && ollama run llama3.1:8b
# 4. Start Chatbot:

import ollama

while True:
    user = input('You: ')  # Get input from the user
    if user.lower() == 'bye':  # Check if the user wants to end the conversation
        print('Goodbye!')  # Print a goodbye message
        break  # Exit the loop

    # Send the user's message to the Ollama chatbot and get the response
    response = ollama.chat(model='llama3.1', messages=[
        {'role': 'user', 'content': user}
    ])

    # Print the chatbot's response
    print('Chatbot:', response['message']['content']) 
