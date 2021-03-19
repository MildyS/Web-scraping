from flask import Flask, render_template, redirect, url_for
from app import main
from app2 import main2

app = Flask(__name__)

@app.route("/")
def welcome():
    suhrn1 = main()
    suhrn2 = main2()
    return render_template("index.html", titul1=suhrn1[0], datum1=suhrn1[1], dlzka1=suhrn1[2], titul2=suhrn2[0], datum2=suhrn2[1], dlzka2=suhrn2[2]);


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=True, debug=True)