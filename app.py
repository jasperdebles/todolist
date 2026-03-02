from flask import Flask 

app = Flask(__name__)

@app.route('/')
def test(): 
    return 'This is a test for a to do list'

if __name__ == '__main__':  
    app.run(debug=True) 