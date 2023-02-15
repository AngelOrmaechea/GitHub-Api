from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

url = "https://api.github.com"

@app.route("/api/users", methods = ["GET"])
def get_user():
    since = request.args.get("since")
    base = f"{url}/users?since={since}"
    response = requests.get(base)
    return jsonify({
        'users': response.json(),
        'next_page_link': response.headers.get('Link')
    }
    )

@app.route("/api/users/<username>/details", methods = ["GET"])
def Get_user_details(username):
    base = f"{url}/users/{username}"
    response = requests.get(base)
    return jsonify( {
       "user_details" : response.json()
    })
        


@app.route("/api/users/<username>/repos", methods =["GET"])
def Get_user_repos(username):
    base = f"{url}/users/{username}/repos"
    response = requests.get(base)
    return jsonify(
        {
            "repos" : response.json() 
        }
    )





if __name__ == "__main__":
    app.run(debug=True, port=5000)
