# Install with: pip install google-generativeai
import google.generativeai as ai

# API Key
API_KEY = 'your-api-key'

# Configure the API
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()

# Initialize conversation history
history = []

# Start a conversation
while True:
    message = input('You: ')
    if message.lower() == 'bye':
        print('Chatbot: Goodbye!')
        break

    # Add user message to conversation history
    history.append(f"User: {message}")

    # Send the full conversation history to the model
    response = chat.send_message('\n'.join(history))

    # Add AI response to conversation history
    history.append(f"Chatbot: {response.text}")

    print(f'Chatbot: {response.text}')
    
