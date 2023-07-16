from flask import Flask, render_template
import wiki

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/average/<code>/<date>", methods=['GET'])
def upload_image():
    return render_template('index.html')

@app.route("/average/<code>/<date>", methods=['GET'])
def wiki(predict):
    return wiki.get_wiki(predict)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)