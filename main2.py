import openai

openai.api_key = "***********************"

messages = []
prompt = input("Please provide a prompt for the conversation:\n")
system_msg = input("What instructions would you like to give to the chatbot?\n")
messages.append({"role": "system", "content": system_msg})
messages.append({"role": "system", "content": prompt})

while True:
    message = input("press enter to start: ")
    if message.lower() == "quit()":
        break
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("Assistant:", reply)
