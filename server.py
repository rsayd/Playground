from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return  redirect('/play')

@app.route('/play')
def play():
    return render_template('playground1.html')

@app.route("/play/<amount_box>")
def blocks(amount_box):
    gain = int(amount_box)
    return render_template('playground2.html', gain=gain)

@app.route("/play/<amount_box>/<color>")
def colorblocks(amount_box,color):
    gain = int(amount_box)
    color = color
    return render_template('playground3.html', gain=gain, color=color)

if __name__ == "__main__":
    app.run(debug = True)





