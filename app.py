from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.post('/')
def index_post():
    form = request.form
    name = form['name']
    return render_template('greetings.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
