
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://prashantjadhav9089:pwskills@cluster0.yajlqt0.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

db=client.test
# Send a ping to confirm a successful connection

if __name__=="__main__":
    try:
        print("Database :: >> ",(db))
        # Database Name
        db=client["pwskills"]
        coll_pwskills =db["my_records"]
        # Data is created
        # data={
        #     "name":"prashant",
        #     "class":"data science master",
        #     "time":"flexi"
        # }
        
        # # # in Database create Table
        # # # insert records in the table
        # coll_pwskills.insert_one(data)
        
        # # # Second record is Created
        # data1={
        #     "mail_id":"prashantjadhav9089@gmail.com",
        #     "phno":845907108,
        #     "addr":"Mangoli"
        # }
        # # 2nd record insert into table
        
        
        # coll_pwskills.insert_one(data1)
        
        # # Third record is Created
        # data2=[
        #     {"name":"prashant","class":"Data Science","time":"Moringing : 5:30"},
        #     {"name":"Skashi","class":"Data Science","time":"Moringing : 5:30"},
        #     {"name":"Pruthivi","class":"Data Science","time":"Moringing : 5:30"},
        #     {"name":"prathamesh","class":"Data Science","time":"Moringing : 5:30"},
        #     {"name":"Vaibhav","class":"Data Science","time":"Moringing : 5:30"},
        #     {"name":"Jay","class":"Data Science","time":"Moringing : 5:30"},
        #     {"name":"Sourbhav","class":"Data Science","time":"Moringing : 5:30"},
        #     {"name":"swanand","class":"Data Science","time":"Moringing : 5:30"},
        #     {"name":"samarat","class":"Data Science","time":"Moringing : 5:30"},
        #     {"name":"abc","class":"Data Science","time":"Moringing : 5:30"}
            
        # ]
        # # 3rd record insert into table
        
        
        # coll_pwskills.insert_many(data2)
        
        # Fourth record is Created
        data3=[
            {"_id":"1","name":"prashant","class":"Data Science","time":"Moringing : 5:30"},
            {"_id":"2","name":"Skashi","class":"Data Science","time":"Moringing : 5:30"},
            {"_id":"3","name":"Pruthivi","class":"Data Science","time":"Moringing : 5:30"},
            {"_id":"4","name":"prathamesh","class":"Data Science","time":"Moringing : 5:30"},
            {"_id":"5","name":"Vaibhav","class":"Data Science","time":"Moringing : 5:30"},
            {"_id":"6","name":"Jay","class":"Data Science","time":"Moringing : 5:30"},
            {"_id":"7","name":"Sourbhav","class":"Data Science","time":"Moringing : 5:30"},
            {"_id":"8","name":"swanand","class":"Data Science","time":"Moringing : 5:30"},
            {"_id":"9","name":"samarat","class":"Data Science","time":"Moringing : 5:30"},
            {"_id":"10","name":"abc","class":"Data Science","time":"Moringing : 5:30"}
            
        ]
        # 4th record insert into table
        
        
        coll_pwskills.insert_many(data3)
        
        
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    
    except Exception as e:
        print(e)
    

        
