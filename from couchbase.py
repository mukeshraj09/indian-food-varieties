from couchbase.cluster import Cluster, ClusterOptions, QueryOptions
from couchbase_core.cluster import PasswordAuthenticator

# Connect to Couchbase cluster
cluster = Cluster('couchbase://localhost', ClusterOptions(
    PasswordAuthenticator('username', 'password')
))

# Open a bucket
bucket = cluster.bucket('bucket_name')

# Get a default collection
collection = bucket.default_collection()

# Perform a N1QL query
query = 'SELECT * FROM bucket_name WHERE type = $type AND status = $status LIMIT 10'
result = cluster.query(query, QueryOptions(named_parameters={"type": "ticket", "status": "open"}))

# Process the results
for row in result:
    print(row)

# Disconnect from the cluster
cluster.disconnect()