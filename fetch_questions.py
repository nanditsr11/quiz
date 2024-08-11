import requests
import json
import random

def fetch_questions_from_api(amount=10, category=18, difficulty='medium'):
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type=multiple"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        formatted_questions = []

        for item in data['results']:
            question = {
                "question": item['question'],
                "choices": item['incorrect_answers'] + [item['correct_answer']],
                "correct_answer": item['correct_answer']
            }
            random.shuffle(question['choices'])  # Shuffle choices for randomness
            formatted_questions.append(question)
        
        return formatted_questions
    else:
        print(f"Failed to fetch questions. Status code: {response.status_code}")
        return []

def save_questions_to_file(questions, filename='question_data.json'):
    with open(filename, 'w') as f:
        json.dump(questions, f, indent=4)

if __name__ == "__main__":
    questions = fetch_questions_from_api(amount=10)
    if questions:
        save_questions_to_file(questions)
        print(f"Successfully saved {len(questions)} questions to question_data.json")
    else:
        print("No questions were fetched.")
