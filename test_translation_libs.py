from langdetect import detect
from deep_translator import GoogleTranslator

def test_translation():
    test_phrases = {
        "hi": "English",
        "नमस्ते": "Hindi",
        "எப்படி இருக்கிறீர்கள்?": "Tamil",
        "మీరు ఎలా ఉన్నారు?": "Telugu",
        "तुम्ही कसे आहात?": "Marathi"
    }
    
    for phrase, lang_name in test_phrases.items():
        try:
            detected = detect(phrase)
            translated = GoogleTranslator(source='auto', target='en').translate(phrase)
            print(f"Phrase: {phrase} ({lang_name})")
            print(f"Detected: {detected}")
            print(f"Translated to EN: {translated}")
            
            # Translate back
            back = GoogleTranslator(source='en', target=detected).translate("Hello, I am a museum curator.")
            print(f"Translated back to {detected}: {back}")
            print("-" * 20)
        except Exception as e:
            print(f"Error with {lang_name}: {e}")

if __name__ == "__main__":
    test_translation()
