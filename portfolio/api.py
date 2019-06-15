from django.shortcuts import Django , render , jsonify

import requests
from key import key

app = Django(__name__)

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"

@app.route("/", methods=["GET"])
def retreive():
    return render('layout.html')

@app.route("/sendRequest/<string:query>")
def results(query):

    url = "https://www.google.com"
    return jsonify({'result': url})

if __name__ == "__main__":
    app.run(debug=True)
