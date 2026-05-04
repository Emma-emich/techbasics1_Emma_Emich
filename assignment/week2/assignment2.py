#%%
#This is a Murder mystery game set in 1923 where a detective questions three suspects: Lady Evelyn, Mr Black and Mr. Finch about the death of the victim named Lord Greenwood. Depending on whom the detective interrogates, a new path will be revealed and in the end the detective has to suspect who they think the real killer is and rate how confident they are with their choice. In the end the game will reveal the true killer and give the detective a score according to his work.
import time
import sys


#  Helper functions to handle the output so the game stays clean
# The game was created with the help of Claude AI

def type_print(text, delay=0.03):
    """Print each text character by character for a typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
#writes every letter at a time with small pauses in between to create a typewriter effect
def slow_print(text, delay=0.6):
    """Print text line by line with a pause between lines."""
    for line in text.split("\n"):
        print(line)
        time.sleep(delay)
#prints each line with a small pause in between
def divider():
    print("\n" + "─" * 50 + "\n")
    time.sleep(0.3)
#prints decorative lines to set the scene and create a visula break just before the game starts


#Intro starts with def intro to set the mood with a slow title reveal and an introduction to the surroundings, each line being revealed with a small time delay

def intro():
    divider()
    type_print("🕯️  WELCOME TO: THE MANSION OF SECRETS  🕯️", delay=0.05)
    type_print("   A Murder Mystery Adventure\n", delay=0.04)
    time.sleep(0.5)
    slow_print("Your are currently in the year 1923.\nYou are a renowned detective summoned to Greenwood Mansion.\nLord Greenwood has been found dead in his study this morning.\n")
    time.sleep(0.4)
    type_print("Three suspects await your questioning...")
    time.sleep(1)
    divider()

#Now the player is asked to put their detective name into the user input: Input 1

def get_player_name():
    name = input("🔍 Enter your detective's name: ").strip()
    if name == "":
        name = "Detective X"
    return name

#Now the player gets to decide which suspect they want to interrogate first by choosing between 1,2 or 3 with the while true loop continuously asking until it receives a valid answer. After receiving a valid answer the interrogation can be led into a completely different direction through the main function. : Input 2

def choose_suspect(player_name):
    divider()
    type_print(f"Welcome, {player_name}. The three suspects are:\n")
    time.sleep(0.4)
    slow_print(
        "  [1] 🥀 Lady Evelyn  — Lord Greenwood's wife\n"
        "  [2] 🗡️  Mr. Black — an old military rival\n"
        "  [3] 📜 Mr. Finch    — the estate's lawyer"
    )
    time.sleep(0.3)

# INPUT 2: suspect choice — conditional checks
    while True:
        choice = input("\nWho do you question first? Enter 1, 2, or 3: ").strip()
        if choice in ["1", "2", "3"]:
            break
        else:
            type_print("⚠️  Invalid choice. Please enter 1, 2, or 3.")  # Conditional 1
#while true keeps asking until the player selects a valid option
    return choice

#depending on which number the player chooses they will be lead ti an interrogation of one suspect, which will be shown in a small dialogue with a yes/no follow-up question and the game will either reveal a clue for the player or send them away empty-handed



def interrogate_lady_evelyn():
    divider()
    type_print("🥀 You approach Lady Evelyn in the drawing room...", delay=0.04)
    time.sleep(0.8)
    slow_print(
        "\n\"I was in my bedroom all evening,\" she says, clutching a locket.\n"
        "\"I had nothing to gain from his death.\"\n"
    )
    time.sleep(0.5)
    clue = input("Do you press her about the locket? (yes/no): ").strip().lower()

    if clue == "yes":                                          # Conditional 2
        type_print("\n🔍 She hesitates... then whispers:")
        time.sleep(0.6)
        slow_print("\"Fine. He was going to cut me out of the will. But I didn't kill him!\"")
        time.sleep(0.4)
        type_print("📌 CLUE FOUND: Lady Evelyn had a motive — she knew about the will change.")
        return "evelyn"
    else:
        type_print("\nShe says nothing more. You find no useful clues here.")
        return None
#if the player selected option 1 the game will lead them to the interrogation of Lady Evelyn and ask her about a locket amd she will reveal her motive about the will change. Through the return of 'evelyn' the main() function recognizes that a clue was found

def interrogate_mr_black():
    divider()
    type_print("🗡️  Mr. Black stands by the fireplace, arms crossed...", delay=0.04)
    time.sleep(0.8)
    slow_print(
        "\n\"Greenwood owed me a debt. A large one.\"\n"
        "\"I came to collect, not to kill.\"\n"
    )
    time.sleep(0.5)
    clue = input("Do you ask about the debt? (yes/no): ").strip().lower()

    if clue == "yes":                                          # Conditional 3
        type_print("\nMr. Black's jaw tightens.")
        time.sleep(0.5)
        slow_print("\"Twenty thousand pounds. He laughed in my face this afternoon.\"")
        time.sleep(0.3)

        # NESTED CONDITIONAL inside Conditional 3
        follow_up = input("Do you ask where he was at 10 PM? (yes/no): ").strip().lower()
        if follow_up == "yes":                                 # Conditional 4 (nested)
            type_print("\n🔍 He pauses too long before answering...")
            time.sleep(0.6)
            type_print("📌 CLUE FOUND: Mr. Black has no alibi for the time of death.")
            return "black"
        else:
            type_print("\nYou let it go. He seems relieved.")
            return None
    else:
        type_print("\nHe shrugs. You find no useful clues here.")
        return None
#if the player selected option 2 they will be lead to the interrogation of Mr black. In this interrogation first the code checks if the player asks about the dept. If they do the second question will be asked about the alibi the night before. Therefore the second question can only be asked if the first question was already true and only then does the second question become relevant

def interrogate_mr_finch():
    divider()
    type_print("📜 Mr. Finch adjusts his spectacles nervously...", delay=0.04)
    time.sleep(0.8)
    slow_print(
        "\n\"Lord Greenwood called me here this evening to update his will.\"\n"
        "\"I assure you, it was all perfectly legal.\"\n"
    )
    time.sleep(0.5)
    clue = input("Do you ask to see the new will? (yes/no): ").strip().lower()

    if clue == "yes":                                          # Conditional 5
        type_print("\n🔍 Finch reaches into his briefcase with trembling hands...")
        time.sleep(0.8)
        slow_print("The will names Mr. Finch himself as sole beneficiary.")
        time.sleep(0.4)
        type_print("📌 CLUE FOUND: Mr. Finch inherits everything. He is the prime suspect.")
        return "finch"
    else:
        type_print("\nHe smiles thinly. You leave without a clue.")
        return None
#if the player selects option 3 he will be lead to the interrogation of Mr. Finch which will reveal him to be the main suspect with the strongest motive, discovering another clue.

#Input 3: confidence level: Now the user is asked to rate how confident they are about their suspected killer before the final accusation. The while true loop checks if the user typed correctly or if they typed text or out of range numbers instead of the in range ones and will print a warning if not. Therefore the main() will always receive a clean answer between 1-10 so it can continue running.

def get_confidence():
    divider()
    type_print("🔎 Time to make your accusation, Detective!", delay=0.04)
    time.sleep(0.4)
    slow_print("Before you accuse someone, rate your confidence in your conclusion.")

    while True:
        try:
            confidence = int(input("Enter your confidence level (1–10): "))
            if 1 <= confidence <= 10:                         # Range check
                break
            else:
                type_print("⚠️  Please enter a number between 1 and 10.")
        except ValueError:
            type_print("⚠️  That's not a valid number. Try again.")

    return confidence

#Once the detective entered a valid number to rate their confidence it will be time for the final accusation
#Final accusation: the function ending() takes all four arguments: player name, suspect choice, the list of clues found and the confidence score and maps the choice number to a suspect name and will then finally reveal the true killer - always Mr. Finch ;)
# There are two possible outcomes: first: if 'finch' is in clues_found, the player guessed correctly and gets praise and extra points if their confidence level was higher than 8. Otherwise the player will be told that they were wrong and shown what clues they have missed

def ending(player_name, suspect_choice, clues_found, confidence):
    divider()
    type_print("⚖️  THE FINAL ACCUSATION", delay=0.05)
    time.sleep(0.5)

# Map choice number to name
    names = {"1": "Lady Evelyn", "2": "Colonel Drake", "3": "Mr. Finch"}
    accused = names[suspect_choice]

    type_print(f"\n{player_name} steps forward and declares:\n")
    time.sleep(0.5)
    type_print(f'   "The murderer is... {accused}!"', delay=0.06)
    time.sleep(1)
    divider()

# Reveal the truth
    slow_print("The inspector opens the sealed envelope left by Lord Greenwood himself...\n")
    time.sleep(1)
    type_print("💀 The true killer was: Mr. Finch", delay=0.05)
    time.sleep(0.8)

    if "finch" in clues_found:
        type_print("\n✅ You were RIGHT! You found the key clue about the will.")
        if confidence >= 8:
            slow_print(f"\n🏆 Outstanding, {player_name}! A perfect deduction with full confidence.")
        else:
            slow_print(f"\n👏 Well done, {player_name}! Trust your instincts next time.")
    else:
        type_print("\n❌ You were wrong. The clue was hidden in the will all along.")
        slow_print(f"\nBetter luck next time, {player_name}...")

    divider()
    type_print("🕯️  THE END — Thank you for playing THE MANSION OF SECRETS  🕯️\n", delay=0.04)

#the main() function orders each section of the code, passes data between them and keeps the clue list updated

def main():
    intro()
    player_name = get_player_name()
    suspect_choice = choose_suspect(player_name)

    clues_found = []

    if suspect_choice == "1":
        result = interrogate_lady_evelyn()
    elif suspect_choice == "2":
        result = interrogate_mr_black()
    else:
        result = interrogate_mr_finch()

    if result:
        clues_found.append(result)

    confidence = get_confidence()
    ending(player_name, suspect_choice, clues_found, confidence)

if __name__ == "__main__":
    main()
