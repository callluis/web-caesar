from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

# a form
form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
        
        <form method="post">
            <label>Rotate by:
                <input name="rot" type="text" value="0"/>
            </label>
            <br>
            <label>
                <textarea name="text">{0}</textarea>
            </label>
            <br>
            <input type="submit" value="Submit Query"/>
        </form>

    </body>
</html>
    
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    a = int(request.form['rot'])
    b = request.form['text']
    c = rotate_string(b, a)

    return form.format(c)

app.run()
