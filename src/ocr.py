import cv2
import pytesseract
from pytesseract import Output

# set path if needed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR	esseract.exe"

def preprocess(image_path: str):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # OTSU threshold to enhance text
    _, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return th

def ocr_image(image_path: str) -> str:
    img = preprocess(image_path)
    data = pytesseract.image_to_data(
        img, 
        output_type=Output.DICT, 
        lang="eng", 
        config="--oem 3 --psm 6"
    )
    
    # reconstruct line-wise text
    lines = {}
    
    for i, text in enumerate(data["text"]):
        if not text.strip():
            continue
        line_no = data["line_num"][i]
        lines.setdefault(line_no, [])
        lines[line_no].append(text)
    sorted_lines = [
        " ".join(words) 
        for ln, words in sorted(lines.items())
    ]
    
    return "
".join(sorted_lines)
