# Cricket Quiz Game

questions = [
    {
        "question": "Who scored the most runs in the ICC Cricket World Cup 2019?",
        "options": ["A. Rohit Sharma", "B. David Warner", "C. Kane Williamson", "D. Joe Root"],
        "answer": "A"
    },
    {
        "question": "Which country won the ICC Champions Trophy in 2017?",
        "options": ["A. Pakistan", "B. India", "C. Australia", "D. England"],
        "answer": "A"
    },
    {
        "question": "Who holds the record for the fastest century in One Day Internationals (ODIs)?",
        "options": ["A. AB de Villiers", "B. Chris Gayle", "C. Shahid Afridi", "D. Virat Kohli"],
        "answer": "A"
    },
    {
        "question": "What is the maximum number of overs allowed in a T20 International match?",
        "options": ["A. 15", "B. 18", "C. 20", "D. 25"],
        "answer": "C"
    },
    {
        "question": "Who was the captain of the Indian cricket team during the 2021 T20 World Cup?",
        "options": ["A. Virat Kohli", "B. MS Dhoni", "C. Rohit Sharma", "D. Kapil Dev"],
        "answer": "A"
    },
    {
        "question": "In which year did England win their first ICC Cricket World Cup?",
        "options": ["A. 1975", "B. 1983", "C. 1992", "D. 2019"],
        "answer": "D"
    },
    {
        "question": "Who is known as the 'Universe Boss' in T20 cricket?",
        "options": ["A. AB de Villiers", "B. Chris Gayle", "C. MS Dhoni", "D. Virat Kohli"],
        "answer": "B"
    },
    {
        "question": "Which player has the most wickets in T20 Internationals?",
        "options": ["A. Shadab Khan", "B. Lasith Malinga", "C. Umar Gul", "D. Shakib Al Hasan"],
        "answer": "D"
    },
    {
        "question": "Who was the Player of the Tournament in the ICC Cricket World Cup 2019?",
        "options": ["A. Rohit Sharma", "B. Kane Williamson", "C. Ben Stokes", "D. Steve Smith"],
        "answer": "B"
    },
    {
        "question": "What is the maximum number of players a team can have in the playing XI during an ODI?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 15"],
        "answer": "B"
    }
]


def run_quiz():
    score = 0

    print("🏏 Welcome to the Cricket Quiz! 🏏\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}\n")

    print(f"🎯 Quiz Over! Your final score: {score}/{len(questions)}")


# Run the quiz
if __name__ == "__main__":
    run_quiz()
