from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')


 # so what I want to do is to get the data that I choose from the request args function.
 #  pull that Data out of the json using a another function lower downself.
 #  and then return my DATAbyName page again and fill in my jinja variables to show the data that I have pulled
 # in the method you need to give it the data set and the name of the guy. Check if they are the same. and then pull out the data and return it as a string so that I can put it into my jinja variables.
# def getCitation(medalList,recipiantName):
#
#     citation=""
#     latitude=0
#     longitude=0
#     location=""
#     date=""
#
#     for n in medalList:
#         if n["Name"] == recipiantName:
#             citation= n["awarded"]["citation"]
#             latitude= n["awarded"]["location"]["latitude"]
#             longitude= n["awarded"]["location"]["longitude"]
#             date= n["date"]["full"]
#     return str(citation)



@app.route("/DataByName")
def render_DataByName():
    with open('static/medal_of_honor.json') as medal_data:
        medalList = json.load(medal_data)
    if 'Name' in request.args:
        recipiantName = request.args["Name"]
        return render_template('DataByName.html', response_options= getData(medalList), citation= getCitation(medalList,recipiantName), recipiantName = recipiantName,longitude=getLongitude(medalList,recipiantName), latitude=getLatitude(medalList,recipiantName), date= getDate(medalList,recipiantName), location=getLocation(medalList,recipiantName))

        # return render_template('DataByName.html')
    return render_template('DataByName.html', response_options=getData(medalList))

@app.route("/graphPage")
def render_graphPage():
    return render_template('graphPage.html')


def getData(medalList):
    names = []
    options = ""
    for c in medalList:
        if c["name"] not in names:
            names.append(c["name"])
            options += Markup("<option value=\"" + c["name"] + "\">" + c["name"] + "</option>")
    return options

def getCitation(medalList,recipiantName):

    citation=""

    for n in medalList:
        if n["name"] == recipiantName:
            citation= n["awarded"]["citation"]
    print(citation)
    return str(citation)

def getLongitude(medalList,recipiantName):

    lon=0

    for n in medalList:
        if n["name"] == recipiantName:
            lon=n["awarded"]["location"]["longitude"]
    return str(lon)

def getLatitude(medalList,recipiantName):

    lat=0

    for n in medalList:
        if n["name"] == recipiantName:
            lat= n["awarded"]["location"]["latitude"]
    return str(lat)

def getDate(medalList,recipiantName):

    date="6"

    for n in medalList:
        if n["name"] == recipiantName:
            date= n["awarded"]["date"]["full"]
    return date

def getLocation(medalList,recipiantName):

    location="here"

    for n in medalList:
        if n["name"] == recipiantName:
            location= n["awarded"]["location"]["name"]
    return location



if __name__=="__main__":
    app.run(debug=True, port=54321)
