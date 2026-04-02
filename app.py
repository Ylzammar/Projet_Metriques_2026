from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Route pour la page d'accueil (hello.html)
@app.route('/')
def hello():
    return render_template('hello.html')

# Route pour la page contact (texte simple)
@app.route("/contact")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

# Route pour la météo de Paris (JSON)
@app.get("/paris")
def api_paris():
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])
    n = min(len(times), len(temps))
    result = [{"datetime": times[i], "temperature_c": temps[i]} for i in range(n)]
    return jsonify(result)

# NOUVELLE ROUTE : pour la page graphique (graphique.html)
@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
