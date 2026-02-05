from google import genai


def ask_for_hint(keyword):

  print('Asking for a hint, please wait...')

  client = genai.Client()

  response = client.models.generate_content(
      model="gemini-3-flash-preview",
      contents="Generate a small hint to help identify the keyword: "+keyword,
  )

  return(response.text)