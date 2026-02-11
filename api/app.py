from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    return jsonify({"status": "Logistics API Running"})

if __name__ == '__main__':
    app.run(debug=True)
