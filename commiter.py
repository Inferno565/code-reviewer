from hugchat import hugchat
from hugchat.login import Login


sign = Login("Inferno565", "P@rs9gt3")
cookies = sign.login()

cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
id = chatbot.new_conversation()
chatbot.change_conversation(id)
file_path = "test.py"  # Specify the path to your file

try:
    with open(file_path, "r") as file:
        file_data = file.read()  # Read the entire file into a string
        # print("File data read successfully:")
        # print(file_data)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# str1 = f"generate a commit message in 100 characters for the following code: {file_data}"
str1 = f"what is your LLM?"
output = str(chatbot.chat(str1))
final = output.split('\n')[0].lstrip().split('(')[0]
print(final)
# print(f)
