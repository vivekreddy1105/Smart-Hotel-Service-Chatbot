# Smart Hotel Service Chatbot

## Overview

The **Smart Hotel Service Chatbot** is an AI-powered assistant designed to enhance the guest experience in hotels by facilitating food orders and providing personalized recommendations. Utilizing advanced language models, this chatbot interacts with guests, captures their preferences, and assists them in placing food orders efficiently.

## Features

- **Personalized Interaction**: Engages with guests by asking a series of tailored questions to understand their preferences.
- **Food Ordering**: Allows guests to order food items based on their hotel location.
- **Dynamic Menu Options**: Presents relevant food options depending on the chosen hotel.
- **Order Confirmation**: Confirms order details to ensure accuracy and satisfaction.
- **Additional Services**: Suggests extra amenities or services based on guest preferences.
- **History Tracking**: Maintains conversation history to provide context and improve interactions.

## Technologies Used

- **Flask**: A lightweight web framework for building the chatbot application.
- **Ollama**: An AI model integration for generating responses.
- **HTML/CSS**: For the user interface.
- **JavaScript**: To handle asynchronous requests and enhance user interactions.

## Installation

### Prerequisites

- Python 3.x
- Flask
- Ollama installed on your local machine

### Steps to Set Up

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/smart-hotel-service-chatbot.git
   cd smart-hotel-service-chatbot
   ```

2. Install required Python packages:
   ```bash
   pip install flask requests
   ```

3. Ensure Ollama is running and accessible at `http://localhost:11434/api/generate`.

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the chatbot in your web browser at `http://localhost:5000`.

## Usage

- Open the application in your web browser.
- Start a conversation with the chatbot by providing your hotel location.
- Follow the prompts to place your food order and explore additional services.




