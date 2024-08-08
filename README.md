# AI Enhanced Content Generation for University Courses

This project leverages the Gemini API Model Pro 1.5 and the LangChain framework to generate precise, original, and plagiarism-free summaries of university course materials. By processing PDFs of students' syllabi and other relevant documents, the system produces concise and accurate summaries that enhance the learning experience.

## Project Overview

The AI Enhanced Content Generation system utilizes advanced AI models to analyze course content and produce high-quality summaries. This project aims to assist both students and educators by providing well-organized, easy-to-understand summaries of academic materials.

## Key Components

- **Gemini API Model Pro 1.5**: The core AI model used for processing and summarizing the content. This model is adept at understanding and generating text based on the provided documents.
- **LangChain Framework**: A powerful framework that facilitates the interaction between the AI model and the content generation processes. It enables smooth integration and efficient handling of the summarization tasks.

## How It Works

1. **Data Input**:
   - Upload PDF files containing students' syllabi and other course-related documents.
   - The system supports multiple document types and formats to ensure versatility.

2. **Content Processing**:
   - The Gemini API Model Pro 1.5 analyzes the input PDFs to extract relevant content.
   - LangChain orchestrates the interaction between the AI model and the document data, ensuring accurate and contextually relevant summaries.

3. **Content Generation**:
   - The AI model generates summaries that are concise, original, and free from plagiarism.
   - Summaries are tailored to reflect the key concepts and details from the provided syllabi and documents.

4. **Output**:
   - The generated summaries are presented in an easily accessible format.
   - Users can review and utilize these summaries for educational purposes, enhancing both teaching and learning experiences.
  
## Workflow

![Workflow Diagram](https://github.com/Pavun-KumarCH/Langchain-Llamaindex-integration-with-Gemeni-API/blob/main/assets/flow1.png)

![Workflow Diagram](https://github.com/Pavun-KumarCH/Langchain-Llamaindex-integration-with-Gemeni-API/blob/main/assets/DBBLOG-3334-image001.png)


## Getting Started

To set up and run the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pavun-KumarCH/Langchain-Llamaindex-integration-with-Gemeni-API.git
2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
3. **Run the Application:**
   ```
   python app.py
4. **Upload Your PDFs:**
   - Access the application through your browser or terminal interface.
   -  Upload the course PDFs to generate summaries.

## Upload Your PDFs

Access the application through your browser or terminal interface. Upload the course PDFs to generate summaries.

## Documentation

### Phase 1 - Interactive PDF Processing
> Corresponding notebook: [Interactive-PDF-Processing.ipynb](https://github.com/Pavun-KumarCH/Langchain-Llamaindex-integration-with-Gemeni-API/blob/main/Notebooks/Lang_Chain.ipynb)

Implemented tasks:
- **Upload PDFs**: Create an interface for users to upload multiple PDF documents.
- **Extract Text**: Read and extract text content from the uploaded PDFs.
- **Display Results**: Show extracted text and user queries in a user-friendly format.

### Phase 2 - Text Chunking and Vector Store Creation
> Corresponding notebook: [Text-Chunks-Vector-Store.ipynb](https://github.com/Pavun-KumarCH/Langchain-Llamaindex-integration-with-Gemeni-API/blob/main/Notebooks/Lang_Chain.ipynb)

Implemented tasks:
- **Split Text**: Break down the extracted text into manageable chunks.
- **Create Embeddings**: Convert text chunks into vector embeddings using Google Generative AI.
- **Build Vector Store**: Store these embeddings in a vector store for efficient similarity searches.

### Phase 3 - Conversational QA System
> Corresponding notebook: [Conversational-QA-System.ipynb](https://github.com/Pavun-KumarCH/Langchain-Llamaindex-integration-with-Gemeni-API/blob/main/Notebooks/Lang_Chain.ipynb)

Implemented tasks:
- **Setup QA Chain**: Configure a question-answering chain with a conversational AI model.
- **Process Queries**: Use the QA system to answer user questions based on the processed text.
- **Display Responses**: Show generated responses and relevant text snippets in a user-friendly format.

### Project Overview Live Preview 
![Project Showcase](https://github.com/Pavun-KumarCH/Langchain-Llamaindex-integration-with-Gemeni-API/blob/main/assets/showcase.gif)

## Future Enhancements

- **Expand Document Support**: Integrate additional file formats and types for broader applicability.
- **Improve Summary Quality**: Enhance summarization algorithms for more precise content generation.
- **User Interface**: Develop a more intuitive user interface for easier interaction.

## Contributing

Feel free to contribute to this project by submitting issues, suggesting improvements, or making pull requests. For detailed contributing guidelines, refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
