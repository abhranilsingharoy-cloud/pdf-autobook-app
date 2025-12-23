# 🎧 AudioFlow - PDF to Audiobook Converter

**AudioFlow** is a modern web application that converts PDF documents into spoken audiobooks using Python. It features a clean, professional user interface and allows users to customize the voice language and reading speed.

## 🚀 Features

* **PDF Text Extraction:** Robust extraction using `PyMuPDF` (supports complex layouts).
* **Text-to-Speech:** High-quality audio generation using Google Text-to-Speech (`gTTS`).
* **Custom Settings:** Choose from multiple languages (English, Hindi, Spanish, French) and adjust reading speed.
* **Instant Download:** Automatically generates and downloads the MP3 file upon conversion.
* **Professional UI:** Responsive design built with HTML5, CSS3, and Flask.

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask
* **Libraries:**
    * `PyMuPDF` (fitz) - For parsing PDF files.
    * `gTTS` (Google Text-to-Speech) - For audio conversion.
* **Frontend:** HTML5, CSS3 (Custom styling)

## 📂 Project Structure

```text
PDF_Audiobook_App/
│
├── app.py                  # Main Flask application logic
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
├── static/
│   └── style.css           # CSS styling for the frontend
└── templates/
    └── index.html          # HTML template for the user interface

 ##⚙️ Installation & Setup
Follow these steps to run the project locally on your machine.

1. Clone the Repository
git clone [https://github.com/your-username/AudioFlow.git](https://github.com/your-username/AudioFlow.git)
cd AudioFlow
2. Create a Virtual Environment (Optional but Recommended)
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install flask pymupdf gTTS
4. Run the Application
python app.py
4. Run the Application
python app.py
5. Access the Web App
Open your web browser and navigate to: http://127.0.0.1:5000/

📖 Usage Guide
Upload PDF: Click the upload box or drag and drop your PDF file.

Select Language: Choose your preferred language for the audio (e.g., English, Hindi).

Select Speed: Choose between "Normal" or "Slow" reading speeds.

Convert: Click the "Generate Audiobook" button.

Listen: The MP3 file will download automatically once processing is complete.

🛡️ Limitations
Scanned PDFs: The current version relies on text extraction. It may not work well with scanned images or PDFs containing only pictures (OCR is not currently implemented).

File Size: Extremely large PDFs may take longer to process depending on internet speed (as gTTS requires an API connection).

🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

