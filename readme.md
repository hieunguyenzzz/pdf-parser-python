# PDF Content Extraction API

## Overview
This is a Flask-based microservice that allows you to extract text content from PDF files hosted at a given URL.

## how to run

1. clone the repository
2. run `docker build -t pdf-extractor .`
3. run `docker run -p 5000:5000 pdf-extractor`
4. test the api using 
```
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com/your-pdf-file.pdf"}' http://localhost:5000/parse-pdf
```

