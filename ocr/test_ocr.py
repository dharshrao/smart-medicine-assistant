from ocr_engine import extract_text, clean_text, detect_medicine_name

# your known medicines
medicine_db = ["paracetamol", "dolo", "cetirizine", "amoxicillin"]

text = extract_text("paracetamol_strip.jpg")

cleaned = clean_text(text)

medicine = detect_medicine_name(cleaned, medicine_db)

print("Detected Medicine:", medicine)