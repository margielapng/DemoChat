from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import openai

openai.api_key = "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"

class QueryDatabaseAction(Action):
    def name(self):
        return "action_query_database"

    def run(self, dispatcher, tracker, domain):
        # Extract user query
        user_query = tracker.latest_message.get("text")

        # Perform database query based on user input (implement this logic)
        database_response = self.query_database(user_query)

        # Use GPT-3.5-turbo to generate a response
        gpt_response = self.generate_gpt_response(user_query)

        # Combine responses
        final_response = f"From the database: {database_response}\n\nAI-driven response: {gpt_response}"

        # Send the response back to the user
        dispatcher.utter_message(final_response)

        return [SlotSet("user_query", user_query)]

    def query_database(self, user_query):
        # Implement logic to query your database based on user input
        # ...

        # For example, return a placeholder response
        return "Data from the database related to user query"

    def generate_gpt_response(self, user_query):
        # Call OpenAI GPT-3.5-turbo to generate a response
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f"User query: {user_query}\nAI, generate a detailed response:",
            temperature=0.7,
            max_tokens=150
        )

        # Extract and return the AI-generated response
        return response["choices"][0]["text"]
