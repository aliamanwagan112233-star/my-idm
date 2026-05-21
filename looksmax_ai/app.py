import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    # Fake report logic jo bilkul real premium apps jaisi dikhti hai
    eye_structures = ["Hunter Eyes (Rare)", "Almond Eyes (Optimal)", "Positive Canthal Tilt"]
    jaw_structures = ["Chiseled & Defined", "Square Cut (High Angularity)", "Symmetrical"]
    
    report = {
        "facial_symmetry": f"{random.randint(88, 97)}%",
        "eye_structure": random.choice(eye_structures),
        "jawline_score": random.choice(jaw_structures),
        "potential_score": f"{random.uniform(8.4, 9.7):.1f}/10"
    }
    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=True)
