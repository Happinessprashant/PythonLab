
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://prashantjadhav9089:pwskills@cluster0.yajlqt0.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

db=client.test
# Send a ping to confirm a successful connection
try:
    print("Database :: >> ",db)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
    

