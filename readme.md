# Document Content Extraction API

## Overview
This is a Flask-based microservice that allows you to extract text content from PDF and DOCX files hosted at a given URL.

## How to Run

1. Clone the repository
2. Run `docker build -t document-extractor .`
3. Run `docker run -p 5000:5000 document-extractor`
4. Test the API using one of the following curl commands:

### PDF Parsing Example
```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://files.merakiweddingplanner.com/1740543229185-22834be1-0c49-4be5-8579-f1d473f48d7d-CV_Wedding_Planner_Assistant__a__ng_Thanh_Tra_n.pdf"}' http://localhost:5000
```

### DOCX Parsing Example
```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://file-examples.com/storage/fe5c8a4a6c9c9c/2017/04/file_example_DOCX_5MB.docx"}' http://localhost:5000
```

### Google Drive PDF Parsing Example
```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://drive.google.com/file/d/1K5E4SVOo6Aox4m8ST0x_h_Jt2LBfgzDU/view"}' http://localhost:5000
```

### Response Format
The API returns a JSON response with two key fields:
- `text`: The extracted text content of the document
- `document_type`: The type of document parsed (either 'pdf' or 'docx')

Example Response:
```json
{
    "text": "Document content extracted here...",
    "document_type": "pdf"
}
```

## Supported Document Types
- PDF (.pdf)
- DOCX (.docx)

## Notes
- Ensure the document URL is publicly accessible
- The API supports documents up to a reasonable size limit
- File type is detected by file extension or content type

## how to run

1. clone the repository
2. run `docker build -t pdf-extractor .`
3. run `docker run -p 5000:5000 pdf-extractor`
4. test the api using 
```
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://files.merakiweddingplanner.com/1740543229185-22834be1-0c49-4be5-8579-f1d473f48d7d-CV_Wedding_Planner_Assistant__a__ng_Thanh_Tra_n.pdf"}' http://localhost:5000
```

