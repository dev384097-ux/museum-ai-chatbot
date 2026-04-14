from chatbot_engine import MuseumChatbot

def test_greeting_override():
    bot = MuseumChatbot()
    state = {}
    
    # 1. Start session with English
    msg1 = "Hello"
    reply1, state = bot.process_message(msg1, state)
    print(f"Input 1: '{msg1}' -> Reply: '{reply1}' (Lang: {state.get('locked_lang')})")
    
    # 2. Switch to Punjabi
    msg2 = "Sat Sri Akal!!!"
    reply2, state = bot.process_message(msg2, state)
    print(f"Input 2: '{msg2}' -> Reply: '{reply2}' (Lang: {state.get('locked_lang')})")
    
    # 3. Switch to Hindi
    msg3 = "NAMASTE"
    reply3, state = bot.process_message(msg3, state)
    print(f"Input 3: '{msg3}' -> Reply: '{reply3}' (Lang: {state.get('locked_lang')})")

    # 4. Verify 100% success
    expected_pa = "Sat Sri Akal! Tuhadi kiven madad karaan?"
    expected_hi = "Namaste! Kaise help kar sakta hoon?"
    
    pa_pass = reply2.strip() == expected_pa
    hi_pass = reply3.strip() == expected_hi
    
    print(f"\nPunjabi Override: {'PASS' if pa_pass else 'FAIL'}")
    print(f"Hindi Override: {'PASS' if hi_pass else 'FAIL'}")

if __name__ == "__main__":
    test_greeting_override()
