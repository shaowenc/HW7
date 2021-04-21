import json
import requests
import secrets as secrets

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    baseurl = "https://api.nytimes.com/svc/topstories/v2/technology.json?"
    param = {'api-key': secrets.api_key}
    response = requests.get(baseurl, param)
    results = response.json()

    topstory_1 = results['results'][0]['title']
    topstory_2 = results['results'][1]['title']
    topstory_3 = results['results'][2]['title']
    topstory_4 = results['results'][3]['title']
    topstory_5 = results['results'][4]['title']

    return render_template('topstories.html', 
        topstory_1=topstory_1, topstory_2=topstory_2, topstory_3=topstory_3, topstory_4=topstory_4, topstory_5=topstory_5)

if __name__ == '__main__':  
    app.run(debug=True)
