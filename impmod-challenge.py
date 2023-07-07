#!/usr/bin/env python3

"""
create a script that includes the trivia dictionary below.
Slice and print out the trivia question and the four answers (one correct, three incorrect) from the dictionary.
Use the html library to render the question/answers in the proper format.
BONUS: have the user answer A, B, C, or D and see if they guess the answer correctly!
"""

import html

def main():

    #trivia dictionary
    trivia= {
            "category": "Entertainment: Film",
            "type": "multiple",
            "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
            "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
            "incorrect_answers": [
                "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
                "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
                "&quot;Round up the usual suspects.&quot;"
                ]
            }

    while True:
        #slice and print question from trivia dictionary
        print(f"\n{trivia.get('question')}\n")

        #slice and print the answers
        print(f"A. {html.unescape(trivia['incorrect_answers'][0])}")
        print(f"B. {html.unescape(trivia['incorrect_answers'][1])}")
        print(f"C. {html.unescape(trivia['incorrect_answers'][2])}")
        print(f"D. {html.unescape(trivia['correct_answer'])}")

        #prompt user for an answer, save, and covert to uppercase
        answer = input(f"\nAnswer: ").upper()

        #compare the answer and tell user if right or wrong
        if answer == 'D':
            print(f"\nCorrect!")
            break
        else:
            print(f"\nSorry, your answer is incorrect.")
            continue

if __name__ == "__main__":
    main()
