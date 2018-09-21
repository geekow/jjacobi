from flask import Flask, render_template

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def run():
    app.run(debug=True, port=5000)


def cli():
    print("Usage...")


if __name__ == "__main__":
    run()
