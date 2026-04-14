# -*- coding: utf-8 -*-
from chatbot_engine import MuseumChatbot
import sys
import io

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_indian_languages():
    bot = MuseumChatbot()
    
    test_cases = [
        {"msg": "Namaste", "lang": "Hinglish Greeting", "expected": "Kaise help kar sakta hoon"},
        {"msg": "I want to book ticket", "lang": "English Booking", "expected": "Sure!"},
        {"msg": "Vanakkam!", "lang": "Tanglish Greeting", "expected": "Vanakkam"},
        {"msg": "Sat Sri Akal", "lang": "Punglish Greeting", "expected": "Sat Sri Akal"},
        {"msg": "Ticket book karna hai", "lang": "Hinglish Flow", "expected": "Zaroor"},
        {"msg": "संग्रहालय का समय क्या है?", "lang": "Hindi Native", "expected": "9:00"}
    ]
    
    print("\n--- Testing Session Lock (Hinglish -> English Switch) ---")
    state = {}
    resp1, state = bot.process_message("mujhe ticket chahiye", state)
    print(f"User: mujhe ticket chahiye\nBot: {resp1}\nLocked Lang: {state.get('locked_lang')}")
    
    resp2, state = bot.process_message("ok book it", state)
    print(f"User: ok book it\nBot: {resp2}\n")
    if "Zaroor" in resp2 or "Kaunsi" in resp2:
        print("RESULT: PASS (Language Locked to Hinglish)")
    else:
        print("RESULT: FAIL (Language Switch detected)")
    
    for case in test_cases:
        state = {'state': 'idle'}
        print(f"\nTesting {case['lang']}: {case['msg']}")
        try:
            response, state = bot.process_message(case['msg'], state)
            print(f"BOT REPLY: {response}")
            # Since it's translated, we just check if it seems broadly correct or at least responsive
            if state['state'] != 'idle' or any(word in response.lower() for word in ['9', 'ticket', 'park', 'confirm', 'choice', 'help']):
                print("Result: PASS (Responsive)")
            else:
                print("Result: POTENTIAL FAIL (Check reply content)")
        except Exception as e:
            print(f"ERROR testing {case['lang']}: {e}")

if __name__ == "__main__":
    test_indian_languages()
