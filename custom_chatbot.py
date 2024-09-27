# Install with: pip install google-generativeai
import google.generativeai as ai

# Set your API key
API_KEY = 'your-api-key'

# Configure the AI API
ai.configure(api_key=API_KEY)

# System instructions for the AI
instruction = "You are a book recommender. Suggest interesting books from different genres and themes, and always be friendly."

# Initialize the model
model = ai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instruction) 


# Start a chat session
chat = model.start_chat()

# Conversation loop
while True:
    message = input('You: ')
    if message.lower() == 'bye':
        print('Chatbot: Goodbye!')
        break
    response = chat.send_message(message)
    print('AI:', response.text)
    
