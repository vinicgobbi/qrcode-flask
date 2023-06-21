from flask import Flask, render_template, request, redirect, url_for
import pyqrcode
import png

app = Flask(__name__)

@app.route("/")
@app.route("/menu")
def main():
    return render_template("index.html")

@app.route("/link")
def link():
    return render_template("link.html")

@app.route("/email")
def email():
    return render_template("email.html")

@app.route("/generate_link", methods=["GET", "POST"])
def gen_link():
    link = request.form['link']
    if not link:
        return render_template("erro.html")
    else:
        if request.method == "POST":
            qrcode = pyqrcode.create(link)
            qrcode.png("./static/qrcode.png", scale=8)
            return render_template("qrcode.html", qrcode=qrcode)
        else:
            return redirect(url_for("link"))
        

@app.route("/generate_email", methods=["GET", "POST"])
def gen_email():
    destinatario = request.form['destinatario']
    assunto = request.form['assunto']
    texto = request.form['texto']
    if not destinatario or not assunto or not texto:
        return render_template("erro.html")
    else:
        if request.method == "POST":
            qrcode = pyqrcode.create(f"MATMSG:TO:{destinatario};SUB:{assunto};BODY:{texto};;")
            qrcode.png("./static/qrcode.png", scale=8)
            return render_template("qrcode.html", qrcode=qrcode)

app.run(debug=True)