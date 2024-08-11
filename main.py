import http.server
import socketserver
import json
import random

PORT = 8000

class QuizHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/get_question":
            with open('question_data.json', 'r') as f:
                questions = json.load(f)
            question = random.choice(questions)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(question).encode())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/check_answer":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            correct_answer = data['correct_answer']
            user_answer = data['user_answer']

            is_correct = correct_answer.lower() == user_answer.lower()
            response = {
                'is_correct': is_correct,
                'correct_answer': correct_answer
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), QuizHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
