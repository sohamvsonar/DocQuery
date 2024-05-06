# DocQuery is a PDF Chat Application with LangChain

### This project demonstrates how to use LangChain to create an application that allows users to chat with PDFs. Users can upload a PDF file and then ask questions about the content of the PDF. The application will use LangChain to search the PDF for relevant information and then generate a response.

## Features
- PDF Upload: Users can upload a PDF file containing text.
- Chat Interface: Users can interact with the application through a chat inerface.
- Question Answering: The application uses LangChain to answer questions based on the content of the uploaded PDF.
- Error Handling: Comprehensive error handling to provide users with clear feedback in case of any issues.

## Screenshots

![](https://github.com/sohamvsonar/DocQuery/blob/main/SS1.jpg)

![](https://github.com/sohamvsonar/DocQuery/blob/main/SS2.jpg)

## Installation

1. Clone the repository:
    git clone https://github.com/sohamvsonar/DocQuery.git

2. Install the required dependencies:
    ```bash
    pip install langchain streamlit PyPDF2 FAISS

3. Google Palm API Key.
#### This project uses the Google Palm API for language processing. To use the Google Palm API, you'll need to obtain an API key from   the Google Cloud Console. Once you have the API key, Replace "your_google_api_key" with your actual Google API key.

## Usage

1. Run the application.
    ```bash
    streamlit run your_app.py

2. Access the application in your web browser at http://localhost:8501.

3. Upload a PDF file and start asking questions about its content.

## Contributing
### Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/new-feature).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature/new-feature).
6. Create a new pull request.

## Contact
- For any inquiries or support, please contact at soham.sonar427@gmail.com.
- You can connect with me on linkedIn @ https://www.linkedin.com/in/sohamsonar23/
