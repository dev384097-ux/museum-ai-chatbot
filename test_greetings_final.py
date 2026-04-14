import os
import sys
from dotenv import load_dotenv
from chatbot_engine import MuseumChatbot

# Ensure UTF-8 output even on Windows
if sys.stdout.encoding != 'utf-8':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

load_dotenv()

def test_greetings():
    bot = MuseumChatbot()
    
    # 2. English Greetings
    en_cases = ["Hello", "Hi", "Hey", "Good morning"]
    # 3. Hindi
    hi_native = ["नमस्ते", "नमस्कार"]
    hi_latin = ["namaste", "namaskar"]
    # 4. Tamil
    ta_native = ["வணக்கம்"]
    ta_latin = ["vanakkam"]
    # 5. Punjabi
    pa_native = ["ਸਤ ਸ੍ਰੀ ਅਕਾਲ"]
    pa_latin = ["sat sri akal"]
    # 6. Bengali
    bn_native = ["নমস্কার"]
    bn_latin = ["nomoskar"]
    # 7. Telugu
    te_native = ["నమస్తే"]
    te_latin = ["namaste"]
    # 8. Kannada
    kn_native = ["ನಮಸ್ಕಾರ"]
    kn_latin = ["namaskara"]
    # 9. Malayalam
    ml_native = ["നമസ്കാരം"]
    ml_latin = ["namaskaram"]
    # 10. Gujarati
    gu_native = ["નમસ્તે"]
    gu_latin = ["namaste"]
    # 11. Marathi
    mr_native = ["नमस्कार"]
    mr_latin = ["namaskar"]
    
    all_tests = [
        (en_cases, "en", "Hello! How can I help you today?"),
        (hi_native, "hi_native", "नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?"),
        (hi_latin, "hi_latin", "Namaste! Kaise help kar sakta hoon?"),
        (ta_native, "ta_native", "வணக்கம்! நான் எப்படி உதவலாம்?"),
        (ta_latin, "ta_latin", "Vanakkam! Naan eppadi help pannalaam?"),
        (pa_native, "pa_native", "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਮੈਂ ਤੁਹਾਡੀ ਕਿਵੇਂ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ?"),
        (pa_latin, "pa_latin", "Sat Sri Akal! Tuhadi kiven madad karaan?"),
        (bn_native, "bn_native", "নমস্কার! আমি কীভাবে সাহায্য করতে পারি?"),
        (bn_latin, "bn_latin", "Nomoskar! Ami kivabe help korte pari?"),
        (te_native, "te_native", "నమస్తే! నేను ఎలా సహాయం చేయగలను?"),
        (te_latin, "te_latin", "Namaste! Nenu ela help cheyagalanu?"),
        (kn_native, "kn_native", "ನಮಸ್ಕಾರ! ನಾನು ಹೇಗೆ సహాయ ಮಾಡಬಹುದು?"),
        (kn_latin, "kn_latin", "Namaskara! Naanu hege help madabahudu?"),
        (ml_native, "ml_native", "നമസ്കാരം! ഞാൻ എങ്ങനെ സഹായിക്കാം?"),
        (ml_latin, "ml_latin", "Namaskaram! Njan engane help cheyyam?"),
        (gu_native, "gu_native", "નમસ્તે! હું તમારી કેવી રીતે મદદ કરી શકું?"),
        (gu_latin, "gu_latin", "Namaste! Hu tamari kem madad kari saku?"),
        (mr_native, "mr_native", "नमस्कार! मी तुम्हाला कशी मदत करू शकतो?"),
        (mr_latin, "mr_latin", "Namaskar! Mi tumhala kashi madat karu shakto?")
    ]
    
    print("--- Testing Production Greetings ---")
    total = 0
    passed = 0
    
    for cases, group, expected in all_tests:
        for msg in cases:
            total += 1
            state = {}
            reply, state = bot.process_message(msg, state)
            success = reply.strip() == expected.strip()
            if success:
                passed += 1
            else:
                print(f"FAIL [{group}] Input: {msg}")
                print(f"  Expected: {expected}")
                print(f"  Received: {reply}")

    print(f"\nSummary: {passed}/{total} Passed")

    print("\n--- Testing Mixed Greetings ---")
    mixed_msg = "hello namaste"
    state = {}
    reply, state = bot.process_message(mixed_msg, state)
    print(f"Input: {mixed_msg} -> Reply: {reply}")
    if reply.strip() == "Hello! How can I help you today?":
        print("PASS (Single Language Output)")
    else:
        print("FAIL (Mixed or Wrong Output)")

if __name__ == "__main__":
    test_greetings()
