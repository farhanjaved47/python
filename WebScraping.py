"""
Farhan Javed - 11-20-2019
Basic Web scraping tutorial with example for working with JSON.
Also includes examples for working with HTML and XML files.
"""


import urllib.request as request
import json
from html.parser import HTMLParser
import xml.dom.minidom
#  Python JSON class : https://docs.python.org/3/library/json.html


def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
        count = theJSON["metadata"]["count"]
        print(str(count) + " events recorded")

        for i in theJSON["features"]:
            print(i["properties"]["place"])
        print("-----------------\n")

        for i in theJSON["features"]:
            if i["properties"]["mag"] >= 4.0:
                print("%2.1f" %i["properties"]["mag"], i["properties"]["place"])
        print("-----------------\n")

        print("Events that were felt: ")
        for i in theJSON["features"]:
            feltReports = i["properties"]["felt"]
            if feltReports != None:
                print("%2.1f" %i["properties"]["mag"], i["properties"]["place"],
                      " reported " + str(feltReports) + " times")


def fetchHTML():

    web_url = request.urlopen("http://www.google.com")
    print("result code : " + str(web_url.getcode()))
    data = web_url.read()
    print(data)


def workingWithJSON():

    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    urlLink = request.urlopen(urlData)
    statusCode = urlLink.getcode()

    if statusCode == 200:
        data = urlLink.read()
        printResults(data)
    else:
        print("Received error code : " + statusCode)

metacount = 0

class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        print("Encountered comment: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == "meta":
            metacount += 1
        print("Encountered tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

        if attrs.__len__() > 0:
            print("\tAttributes: ")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    def handle_endtag(self, tag):
        print("Encountered tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered some data: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])


def htmlParsing():

    parser = MyHTMLParser()
    file = open("samplehtml.html")
    if file.mode == 'r':
        contents = file.read()
        parser.feed(contents)

    print("Total meta tags found " + str(metacount))


def xmlParsing():
    doc = xml.dom.minidom.parse("samplexml.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    skills = doc.getElementsByTagName("skill")
    print("%d skills : " %skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)

    skills = doc.getElementsByTagName("skill")
    print("%d skills : " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))


def main():

    fetchHTML()
    workingWithJSON()
    htmlParsing()
    xmlParsing()


if __name__ == "__main__":
    main()