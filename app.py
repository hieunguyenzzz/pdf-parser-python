import os
import requests
from flask import Flask, request, jsonify
import PyPDF2
import io
import docx
import mimetypes
from urllib.parse import urlparse, parse_qs
import re

app = Flask(__name__)

def convert_google_drive_url(url):
    """
    Convert Google Drive sharing URL to direct download link
    """
    # Check if it's a Google Drive URL
    if 'drive.google.com' in url:
        # Extract file ID from the URL
        match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
        if match:
            file_id = match.group(1)
            # Construct direct download link
            return f'https://drive.google.com/uc?export=download&id={file_id}'
    return url

def download_document(url):
    """
    Download document from a given URL
    """
    try:
        # Convert Google Drive URL if necessary
        original_url = url
        url = convert_google_drive_url(url)
        
        print(f"Downloading from URL: {url} (original: {original_url})")
        
        # Add headers to mimic browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10, stream=True)
        response.raise_for_status()
        
        content_type = response.headers.get('Content-Type')
        print(f"Content-Type received: {content_type}")
        
        return io.BytesIO(response.content), content_type
    except requests.RequestException as e:
        print(f"Error downloading document: {e}")
        return None, None

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

def extract_docx_text(docx_stream):
    """
    Extract text from DOCX stream
    """
    try:
        doc = docx.Document(docx_stream)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        print(f"Error extracting DOCX text: {e}")
        return None

def detect_document_type(url, content_type=None):
    """
    Detect document type from URL or content type
    """
    # Special case for Google Drive URLs
    if 'drive.google.com' in url:
        # Default to PDF for Google Drive links unless we can determine otherwise
        return 'pdf'
    
    # Try to determine from URL extension
    path = urlparse(url).path.lower()
    if path.endswith('.pdf'):
        return 'pdf'
    elif path.endswith('.docx'):
        return 'docx'
    
    # Try to determine from content type
    if content_type:
        if 'pdf' in content_type.lower() or 'application/octet-stream' in content_type.lower():
            return 'pdf'
        elif 'docx' in content_type.lower() or 'document' in content_type.lower():
            return 'docx'
    
    # Default to unknown
    return 'unknown'

@app.route('/', methods=['POST'])
def parse_document():
    """
    Parse document from URL and return extracted text
    """
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({"error": "URL is required"}), 400
    
    document_url = data['url']
    
    # Download document
    document_stream, content_type = download_document(document_url)
    if not document_stream:
        return jsonify({"error": "Could not download document"}), 400
    
    # Detect document type
    document_type = detect_document_type(document_url, content_type)
    
    # Extract text based on document type
    extracted_text = None
    if document_type == 'pdf':
        extracted_text = extract_pdf_text(document_stream)
    elif document_type == 'docx':
        extracted_text = extract_docx_text(document_stream)
    else:
        return jsonify({"error": "Unsupported document type"}), 400
    
    if not extracted_text:
        return jsonify({"error": f"Could not extract text from {document_type.upper()} document"}), 400
    
    return jsonify({
        "text": extracted_text,
        "document_type": document_type,
        "source_url": document_url
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 