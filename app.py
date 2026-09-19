from flask import Flask, request, jsonify

app = Flask(__name__)

latitude = 0
longitude = 0

@app.route("/")
def home():
    return "GPS Server is running!"

@app.route("/gps", methods=["GET"])
def get_gps():
    return jsonify({
        "latitude": latitude,
        "longitude": longitude
    })

@app.route("/gps", methods=["POST"])
def receive_gps():
    global latitude, longitude

    data = request.get_json()

    latitude = data["latitude"]
    longitude = data["longitude"]

    print("Latitude:", latitude)
    print("Longitude:", longitude)

    return jsonify({
        "status": "received"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
