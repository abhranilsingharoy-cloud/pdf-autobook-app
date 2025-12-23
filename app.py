import os
import fitz  # PyMuPDF
from flask import Flask, render_template, request, send_file
from gtts import gTTS
import io

app = Flask(__name__)
app.secret_key = "super_secret_key"

def extract_text(pdf_stream):
    """Extracts text from the uploaded PDF file stream."""
    try:
        doc = fitz.open(stream=pdf_stream.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        return text
    except Exception as e:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if file is uploaded
        if 'pdf_file' not in request.files:
            return render_template('index.html', error="No file uploaded")
        
        file = request.files['pdf_file']
        
        if file.filename == '':
            return render_template('index.html', error="No file selected")

        if file:
            # 1. Extract Text
            text = extract_text(file)
            
            if not text or not text.strip():
                return render_template('index.html', error="Could not extract text. The PDF might be scanned/image-based.")

            # 2. Get Settings from Form
            lang = request.form.get('language', 'en')
            speed = request.form.get('speed', 'normal')
            is_slow = True if speed == 'slow' else False

            # 3. Convert to Audio (gTTS)
            try:
                tts = gTTS(text=text, lang=lang, slow=is_slow)
                
                # Save to memory buffer instead of disk to keep it fast
                mp3_fp = io.BytesIO()
                tts.write_to_fp(mp3_fp)
                mp3_fp.seek(0)
                
                return send_file(
                    mp3_fp,
                    mimetype="audio/mpeg",
                    as_attachment=True,
                    download_name=f"{file.filename.replace('.pdf', '')}.mp3"
                )
            except Exception as e:
                return render_template('index.html', error=f"Conversion failed: {str(e)}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
