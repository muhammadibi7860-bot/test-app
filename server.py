from flask import Flask

app = Flask(__name__)

# Feature 1
@app.route("/devops")
def devops_team():
    return "Welcome to DevOps team"

# Feature 2
@app.route("/data-eng")
def data_eng_team():
    return "Welcome to Data Eng team"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
