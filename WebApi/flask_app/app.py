from flask import Flask , request , render_template, jsonify

app= Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/postman_data", methods=["POST","GET"])
def math_ops():
        if request.method=="POST":
            ops=request.json["operation"]
            num1=int(request.json['num1'])
            num2=int(request.json["num2"])
        
        if request.method=="GET":
            ops=request.args.get("operation")
            num1=int(request.args.get('num1'))
            num2=int(request.args.get("num2"))
            
        
        if ops =="add":
            r=num1+num2
            result= (f" Addition of {num1} and {num2} is {r}")                                                                                                                                                      
        elif ops =="subtract":
            r=num1-num2
            result= (f"Substration of {num1}  and {num2} is {r}")   
            
        elif ops =="multiply":
            r=num1*num2
            result= (f"Substration of {num1}  and {num2} is {r}")   
            
        elif ops =="divide":
            r=num1/num2
            result= (f"division of {num1}  and {num2} is {r}")   
            
        else:
            result=(f"{ops} is not arithmetic  operation please check valid operation") 
            
        return jsonify(result)  
    
     
@app.route("/math", methods=["POST"])
def math_ops():
        ops=request.form["operation"]
        num1=int(request.form['num1'])
        num2=int(request.form["num2"])
        
        if ops =="add":
            r=num1+num2
            result= (f" Addition of {num1} and {num2} is {r}")
        elif ops =="subtract":
            r=num1-num2
            result= (f"Substration of {num1}  and {num2} is {r}")   
            
        elif ops =="multiply":
            r=num1*num2
            result= (f"Substration of {num1}  and {num2} is {r}")   
            
        elif ops =="divide":
            r=num1/num2
            result= (f"division of {num1}  and {num2} is {r}")   
            
        else:
            result= (f"{ops} is not arithmetic  operation please check valid operation") 
            
        return render_template("results.html", result1=result)   



if __name__=="__main__":
    app.run(host="0.0.0.0",port="9089")



