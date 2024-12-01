from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
import nltk



# intialiaze chat bot
boyfriend = ChatBot(
    "BoyfriendBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "*Blinded for his love for you* What was that?", # change this, default phrase when the chatbot does not understand
            "maximum_similarity_threshold": 0.90,
        }
    ],
    database_uri="sqlite:///database.sqlite3"
)


print("BoyfriendBot: Hi! I'm here for you. Type 'exit' to quit.") # change this to something better

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit': # type exit to quit
#         print("BoyfriendBot: Bye! Take care. ❤️")
#         break
#     response = boyfriend.get_response(user_input)
#     print(f"BoyfriendBot: {response}")


# Create the Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    bot_response = boyfriend.get_response(user_message)
    return jsonify({"response": str(bot_response)})

if __name__ == "__main__":
    app.run(debug=True)