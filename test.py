import openai
openai.api_key = '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'

prompt = "Say hi"
response = openai.Completion.create(
    engine='text-davinci-002',
    prompt=prompt,
    temperature=0.7,
    max_tokens=100
)
generated_text = response.choices[0].text.strip()

print("\nGenerated Text:", generated_text)
