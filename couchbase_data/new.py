from flask import Flask, render_template, request
from datetime import datetime
import traceback
# For exceptions
from couchbase.exceptions import CouchbaseException
# Required for any cluster connection
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
# Required for options -- cluster, timeout, SQL++ (N1QL) query, etc.
from couchbase.options import ClusterOptions
from datetime import timedelta

app = Flask(__name__)

# Couchbase connection details
endpoint = "couchbases://cb.buk3yoejwdohwo9t.cloud.couchbase.com" # Replace this with Connection String
username = "medAI" # Replace this with username from database access credentials
password = "Mb09128343053$!" # Replace this with password from database access credentials
bucket_name = "travel-sample"
scope_name = "_default"
collection_name = "Interview_form"

# Connect options - authentication
auth = PasswordAuthenticator(username, password)
# Get a reference to our cluster
options = ClusterOptions(auth)
# Use the pre-configured profile below to avoid latency issues with your connection.
options.apply_profile("wan_development")
cluster = Cluster(endpoint, options)
# Wait until the cluster is ready for use.
# cluster.wait_until_ready(timeout=5)

# Get a reference to our bucket and collection
cb = cluster.bucket(bucket_name)
cb_coll = cb.scope(scope_name).collection(collection_name)


occupations = ['Healthcare', 'Engineer', 'Law', 'Other']
age_ranges = ['<20', '20-40', '40>']
interest_options = ['Yes', 'No']
money=['0','0-10','10-100','101']


@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        # Retrieve data from the form
        occupation = request.form['occupation']
        age = request.form['age']
        interest = request.form['interest']
        payment = request.form['payment']
        
        # Construct the document to be inserted into Couchbase
        document = {
            "type": "airplane_sample",
            "timestamp": datetime.now().isoformat(),
            "occupation": occupation,
            "age": age,
            "interest": interest,
            "money": payment
        }

        try:
            # Insert the document into the Couchbase collection
            result = cb_coll.insert(f"airplane_sample_{datetime.now().timestamp()}", document)
            print("\nCreate document success. CAS: ", result.cas)
        except CouchbaseException as e:
            print(e)
            return "Error occurred while saving data to database"
        

        return "Thank you for completing the questionnaire!"

    return render_template('questionnaire.html', 
                           occupations=occupations, 
                           age_ranges=age_ranges, 
                           interest_options=interest_options)

if __name__ == '__main__':
    app.run(debug=True, port=3001, host='0.0.0.0')
