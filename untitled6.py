import random

# Predefined lists of random words
places = ["park", "beach", "mall", "zoo", "school"]
adjectives = ["funny", "exciting", "boring", "beautiful", "crazy"]
nouns = ["cat", "dog", "robot", "teacher", "alien"]
verbs = ["running", "jumping", "dancing", "laughing", "singing"]

def get_random_word(word_list):
    """Returns a random word from a given list."""
    return random.choice(word_list)

def play_mad_libs():
    print("Welcome to the Mad Libs Game!")

    # Multiple story templates
    story_templates = [
        "Today I went to the {place}. It was very {adjective}. I saw a {noun} {verb} there!",
        "The {noun} was {verb} while the {adjective} {noun} watched in surprise at the {place}!",
        "At the {place}, I met a {adjective} {noun} who was {verb} all day!"
    ]
    
    print("\nChoose a story template:")
    for i, template in enumerate(story_templates, 1):
        print(f"{i}: {template[:30]}...")

    # Select a story template
    template_choice = int(input("\nEnter the number of the story you want to play (1/2/3): "))
    if template_choice not in [1, 2, 3]:
        print("Invalid choice. Please select a number between 1 and 3.")
        return

    selected_template = story_templates[template_choice - 1]

    # Collect user inputs or use random words
    place = input("Enter a place (or press Enter for a random word): ").strip() or get_random_word(places)
    adjective = input("Enter an adjective (or press Enter for a random word): ").strip() or get_random_word(adjectives)
    noun = input("Enter a noun (or press Enter for a random word): ").strip() or get_random_word(nouns)
    verb = input("Enter a verb (-ing form) (or press Enter for a random word): ").strip() or get_random_word(verbs)

    # Fill the selected template
    final_story = selected_template.format(place=place, adjective=adjective, noun=noun, verb=verb)
    
    # Print the final story
    print("\nHere's your Mad Libs story:")
    print(final_story)

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_mad_libs()

# Run the game
if __name__ == "__main__":
    play_mad_libs()
