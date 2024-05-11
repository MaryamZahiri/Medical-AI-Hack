from flask import Flask, render_template, request

app = Flask(__name__)

occupations = ['Healthcare', 'Engineer', 'Law', 'Other']
age_ranges = ['<20', '20-40', '40>']
interest_options = ['Yes', 'No']
money=['0','0-10','10-100','101']

@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        occupation = request.form['occupation']
        age = request.form['age']
        interest = request.form['interest']
        money=request.form['money']
        # Here you can process the submitted data, such as storing it in a database
        
        return "Thank you for completing the questionnaire!"

    return render_template('questionnaire.html', 
                           occupations=occupations, 
                           age_ranges=age_ranges, 
                           interest_options=interest_options)

if __name__ == '__main__':
    app.run(debug=True, port=3001)
