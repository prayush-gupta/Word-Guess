# import functions

# game_result = functions.game_controller()


# from openai import OpenAI
# client = OpenAI(api_key='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')

# response = client.responses.create(
#     model="gpt-5.0",
#     input="What is ChatGPT?"
# )

# print(response.output_text)


import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)