the response looks like this:
```
{"text":"\u0110\u1eb6NG THANH TR\u00c2N\n+84 902 545 319\ndangthanhtran.164@gmail.com16/04/2001\nTh\u00e0nh ph\u1ed1 H\u1ed3 Ch\u00ed Minh\nKINH NGHI\u1ec6M\n10/2022 - 01/2023\nT\u00ecm ki\u1ebfm ngu\u1ed3n kh\u00e1ch h\u00e0ng ti\u1ec1m n\u0103ng.\nT\u01b0 V\u1ea5n, thuy\u1ebft ph\u1ee5c kh\u00e1ch h\u00e0ng s\u1eed d\u1ee5ng s\u1ea3n ph\u1ea9m t\u00edn d\u1ee5ng\nc\u1ee7a ng\u00e2n h\u00e0ng.\nH\u1ed7 tr\u1ee3, ho\u00e0n thi\u1ec7n h\u1ed3 s\u01a1 vay th\u1ec3 ch\u1ea5p cho kh\u00e1ch h\u00e0ng.\nCh\u0103m s\u00f3c kh\u00e1ch h\u00e0ng sau gi\u1ea3i ng\u00e2n.Th\u1ef1c t\u1eadp sinh \nQuan h\u1ec7 kh\u00e1ch h\u00e0ng c\u00e1 nh\u00e2n\nNG\u00c2N H\u00c0NG TMCP TI\u00caN PHONG01/2024 - 03/2024\nS\u00e1ng t\u1ea1o v\u00e0 qu\u1ea3n l\u00fd n\u1ed9i dung \u0111a d\u1ea1ng tr\u00ean website v\u00e0\nfanpage, t\u1eadp trung v\u00e0o c\u00e1c ch\u1ee7 \u0111\u1ec1 v\u1ec1 c\u00e1c gi\u1ea3i \u0111\u1ea5u th\u1ec3 thao. \nPh\u1ed1i h\u1ee3p ch\u1eb7t ch\u1ebd v\u1edbi \u0111\u1ed9i ng\u0169 thi\u1ebft k\u1ebf \u0111\u1ec3 t\u1ea1o ra c\u00e1c \u1ea5n ph\u1ea9m\ntruy\u1ec1n th\u00f4ng.Th\u1ef1c t\u1eadp sinh Content Marketing\nC\u00d4NG TY C\u1ed4 PH\u1ea6N VSTATION VI\u1ec6T NAM09/2024 - 02/2025\nTi\u1ebfp nh\u1eadn brief t\u1eeb kh\u00e1ch h\u00e0ng, l\u00e0m r\u00f5 y\u00eau c\u1ea7u, m\u1ee5c ti\u00eau c\u1ee7a chi\u1ebfn\nd\u1ecbch.\nT\u01b0 v\u1ea5n, \u0111\u1ec1 xu\u1ea5t gi\u1ea3i ph\u00e1p truy\u1ec1n th\u00f4ng ph\u00f9 h\u1ee3p v\u1edbi ng\u00e2n s\u00e1ch v\u00e0\nm\u1ee5c ti\u00eau c\u1ee7a kh\u00e1ch h\u00e0ng.\nPh\u00e2n t\u00edch brief v\u00e0 truy\u1ec1n \u0111\u1ea1t ch\u00ednh x\u00e1c y\u00eau c\u1ea7u c\u1ee7a kh\u00e1ch h\u00e0ng\n\u0111\u1ebfn c\u00e1c team n\u1ed9i b\u1ed9.\nTheo d\u00f5i ti\u1ebfn \u0111\u1ed9 c\u00f4ng vi\u1ec7c, \u0111\u1ea3m b\u1ea3o c\u00e1c deliverables \u0111\u01b0\u1ee3c ho\u00e0n\nth\u00e0nh \u0111\u00fang deadline.\nL\u00e0m vi\u1ec7c v\u1edbi c\u00e1c \u0111\u1ed1i t\u00e1c b\u00ean ngo\u00e0i nh\u01b0 nh\u00e0 cung c\u1ea5p, KOLs,\nproduction house \u0111\u1ec3 \u0111\u1ea3m b\u1ea3o s\u1ea3n ph\u1ea9m \u0111\u1ea7u ra \u0111\u1ea1t y\u00eau c\u1ea7u.\nGi\u00e1m s\u00e1t c\u00e1c ho\u1ea1t \u0111\u1ed9ng th\u1ef1c thi, bao g\u1ed3m s\u1ea3n xu\u1ea5t booth,\nactivation, event,...\nKi\u1ec3m tra v\u00e0 ph\u00ea duy\u1ec7t c\u00e1c \u1ea5n ph\u1ea9m tr\u01b0\u1edbc khi g\u1eedi cho kh\u00e1ch h\u00e0ng.Account Executive\nC\u00d4NG TY TNHH QU\u1ea2NG C\u00c1O V\u00c0 TH\u01af\u01a0NG M\u1ea0I DELTAM\u1ee4C TI\u00caU NGH\u1ec0 NGHI\u1ec6P\nM\u1ee5c ti\u00eau trong 2 n\u0103m: Trau d\u1ed3i th\u00eam ki\u1ebfn th\u1ee9c v\u00e0 k\u0129 n\u0103ng\nchuy\u00ean m\u00f4n \u0111\u1ec3 tr\u1edf th\u00e0nh Wedding Planner\nM\u1ee5c ti\u00eau trong 5 n\u0103m: Tr\u1edf th\u00e0nh ng\u01b0\u1eddi c\u00f3 \u0111\u1ee7 k\u1ef9 n\u0103ng cho v\u1ecb\ntr\u00ed Wedding Planner Manager\nK\u1ef8 N\u0102NG\nTin h\u1ecdc v\u0103n ph\u00f2ng\nWord, Power Point, Excel \nThi\u1ebft k\u1ebf\nPhotoshop, AI, Canva \nK\u1ef9 n\u0103ng kh\u00e1c\nGiao ti\u1ebfp v\u00e0 l\u00e0m vi\u1ec7c nh\u00f3m t\u1ed1t\nT\u01b0 v\u1ea5n chuy\u00ean m\u00f4n v\u1ec1 s\u1ef1 ki\u1ec7n cho\nkh\u00e1ch h\u00e0ng\nQu\u1ea3n l\u00fd th\u1eddi gian\u0110\u1ea1i H\u1ecdc V\u0103n Lang 2020 - 2024\nChuy\u00ean ng\u00e0nh:\nMarketing\nGPA: 3.37/4\ud835\udc16 \ud835\udc1e\ud835\udc1d\ud835\udc1d\ud835\udc22\ud835\udc27\ud835\udc20  \ud835\udc0f\ud835\udc25\ud835\udc1a\ud835\udc27\ud835\udc27\ud835\udc1e\ud835\udc2b  \ud835\udc00\ud835\udc2c\ud835\udc2c\ud835\udc22\ud835\udc2c\ud835\udc2d\ud835\udc1a\ud835\udc27\ud835\udc2d\nGI\u1edaI THI\u1ec6U B\u1ea2N TH\u00c2N\nKinh nghi\u1ec7m tri\u1ec3n khai d\u1ef1 \u00e1n event &\nactivation \u0111a quy m\u00f4 cho c\u00e1c \u0111\u01a1n v\u1ecb uy t\u00edn:\nVinamilk, Huggies, S\u01a1n Kim Land,... \u0110am\nm\u00ea t\u1ed5 ch\u1ee9c s\u1ef1 ki\u1ec7n, t\u00f4i c\u00f3 kh\u1ea3 n\u0103ng qu\u1ea3n\nl\u00fd, \u0111i\u1ec1u ph\u1ed1i v\u00e0 gi\u00e1m s\u00e1t tri\u1ec3n khai, \u0111\u1ea3m\nb\u1ea3o d\u1ef1 \u00e1n di\u1ec5n ra su\u00f4n s\u1ebb, \u0111\u00fang ti\u1ebfn \u0111\u1ed9 v\u00e0\nmang l\u1ea1i tr\u1ea3i nghi\u1ec7m \u1ea5n t\u01b0\u1ee3ng cho kh\u00e1ch\nh\u00e0ng.\nHi\u1ec7n t\u1ea1i, t\u00f4i mong mu\u1ed1n chuy\u1ec3n h\u01b0\u1edbng\nsang l\u0129nh v\u1ef1c Wedding Planner v\u00ec ni\u1ec1m\ny\u00eau th\u00edch \u0111\u1eb7c bi\u1ec7t v\u1edbi ng\u00e0nh c\u01b0\u1edbi. T\u00f4i\nkhao kh\u00e1t \u0111\u01b0\u1ee3c h\u1ecdc h\u1ecfi v\u00e0 \u0111\u00f3ng g\u00f3p \u0111\u1ec3 t\u1ea1o\nn\u00ean nh\u1eefng kho\u1ea3nh kh\u1eafc \u00fd ngh\u0129a v\u00e0 tr\u1ecdn\nv\u1eb9n nh\u1ea5t cho c\u00e1c c\u1eb7p \u0111\u00f4i trong ng\u00e0y tr\u1ecdng\n\u0111\u1ea1i c\u1ee7a h\u1ecd.\nH\u1eccC V\u1ea4N\nNG\u00d4N NG\u1eee\nTi\u1ebfng anh \nAptis: B2\nPORTFOLIO\n"}
```

