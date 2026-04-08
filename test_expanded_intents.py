from chatbot_engine import MuseumChatbot
import json
import sys

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_fixed_chatbot():
    bot = MuseumChatbot()
    
    # CASE 1: Intent Collision Fix
    state = {'state': 'idle', 'lang': 'en'}
    print("\n--- Testing Intent Collision: 'what about security?' ---")
    resp, state = bot.process_message("what about security?", state)
    print(f"REPLY: {resp}")
    if "Security is a top priority" in resp:
        print("PASS: Correctly matched Security intent.")
    else:
        print("FAIL: Matched wrong intent (likely History).")

    # CASE 2: Language Flapping Fix (Short words)
    state = {'state': 'idle', 'lang': 'en'}
    print("\n--- Testing Language Flapping: 'hindi' (should stay English) ---")
    resp, state = bot.process_message("hindi", state)
    print(f"REPLY: {resp}")
    print(f"LANG: {state['lang']}")
    if state['lang'] == 'en':
        print("PASS: Stayed in English.")
    else:
        print(f"FAIL: Switched to {state['lang']}.")

    # CASE 3: State-Based KB Query
    state = {'state': 'awaiting_exhibition_selection', 'lang': 'en'}
    print("\n--- Testing KB Query during Booking: 'parking' ---")
    resp, state = bot.process_message("parking", state)
    print(f"REPLY: {resp}")
    if "You can continue your booking" in resp:
        print("PASS: Answered KB and provided reminder.")
    else:
        print("FAIL: Missing state reminder.")

    # CASE 4: Another short word collision
    state = {'state': 'idle', 'lang': 'en'}
    print("\n--- Testing Language Flapping: 'time' ---")
    resp, state = bot.process_message("time", state)
    print(f"REPLY: {resp}")
    print(f"LANG: {state['lang']}")
    if state['lang'] == 'en' and "Museum Hours" in resp:
        print("PASS: Correctly identified Timing in English.")

if __name__ == "__main__":
    test_fixed_chatbot()
