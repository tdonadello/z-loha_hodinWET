from flask import Flask, render_template, request, redirect, url_for #importujeme flask a funkce v něm

app = Flask(__name__) #vytvoření flask aplikace


@app.route("/")
def home():
 return render_template("index.html")

@app.route("/form")
def form():
   py_var = request.args.get("html_name")
   return render_template("form.html", jinja_var=py_var)

# @app.routr("/result")
# def result():
#    py_var = request.form.get("html_name")
#    return redirect(url_for("result", jinja_var=py_var))
# name = request.args.get("name") 
# input_class = request.args.get("class")
# message = request.args.get("message")

#     return redirect(url_for("result", name=name, form_class=input_class, message=message))
    


# 
# input_class = request.form.get("class")
# message = request.form.get("message")

#     
    





if __name__ == "__main__": #kontroluje jestli je přímo spouštěn
    app.run(debug=True) #spouštění flaskové aplikace


# var = proměnná
# args = argumenty