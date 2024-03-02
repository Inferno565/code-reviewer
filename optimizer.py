from openai import OpenAI

file_path = "test.py"

try:
    with open(file_path, "r") as file:
        file_data = file.read()  # Read the entire file into a string

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")


client = OpenAI()


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a code assistant, skilled with complex programming concepts, analyzes the provided code and provides the user with optimized version of the code to improve its quality",
        },
        {
            "role": "user",
            "content": f"write an optimized code for the given file: \n{file_data}",
        },
    ],
)

print(completion.choices[0].message.content)
