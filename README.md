Code God - ChatGPT Powered Q&A Web Application
Welcome to Code God, a web application that uses OpenAI's ChatGPT to answer your coding questions. This README will guide you through the installation and setup process.

### Prerequisites
Before you get started, make sure you have the following prerequisites installed on your system:

Python 3.x: Download Python
Flask: Install Flask using pip with pip install Flask
Flask-CORS: Install Flask-CORS using pip with pip install flask-cors
OpenAI Python Library: Install OpenAI Python library using pip with pip install openai
OpenAI API Key: Sign up for an OpenAI account and create an API key.
Installation
Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/code-god.git
cd code-god
```
Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install project dependencies:
```

```bash
pip install -r requirements.txt
API Key Configuration
Create a .env file in the project root directory.
```

Open the .env file and add your OpenAI API key like this:

```makefile
OPENAI_API_KEY=your-api-key-here
Replace your-api-key-here with your actual OpenAI API key.
```

### Starting the Local Server
Run the Flask application using the following command:

```bash
python server.py
```
This will start the server on your local machine.

By default, the server will run on http://127.0.0.1:5000/. You can access the Code God web application by opening your web browser and navigating to http://127.0.0.1:5000/.

### How to Use

Visit the Code God web application in your browser at http://127.0.0.1:5000/.

You'll see a text input field where you can type your coding questions.

Press the "Enter" key, and the application will send your question to the server, which will use the OpenAI API to generate an answer.

The answer will be displayed on the right side of the screen.

If you encounter any issues or errors, the application will display error messages to help you diagnose and resolve the problem.

### Deploying to Production
If you want to deploy this application to a production server, consider using a web server like Nginx or Apache in combination with a production-ready web application server like Gunicorn.

### Security Note
Do not share your OpenAI API key or sensitive information in your public repository. Always keep your API keys and secret information secure.
