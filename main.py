from pdf_processing import pdfplumber_extraction
import requests

API_KEY_VALUE = "YOUR_API_KEY_VALUE"
API_URL = "YOUR_API_URL_VALUE"

def ask_question(question, context):
    headers = {
        "Authorization": f"Bearer {API_KEY_VALUE}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [
            {
                "role": "system",
                "content": f"Answer questions based on this document. If unsure, say 'I don't know'.\nDocument: {context}"
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "temperature": 0.2
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.text}"


def main():
    pdf_file = "table_pdf.pdf"
    doc_content = pdfplumber_extraction(pdf_file)

    print("Document Q&A System")
    print("Enter 'exit' to quit")

    while True:
        user_input = input("\nYour question: ")
        if user_input.lower() == 'exit':
            break

        response = ask_question(user_input, doc_content)
        print("\nAssistant:", response)
    print(response)

if __name__ == "__main__":
    main()