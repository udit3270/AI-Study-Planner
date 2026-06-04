import google.generativeai as genai

genai.configure(
    api_key="YOUR_GEMINI_API_KEY"
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

response = model.generate_content(
    "Say hello"
)

print(response.text)