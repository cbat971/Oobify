from flask import Flask, render_template, request, redirect
from oobify import oobify
app = Flask(__name__)

parsed_phrase = "Type what you would like to Oobify into the box above  !"
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # url = request.form['url']
        return redirect(url_for('results'))
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
        phrase_to_parse = request.form["nm"]
        print(oobify(phrase_to_parse))
        global parsed_phrase
        parsed_phrase = oobify(phrase_to_parse)
        return render_template('results.html', parsed_phrase = parsed_phrase)

if __name__ == '__main__':
    app.run(debug=True)