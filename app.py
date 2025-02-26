import os
import requests
from flask import Flask, request, jsonify
import PyPDF2
import tempfile

app = Flask(__name__)

def download_pdf(url):
    """
    Download PDF from a given URL
    
    Args:
        url (str): URL of the PDF file
    
    Returns:
        str: Path to the downloaded PDF file
    """
    try:
        # Send a GET request to download the PDF
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Create a temporary file to save the PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
            for chunk in response.iter_content(chunk_size=8192):
                temp_file.write(chunk)
            temp_file_path = temp_file.name
        
        return temp_file_path
    
    except requests.RequestException as e:
        raise Exception(f"Error downloading PDF: {e}")

def extract_pdf_text(pdf_path):
    """
    Extract text content from a PDF file
    
    Args:
        pdf_path (str): Path to the PDF file
    
    Returns:
        dict: Extracted text for each page
    """
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Extract text from each page
            pages_text = {}
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                pages_text[f"page_{page_num + 1}"] = text
            
            return {
                "total_pages": len(pdf_reader.pages),
                "content": pages_text
            }
    
    except Exception as e:
        raise Exception(f"Error extracting PDF text: {e}")
    finally:
        # Clean up the temporary file
        if 'pdf_path' in locals():
            os.unlink(pdf_path)

@app.route('/parse-pdf', methods=['POST'])
def parse_pdf():
    """
    API endpoint to parse PDF from a URL
    
    Expected JSON payload:
    {
        "url": "https://example.com/sample.pdf"
    }
    """
    try:
        # Get PDF URL from request
        data = request.get_json()
        pdf_url = data.get('url')
        
        if not pdf_url:
            return jsonify({"error": "PDF URL is required"}), 400
        
        # Download PDF
        pdf_path = download_pdf(pdf_url)
        
        # Extract text
        pdf_content = extract_pdf_text(pdf_path)
        
        return jsonify(pdf_content), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 