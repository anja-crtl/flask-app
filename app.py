from flask import Flask, render_template, request
from scripts import script

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    results = None
    if request.method == 'POST':
        results = script.main()
    return render_template("index.html", results=results)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
