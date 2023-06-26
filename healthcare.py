
import gradio

questions = [
    "What is your heart condition?",
    "What is the silence killer?",
    "What is medical screening for?",
    "What is blood and urine test?",
    "What is most common imaging test?",
    "What is Comprehensive Medical Test?",
    "What is average costs for medical test?"
]

choices = [
    ["a) Like to Know", "b) Let me Guess", "c) I Don't Bother"],
    ["a) Diabetes", "b) Stroke & Heart Attack", "c) Colon Cancer"],
    ["a) Detection of diseases", "b) Prevention of diseases ", "c) Treatment of diseases"],
    ["a) Yearly medical exmination", "b) Basic medical screening", "c) Occasion medical examination"],
    ["a) X-rays", "b) Ultrasound", "c) MRI"],
    ["a) ABO blood group", "b) Full Medical check-ups", "c) Cancer markers"],
    ["a) RM 3000", "b) RM 5000", "c) RM 7000"],
]

correct_answers = ["Like to know", "Stroke & Heart Attack", "Detection of diseases", "Basic medical screening", "X-rays", "Full Medical check-ups", "RM 3000"]

def run_quiz(*answers):
    score = 0

    for i in range(len(questions)):
        user_answer = answers[i]
        if user_answer is None:
            return "Please provide an answer for all questions."
        if user_answer.split(") ")[1].lower() == correct_answers[i].lower():
            score += 1

    percentage = (score / len(questions)) * 100
    result = f"\nYou scored {score} out of {len(questions)} questions correctly.\nYour score: {percentage}%"

    # Save the score in a file
    with open("quiz_scores.txt", "a") as file:
        file.write(f"Score: {score}/{len(questions)} - {percentage}%\n")

    return result


gradio_interface = gradio.Interface(
    fn=run_quiz,
    inputs=[
        gradio.inputs.Radio(label=questions[i], choices=choices[i]) for i in range(len(questions))
    ],
    outputs="text",
    title="Python Quiz",
    description="Answer the quiz questions to test your knowledge!",
    examples=[
        ["a) Like to know", "b) Stroke & Heart Attack", "a) Detection of diseases", "b) Basic medical screening", "a) X-rays", "b) Full Medical check-ups", "a) RM 3000"]  # Example input: Provide the correct answers as an example, e.g., ["a", "b", "a", "b", "a", "b", "a"]
    ],
)

gradio_interface.launch(share=True)