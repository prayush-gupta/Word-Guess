import requests
import random
import pandas as pd

url = "https://random-words-api.kushcreates.com/api")

df = pd.read_json(url)

df['length_str'] = df['length'].astype(str)
df['sql_output'] = "('" + df['word'] + "', '" + df['length_str'] + "', '" + df['category'] + "', '" + df['language'] + "'),"

df['sql_output'].to_clipboard(index=False, header=False)