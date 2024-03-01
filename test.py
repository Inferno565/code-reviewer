import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

# Example prompt for text generation
prompt = "Translate the following English text to French: 'Hello, how are you?'"

# Call the OpenAI API for text generation (GPT-3)
response = openai.Completion.create(
    engine="text-davinci-002",  # You can choose the engine you want to use
    prompt=prompt,
    temperature=0.7,
    max_tokens=100
)

# Get the generated text from the API response
generated_text = response.choices[0].text.strip()

# Print the generated text
print("Generated Text:", generated_text)
