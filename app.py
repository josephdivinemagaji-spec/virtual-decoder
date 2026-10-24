from flask import Flask, render_template, request, jsonify

# This line tells Flask to look for index.html right on your main screen
app = Flask(__name__, template_folder=".")

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
