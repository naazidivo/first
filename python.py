
from flask import Flask,request,jsonify

de = {'name': 'samir','age':13}
app =Flask( "__name__")


@app.route('/',methods =['GET'])
def hello ():
    
    name = str(request.args['name'])
    de.update({f"s{name}": name})
    return de




if __name__ == "__main__":
    app.run(debug=True)