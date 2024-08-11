# Quiz Server

A simple Python quiz server using `http.server` that serves random programming-related questions from a JSON file and checks answers.

## Features

- **GET `/get_question`**: Returns a random question.
- **POST `/check_answer`**: Verifies the user's answer.


## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/quiz_server.git
   cd quiz_server

2. **Prepare Questions: Ensure question_data.json contains your quiz questions.**

3.  **Run the Server:**
       python main.py

## Usage

1. GET Question: curl http://localhost:8000/get_question
2. POST Answer:
     curl -X POST http://localhost:8000/check_answer -H "Content-Type: application/json" -d '{"user_answer": "Paris", "correct_answer": "Paris"}'

## Summary

This Python quiz server uses http.server to serve random programming-related questions from a JSON file and verify user answers via simple GET and POST requests. To set it up, clone the repository, ensure the question_data.json contains your questions, and run main.py to start the server. The server operates on http://localhost:8000, where you can fetch a question with a GET request to /get_question and check answers with a POST request to /check_answer.


