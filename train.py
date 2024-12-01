from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk


nltk.download('punkt')

# create chat bot
boyfriend = ChatBot(
    "BoyfriendBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3"
)
def training():
    # Train the ChatBot
    trainer = ChatterBotCorpusTrainer(boyfriend)

    # Train the Chatbot on English Corpus
    trainer.train("chatterbot.corpus.english")

    # Custom Training Data 
    custom_conversations = [ #chatbot response | user typically response
        "I'm doing great!How about you?| Hi, how are you?" , # add more, more stuff
        "I love you too!|I love you.",
        "Let's go for a walk or watch a movie together.|What should we do today?",
        "Thank you! You're amazing too.|You're so sweet.",
        "Goodnight! Sweet dreams.|Goodnight.",
        "Amazing! Now that you're here.|How's your day? ",
    ]

    # Prepare custom data for training using | as the delimeter above
    for conversation in custom_conversations:
        statement, response = conversation.split("|")
        boyfriend.storage.create(text=statement, in_response_to=response)
    print('Training done!')
if __name__ == "__main__":
    training()