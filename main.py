'''
Med AI Web Server
'''
from flask import Flask, render_template, request
from parse_pdf import extract_text_from_pdf
from gpt_agent import gpt_agent

app = Flask(__name__)

# All headers
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

# first page
@app.route('/upload', methods=['POST'])
def upload():
    if 'pdfFile' not in request.files:
        return 'No file part'

    file = request.files['pdfFile']

    if file.filename == '':
        return 'No selected file'

    if file:
        # Save the uploaded file to a temporary location
        file.save('temp.pdf')

        extracted_text = extract_text_from_pdf("temp.pdf")

        # print(extracted_text)
        # # Return the extracted text to the client
        extracted_text_analyse = gpt_agent(extracted_text)

        return f"The Extracted text is as follows:\n{extracted_text_analyse}\n"

    return 'File uploaded successfully'

if __name__== '__main__':
    app.run(debug=True, port=5000)