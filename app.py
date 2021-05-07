# To import the Flask dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)
#The forward slash is commonly known as the 
# highest level of hierarchy in any computer system.
@app.route('/')

def hello_world():
    return 'Hello world'

