from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return"Your website goes here."
if __name__=="__main__":
    app.run(debug=True)
