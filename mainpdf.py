import openai
import PyPDF2

# Set your OpenAI API key
openai.api_key = "****************************"

# Function to read text from a PDF file
def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

# Function to chat with GPT-3 model
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    pdf_file_path = input("Please provide the path to the PDF file: ")
    try:
        pdf_text = read_pdf(pdf_file_path)
        print("PDF read successfully.")

        while True:
            user_question = input("Your question (type 'exit' to quit): ")
            if user_question.lower() == "exit":
                break

            response = chat_with_gpt(pdf_text + " " + user_question)
            print("Chatbot:", response)
    except FileNotFoundError:
        print("File not found. Please provide a valid path.")