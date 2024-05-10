'''
Med AI Web Server
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/lab-report')
def lab_report():
    return render_template('/header_html/lab_report.html')

@app.route('/calories-tracker')
def calory_tracker():
    return render_template('/header_html/calories_tracker.html')

@app.route('/symptom-tracker')
def symptom_tracker():
    return render_template('/header_html/symptom_tracker.html')

@app.route('/dashboard')
def dashboard():
    return render_template('/header_html/dashboard.html')

@app.route('/join')
def join():
    return render_template('/header_html/join.html')

@app.route('/chat-bot')
def chat_bot():
    return render_template('/header_html/chat_bot.html')

if __name__== '__main__':
    app.run(debug=True, port=5000)