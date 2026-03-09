from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def root_page():
    with open("cocio.html", "r") as file:
        return file.read()


@app.route("/info")
def test():
    return "<h1>Hello this is test</h1>"


@app.route("/favicon.ico")
def favicon():
    return send_file("./images/cocio-seeklogo.svg")


@app.route("/cocio.png")
def cocio_logo_png():
    return send_file("./images/cocio-seeklogo.png")


@app.route("/cocio.svg")
def cocio_logo_svg():
    return send_file("./images/cocio-seeklogo.svg")


# if __name__ == "__main__":
#     print("Starting Server")
#     app.run(host="0.0.0.0", port=8000, ssl_context=("cert.pem", "cert.key"))
