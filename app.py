from flask import Flask, render_template, request, redirect, url_for
import requests
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)

moviekeys = { "apikey": "fe9d9489a53300b8da850e6349475c52", "read_access_token": "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmZTlkOTQ4OWE1MzMwMGI4ZGE4NTBlNjM0OTQ3NWM1MiIsInN1YiI6IjY1YTU5NWE2ZDA1YTAzMDBjOGE5ZWJjNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ArysHTlTdStAaVZDOpAoFLDyZkcp4CL3jMgfbpnVdyY" }

headers = {"Authorization": f"Bearer {moviekeys['read_access_token']}"}


def get_discovery(pagenum):
    response = requests.get(f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={pagenum}",headers=headers)
    results = response.json()
    return results

@app.route('/')
@cross_origin()
def index():
    pagenum = request.args.get('page') if request.args.get('page') else 1
    
    discovery = get_discovery(pagenum)
    
    return render_template('index.html',discovery=discovery,access_token=moviekeys["read_access_token"])



if __name__ == "__main__":
    #get_discovery()
    app.run(debug=True)