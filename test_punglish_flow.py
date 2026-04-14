from chatbot_engine import MuseumChatbot

def test_punglish_booking_flow():
    bot = MuseumChatbot()
    state = {}
    
    # 1. Greeting (Should lock to Roman Punjabi)
    msg1 = "sat sri akal"
    reply1, state = bot.process_message(msg1, state)
    print(f"Input 1: '{msg1}' -> Reply: '{reply1}'")
    print(f"Locked Script: {state.get('locked_script')}")
    
    # 2. Start Booking
    msg2 = "ticket book"
    reply2, state = bot.process_message(msg2, state)
    print(f"\nInput 2: '{msg2}' -> Reply: (truncated)")
    print(f"Locked Script: {state.get('locked_script')}")
    
    # 3. Select Exhibition 1
    msg3 = "1"
    reply3, state = bot.process_message(msg3, state)
    print(f"\nInput 3: '{msg3}' -> Reply: '{reply3}'")
    
    # Expected: "Wadiya choice" (Roman), NOT "ਵਧੀਆ ਚੋਣ" (Native)
    expected_start = "Wadiya choice"
    success = reply3.startswith(expected_start)
    
    print(f"\nResult: {'PASS' if success else 'FAIL'}")
    if not success:
        print(f"Expected start: {expected_start}")
        print(f"Actual reply: {reply3}")

if __name__ == "__main__":
    test_punglish_booking_flow()
