import os
import requests
from flask import Flask, request, jsonify
import PyPDF2
import io

app = Flask(__name__)

def download_pdf(url):
    """
    Download PDF from a given URL
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return io.BytesIO(response.content)
    except requests.RequestException as e:
        print(f"Error downloading PDF: {e}")
        return None

def extract_pdf_text(pdf_stream):
    """
    Extract text from PDF stream
    """
    try:
        reader = PyPDF2.PdfReader(pdf_stream)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error extracting PDF text: {e}")
        return None

@app.route('/', methods=['POST'])
def parse_pdf():
    """
    Parse PDF from URL and return extracted text
    """
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({"error": "URL is required"}), 400
    
    pdf_url = data['url']
    
    # Download PDF
    pdf_stream = download_pdf(pdf_url)
    if not pdf_stream:
        return jsonify({"error": "Could not download PDF"}), 400
    
    # Extract text
    extracted_text = extract_pdf_text(pdf_stream)
    if not extracted_text:
        return jsonify({"error": "Could not extract text from PDF"}), 400
    
    return jsonify({
        "text": extracted_text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 