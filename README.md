# ezzybooksAI

ezzybooksAI is an AI-powered application designed to summarize content from PDF files, making it easier to extract key information from extensive documents.

This is built for the ezzybookAI website (coming soon), but you can also use it separately.

## Features

- **PDF and DOCX Summarization**: Upload your PDF or DOCX files, and the AI will generate concise summaries highlighting the main points.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Rohithgg/ezzybooksAI.git
   ```


2. **Navigate to the Project Directory**:

   ```bash
   cd ezzybooksAI
   ```


3. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```


4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```


## Usage

1. **Run the Application**:

   ```bash
   python main.py
   ```


2. **Access the Web Interface**:

   Open your web browser and navigate to `http://127.0.0.1:5000`.

3. **Upload a Document**:

   - Click on the "Upload" button and select a PDF or DOCX file.

4. **View Summary**:

   - After uploading, the application will process the document and display a summary.

## Testing

To test the application's functionality, you can use the provided `test_main.http` file with an HTTP client like [HTTPie](https://httpie.io/) or [Postman](https://www.postman.com/).

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the open-source community for providing the tools and libraries that made this project possible. 
