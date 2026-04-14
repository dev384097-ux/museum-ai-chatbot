from chatbot_engine import MuseumChatbot

def test_final_polish():
    bot = MuseumChatbot()
    
    test_cases = [
        ("Sat   Sri   Akal!!!", "Sat Sri Akal! Tuhadi kiven madad karaan?"), # Messy spacing + punct
        (" vanakkam ", "Vanakkam! Naan eppadi help pannalaam?"),     # Extra spaces
        ("NAMASTE!!!", "Namaste! Kaise help kar sakta hoon?"),        # Case + bang
        ("hello namaste", "Hello! How can I help you today?")       # English Priority check
    ]
    
    print("--- Final Production Polish Test ---")
    for msg, expected in test_cases:
        state = {}
        reply, state = bot.process_message(msg, state)
        success = reply.strip() == expected.strip()
        status = "PASS" if success else "FAIL"
        print(f"Input: '{msg}' -> {status}")
        if not success:
            print(f"  Expected: {expected}")
            print(f"  Received: {reply}")

if __name__ == "__main__":
    test_final_polish()
