

# from MangoDbConnection import client,coll_pwskills,db
import mangoDBconnection as pj
db=pj.client["pwskills"]
coll_pwskills =db["my_records"]

try:
    print("Database :: >> ",(db))
    
    # for i in coll_pwskills.find():
    #     print(i)
      
    # print("@==============================================================")    
    # print(list(coll_pwskills.find({"name":"prashant"})))
        
      
    # print("@==============================================================")    
    # for i in coll_pwskills.find({"name":"prashant"}):
    #     print(i)
        
    # print("@==============================================================")    
    # for i in coll_pwskills.find({"class":"Data Science"}):
    #     print(i)
    #     print("@==============================================================\n\n")    
        
    # print("\n@======================= Greter Than Equal 4 =======================================\n")    
    # for i in coll_pwskills.find({"_id": {"$gte": "2"}}):
    #     print(i)
    #     print("@==============================================================")    

    # coll_pwskills.update_many({"class":"Data Science"},{"$set":{"class":"Python With Data Science "}})
    # coll_pwskills.update_many({"class":"Python With Data Science "},{"$set":{"class":"Data Science "}})
    
    print("\n\n@========================== Change Class Name ====================================\n\n")    

    for i in coll_pwskills.find({"_id": {"$gte": "1"}}):
        coll_pwskills.update_many({"class":"Data Science"},{"$set":{"class":"Python With Data Science"}})
           
    for i in coll_pwskills.find({"_id": {"$gte": "1"}}):
        print(i)
        print("@==============================================================")    

    
    # client.admin.command('ping')
    print("\n\n@============================= END =================================@")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
     
    