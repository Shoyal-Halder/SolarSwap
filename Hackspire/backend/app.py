from flask import Flask, request

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.form
    with open("users.txt", "a") as file:
        file.write(str(dict(data)) + "\n")
    return "Success"

if __name__ == "__main__":
    app.run(debug=True)
