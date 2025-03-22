from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    session,
    redirect,
    url_for
)

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/gpt', methods=['GET'])
def gpt():
    return render_template('gpt.html')

@app.route('/permutasi', methods=['GET'])
def permutasi():
    return render_template('materipermutasi.html')

@app.route('/gabungan', methods=['GET'])
def gabungan():
    return render_template('materigabungan.html')

# jangan diganggu
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

