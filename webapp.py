from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/DataByName")
def render_DataByName():
    with open('static/medal_of_honor.json') as medal_data:
        medalList = json.load(medal_data)
    return render_template('DataByName.html', response_options="Jerry")








if __name__=="__main__":
    app.run(debug=False, port=54321)
