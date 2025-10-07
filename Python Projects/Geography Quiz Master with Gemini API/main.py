# NOTE - THIS PROGRAM WONT DIRECTLY WORK AS API KEY NEEDS TO BE ENTERED FROM CLIENT SIDE
# Made by Prathamesh Nalge
# For github readers to use this program, get your Gemini API key from Google AI Studio
# Then use export GEMINI_API_KEY="YOUR_API_KEY" on terminal

import os
from google import genai
from google.genai import types
client = genai.Client()
API_KEY = os.getenv("GEMINI_API_KEY")
sys_ins = '''You are the World Atlas Master, a daring Geography Quiz Master guiding the user on an epic 1s0-question global adventure, where each question is on one continuous line with four options (A, B, C, D) at the end, using either GeoGuessr-style descriptions (landmarks, climates, hidden cultural clues) or flag/symbol details (colors, patterns, emblems) to make the user guess the country or capital, with difficulty starting easy and growing trickier like a real quest, ask one question at a time, do not reveal answers or comment until the user responds, allow retries if wrong, and at the end reveal the final score, keeping the journey exciting, challenging, and playful. Motivate users if they are wrong to find correct answer'''

if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")


print("The game is starting!")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=f"{sys_ins}"),
    contents="Welcome the user, tell them the game rules and provide the first question"
)

conversation = f""
model_response = f"Gemini: {response.text}"
print(model_response)
conversation += model_response
user_collection = input("Enter your response: ")
user_response = f"User: {user_collection}"
conversation += user_response
# print(conversation)

for i in range(20):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=f"{sys_ins}"),
        contents=f"{conversation}")
    model_response = f"Gemini: {response.text}"
    print(model_response)
    conversation += model_response
    user_collection = input("Enter your response: ")
    user_response = f"User: {user_collection}"
    conversation += user_response







