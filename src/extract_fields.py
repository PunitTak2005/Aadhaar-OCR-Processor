import re
import json

def extract_aadhaar_number(text: str):
    m = re.search(r"\b(\d{4}\s\d{4}\s\d{4})\b", text)
    return m.group(1) if m else None

def extract_gender(text: str):
    if re.search(r"\bMALE\b", text, re.IGNORECASE):
        return "MALE"
    if re.search(r"\bFEMALE\b", text, re.IGNORECASE):
        return "FEMALE"
    return None

def extract_dob_or_yob(text: str):
    m_dob = re.search(r"(DOB[:\s]*)?(\d{2}[\/\-]\d{2}[\/\-]\d{4})", text, re.IGNORECASE)
    if m_dob:
        return m_dob.group(2)
    m_yob = re.search(r"(Year of Birth[:\s]*)?(\d{4})", text, re.IGNORECASE)
    if m_yob:
        return m_yob.group(2)
    return None

def extract_name(front_text: str, dob_or_yob: str | None):
    lines = front_text.split("
")
    if dob_or_yob:
        for i, line in enumerate(lines):
            if dob_or_yob in line:
                for j in range(i - 1, max(-1, i - 3), -1):
                    candidate = lines[j].strip()
                    if candidate and not any(ch.isdigit() for ch in candidate):
                        return candidate
    for line in lines:
        line = line.strip()
        if line and not any(ch.isdigit() for ch in line):
            return line
    return None

def extract_address(back_text: str):
    m = re.search(r"Address[:\-]?(.*)", back_text, re.IGNORECASE | re.DOTALL)
    if m:
        return m.group(1).strip()
    return None

def build_aadhaar_json(front_text: str, back_text: str):
    aadhaar_number = extract_aadhaar_number(front_text + "
" + back_text)
    gender = extract_gender(front_text)
    dob_or_yob = extract_dob_or_yob(front_text)
    name = extract_name(front_text, dob_or_yob)
    address = extract_address(back_text)
    
    return {
        "document_type": "aadhaar",
        "name": name,
        "dob_or_yob": dob_or_yob,
        "gender": gender,
        "aadhaar_number": aadhaar_number,
        "address": address,
        "raw_text_front": front_text,
        "raw_text_back": back_text
    }

if __name__ == "__main__":
    front = "GOVERNMENT OF INDIA
RAVI KUMAR
DOB: 15/03/1998
MALE
1234 5678 9012"
    back = "Address: Flat 201, XYZ Apartments,
Dwarka, New Delhi, 110075"
    result = build_aadhaar_json(front, back)
    print(json.dumps(result, indent=2, ensure_ascii=False))
