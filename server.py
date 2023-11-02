from flask import Flask, request, jsonify
import openai
from flask_cors import CORS  # Import the CORS module
from dotenv import load_dotenv  # Import the load_dotenv function
import os  # Import the os module

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key:", openai.api_key)


app = Flask(__name__)


# Enable CORS for your app
CORS(app)

# Define the '/ask' endpoint for handling ChatGPT requests
@app.route('/ask', methods=['POST'])
def ask():
    try:
        question = request.json['question']

        # Make an API request to ChatGPT with a maximum of 100 tokens
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"You: {question}\nAI:",
            max_tokens=100  # Set maximum tokens to 100
        )
        response_text = response.choices[0].text
        print("Response Text:", response_text)

        if "You exceeded your current quota" in response.choices[0].text:
            return jsonify({'answer': 'Tokens expired'})
        
        answer = response.choices[0].text
        return jsonify({'answer': answer})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run()
