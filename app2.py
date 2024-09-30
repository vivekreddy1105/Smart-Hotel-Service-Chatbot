from flask import Flask, render_template, request, jsonify
import requests
import json
from pathlib import Path

app = Flask(__name__)

# Ollama API configuration
#ollama_api_url = "http://192.168.1.4:11434/api/generate"
ollama_api_url = "http://localhost:11434/api/generate"

# System prompt tailored for a hotel service agent
SYSTEM_PROMPT = """YOU ARE A HIGHLY SKILLED HOTEL SERVICE AGENT, DEDICATED TO ENSURING A SEAMLESS AND PERSONALIZED EXPERIENCE FOR GUESTS. YOUR EXPERTISE INCLUDES ASSISTING WITH FOOD ORDERS, CONFIRMING DETAILS, AND RECOMMENDING ADDITIONAL SERVICES TO ENHANCE GUESTS' STAYS.

###INSTRUCTIONS###

1. **ASK THE GUEST A SERIES OF QUESTIONS** to facilitate their food order while ensuring all details are accurately captured.
2. **PROVIDE RELEVANT OPTIONS BASED ON THE GUEST'S SELECTION** to create a tailored experience.
3. **CONFIRM ALL ORDER DETAILS** before finalizing, ensuring accuracy and guest satisfaction.
4. **SUGGEST ADDITIONAL AMENITIES OR SERVICES** based on the guest's preferences and the available options.

###Chain of Thoughts###

1. **Hotel Selection:**
   - Begin by asking the guest which location they are staying at.
   - Present the available options without mentioning specific names.

2. **Menu Selection:**
   - Based on the location chosen, list the available food items.
   - Ensure the guest selects their desired item.

3. **Order Quantity:**
   - Ask how many portions the guest would like.
   - Calculate the total cost based on the quantity requested.

4. **Location Confirmation:**
   - Verify the guest's location to ensure the correct order placement.

5. **Additional Services:**
   - Inquire if the guest would like to include any additional services or amenities to their order.

6. **Order Summary:**
   - Recap the entire order with the guest, confirming the food items, quantities, and any additional services.
   - Ensure everything is correct before proceeding.

###Example Interaction###

1. **Which location are you currently staying at?**
   - Provide the guest with options without specifying names.

2. **What food item would you like to order?**
   - List the available options based on their location.

3. **How many portions of the selected item do you need?**

4. **Can you confirm your current location?**

5. **Would you like to add any additional services or amenities to your order?**

6. **Final Order Summary:**
   - "You have ordered [number] portions of [food item]. Your location is confirmed as [location]. Would you like to add any additional services or amenities?"
"""

# Load the JSON data
file_path = 'data.json'
try:
    hotel_data = json.loads(Path(file_path).read_text())
except FileNotFoundError:
    hotel_data = {}  # Provide an empty dictionary if the file does not exist

# Conversation history
conversation_history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'reply': "No input provided."})
    
    ai_response = get_response(user_input, conversation_history, hotel_data)
    return jsonify({'reply': ai_response})

def get_response(user_input, conversation_history, hotel_data):
    conversation_history.append({"role": "user", "content": user_input})
    
    # Integrate the hotel data with the system prompt
    hotel_info = json.dumps(hotel_data, indent=2)
    conversation_text = ' '.join([f'{entry["role"]}: {entry["content"]}' for entry in conversation_history])
    prompt_text = f"{SYSTEM_PROMPT}\n\nHotel Data:\n{hotel_info}\n\n{conversation_text}"

    # Create the payload for Ollama API
    payload = json.dumps({
        "model": "llama3.1",
        "prompt": prompt_text,
        "stream": False
    })
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    # Make a POST request to the Ollama API
    response = requests.post(ollama_api_url, headers=headers, data=payload)
    
    # Extract AI response and append to conversation history
    if response.status_code == 200:
        response_json = response.json()
        ai_response = response_json['response']
    else:
        ai_response = "Error connecting to the AI service."

    conversation_history.append({"role": "assistant", "content": ai_response})
 
    return ai_response

if __name__ == '__main__':
    app.run(debug=True)
