from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, world!"


def run():
    app.run(debug=True, port=5000)


def cli():
    print("Usage...")


if __name__ == "__main__":
    run()
