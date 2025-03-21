import pandas as pd
from googletrans import Translator
import json
import time  # To add a delay between requests
import random  # To introduce variability in delays

# Load the dataset
df = pd.read_csv('Conversation.csv')

# Initialize the translator
translator = Translator()

# Function to translate text
def translate_text(text, target_language="ro"):
    if not text:  # Check if the text is empty or None
        return ""  # Return empty string if there's no text to translate
    
    try:
        translated = translator.translate(text, src='en', dest=target_language)
        return translated.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return ""  # Return empty string in case of error

# Create a list to store the translated conversations
translated_conversations = []

# Loop through each row in the dataframe
for index, row in df.iterrows():
    # Extracting question and answer
    question = row.get('question', '')
    answer = row.get('answer', '')
    
    # Translate the question and answer
    question_ro = translate_text(question, 'ro')
    answer_ro = translate_text(answer, 'ro')
    
    # Add the translated conversation to the list
    translated_conversations.append({
        "question_ro": question_ro,
        "answer_ro": answer_ro
    })
    
    # Add a random delay between requests to avoid rate-limiting
    time.sleep(random.uniform(1, 3))  # Sleep between 0.5 to 2 seconds

# Save the translated conversations to a JSON file
with open('Conversation_romanian.json', 'w', encoding='utf-8') as f:
    json.dump(translated_conversations, f, ensure_ascii=False, indent=4)

print("Translated conversations have been saved to 'Conversation_romanian.json'")
