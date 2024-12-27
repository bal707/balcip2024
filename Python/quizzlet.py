"""
Program loops over a dictionary of words and 
quizzes the user for their corresponding Spanish translations, 
keeping count of how many the user gets correct! 
"""

def quiz_user(translations):
    correct_count = 0
    total_questions = len(translations)

    for english_word, spanish_word in translations.items():
        user_answer = input(f"What is the Spanish translation for {english_word}? ").strip()
        
        if user_answer.lower() == spanish_word.lower():
            print("That is correct!\n")
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {spanish_word}.\n")
    
    print(f"You got {correct_count}/{total_questions} words correct, come study again soon!")

def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    quiz_user(translations)

if __name__ == '__main__':
    main()
