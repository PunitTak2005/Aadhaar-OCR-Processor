# Aadhaar OCR Processor

This project demonstrates an end-to-end pipeline for extracting structured information from Aadhaar card images using OCR (Optical Character Recognition) and rule-based NLP.

## Task Objective
Demonstrate hands-on ability in OCR, NLP, and Generative AI-based document processing by:
- Selecting a document type (Aadhaar Card).
- Extracting text using OCR.
- Identifying and structuring key fields into JSON.
- Explaining accuracy improvements using LLMs.

## Project Structure
- `src/ocr.py`: Handles image preprocessing (grayscale, thresholding) and Tesseract OCR integration.
- `src/extract_fields.py`: Contains regex patterns and logic to parse OCR text into a structured JSON format (Name, DOB, Gender, Aadhaar Number, Address).
- `requirements.txt`: Python dependencies.

## Key Fields Extracted
- **Name**: Detected via line positions and character filtering.
- **DOB/YOB**: Extracted using regex patterns for dates and \"Year of Birth\".
- **Gender**: Identified via keyword matching (MALE/FEMALE).
- **Aadhaar Number**: Extracted using the 12-digit (4-4-4) pattern.
- **Address**: Parsed from the back side of the card.

## Improving Accuracy with NLP / LLMs
While this implementation uses rule-based parsing, production systems can be improved by:
1. **Named Entity Recognition (NER)**: Fine-tuning models like spaCy or LayoutLM to recognize fields regardless of layout variations.
2. **LLM Post-processing**: Using LLMs (like GPT-4) to clean noisy OCR text and correct common misread characters (e.g., 'I' vs '1').
3. **Format Validation**: Implementing checksum algorithms for Aadhaar numbers and date validation.

## How to Run
1. Install Tesseract OCR on your system.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the extraction script: `python src/extract_fields.py`.
