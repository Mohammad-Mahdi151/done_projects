def main():
    print("Welcome to the Word Chain Game!")
    print("Two players will take turns entering words.")
    print("Each word must start with the last letter of the previous word.")
    print("No repeated words are allowed.")
    print("Let's start!\n")
 
    used_words = set()
    current_word = input("Player 1, enter the first word: ").strip().lower()
    used_words.add(current_word)
 
    # Determine which player's turn it is: 1 or 2
    player_turn = 2
 
    while True:
        last_char = current_word[-1]
        if player_turn == 2:
            prompt = f"Player 2, enter a word starting with {last_char} :"
        else:
            prompt = f"Player 1, enter a word starting with {last_char} : "
 
        next_word = input(prompt).strip().lower()
 
        # Check if the word has been used before
        if next_word in used_words:
            print("This word has already been used. Try again.")
            continue
 
        # Check if the first letter matches the last letter of previous word
        if not next_word.startswith(last_char):
            print(f"Invalid start letter. The word should start with {last_char}")
            continue
 
        # Valid move
        used_words.add(next_word)
        current_word = next_word
        # Switch turns
        player_turn = 1 if player_turn == 2 else 2
