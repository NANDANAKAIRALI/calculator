class Dictionary:
    def __init__(self):

        self.word_meanings = {
            "python": "a programming language",
            "code": "a system of signals or symbols for communication",
            "algorithm": "a set of rules for solving a problem in a finite number of steps",
           
        }

    def lookup_word(self, word):
        return self.word_meanings.get(word, None)

    def suggest_words(self, prefix):
        suggestions = [word for word in self.word_meanings if word.startswith(prefix)]
        return suggestions


dictionary = Dictionary()

while True:
    user_input = input("Enter a word or 'exit' to quit: ").lower()

    if user_input == 'exit':
        print("Goodbye!")
        break
    meaning = dictionary.lookup_word(user_input)
    if meaning:
        print(f"Meaning of '{user_input}': {meaning}")
    else:
        suggestions = dictionary.suggest_words(user_input)
        if suggestions:
            print(f"Word not found. Suggestions: {', '.join(suggestions)}")
        else:
            print("Word not found, and no suggestions available.")

