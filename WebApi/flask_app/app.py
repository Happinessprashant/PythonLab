from flask import Flask , request , render_template, jsonify

app= Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/math", methods=["POST"])
def math_ops():
        ops=request.form["operation"]
        num1=int(request.form['num1'])
        num2=int(request.form["num2"])
        
        if ops =="add":
            r=num1+num2
            result= (f" Addition of {num1} and {num2} is {r}")
        elif ops =="substract":
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



