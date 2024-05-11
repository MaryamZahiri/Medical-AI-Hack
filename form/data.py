from datetime import timedelta
import traceback
# For exceptions
from couchbase.exceptions import CouchbaseException
# Required for any cluster connection
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
# Required for options -- cluster, timeout, SQL++ (N1QL) query, etc.
from couchbase.options import ClusterOptions
endpoint = "couchbases://cb.buk3yoejwdohwo9t.cloud.couchbase.com" # Replace this with Connection String
username = "medAI" # Replace this with username from database access credentials
password = "Mb09128343053$!" # Replace this with password from database access credentials
bucket_name = "travel-sample"
scope_name = "_default"
collection_name = "Interview_form"
# Sample airline document
# sample_airline = {
# 	"type": "airline",
# 	"id": 8091,
# 	"callsign": "CBS",
# 	"iata": None,
# 	"icao": None,
# 	"name": "Couchbase Airways",
# }



# Key will equal: "airline_8091"
key = "airline_8091"
# User Input ends here.
# Connect options - authentication
auth = PasswordAuthenticator(username, password)
# Get a reference to our cluster
options = ClusterOptions(auth)
# Use the pre-configured profile below to avoid latency issues with your connection.
options.apply_profile("wan_development")
try:
	cluster = Cluster(endpoint, options)
	# Wait until the cluster is ready for use.
	cluster.wait_until_ready(timedelta(seconds=5))
	# Get a reference to our bucket
	cb = cluster.bucket(bucket_name)
	# Get a reference to our collection
	cb_coll = cb.scope(scope_name).collection(collection_name)
	# Simple K-V operation - to create a document with specific ID
	try:
		result = cb_coll.insert(key, sample_airline)
		print("\nCreate document success. CAS: ", result.cas)
	except CouchbaseException as e:
		print(e)
	# Simple K-V operation - to retrieve a document by ID
	try:
		result = cb_coll.get(key)
		print("\nFetch document success. Result: ", result.content_as[dict])
	except CouchbaseException as e:
		print(e)
	# Simple K-V operation - to update a document by ID
	# try:
	# 	sample_airline["name"] = "Couchbase Airways!!"
	# 	result = cb_coll.replace(key, sample_airline)
	# 	print("\nUpdate document success. CAS: ", result.cas)
	# except CouchbaseException as e:
	# 	print(e)
	# Simple K-V operation - to delete a document by ID
	# try:
	# 	result = cb_coll.remove(key)
	# 	print("\nDelete document success. CAS: ", result.cas)
	# except CouchbaseException as e:
	# 	print(e)
except Exception as e:
	traceback.print_exc()


if __name__ == '__main__':
    app.run(debug=True, port=3001)