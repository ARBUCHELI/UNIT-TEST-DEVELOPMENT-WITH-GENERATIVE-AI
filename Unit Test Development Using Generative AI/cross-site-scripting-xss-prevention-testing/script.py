from flask import Flask, request, render_template_string, session

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Simulate a simple in-memory 'database' to store user input
fake_db = {"user_input": ""}

@app.route('/store', methods=['POST'])
def store():
    user_input = request.form['input']
    fake_db['user_input'] = user_input  # Store the input in the 'database'
    return "Input stored successfully!"

@app.route('/get-stored-input')
def get_stored_input():
    # Return the stored input back to the user
    stored_input = fake_db['user_input']
    return render_template_string(f"<div>{stored_input}</div>")

if __name__ == '__main__':
    app.run(debug=True)
