from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your Google Custom Search API key and CX (Custom Search Engine ID)
API_KEY = "AIzaSyDx0ln_ucuerNfbi8hQWRnmy7L2w4qUWRU"
CX = "a74a46057f65e4d90"


def fetch_ambulance_data(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch data"}

def process_data(data):
    results = data.get("items", [])
    processed_data = []
    for item in results:
        processed_data.append({
            "title": item["title"],
            "link": item["link"],
            "snippet": item.get("snippet", "No description available")
        })
    return processed_data

@app.route("/")
def home():
    # query = "ambulance services in Kochi"
    query = "ambulance services in allepey"
    raw_data = fetch_ambulance_data(query)
    if "error" in raw_data:
        return f"<h1>Error: {raw_data['error']}</h1>"
    processed_data = process_data(raw_data)
    return render_template("index.html", data=processed_data)

if __name__ == "__main__":
    app.run(debug=True)




