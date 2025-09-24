from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # 必要になれば将来ここでDBやAPIからデータを渡す
    return render_template("index.html")

if __name__ == "__main__":
    # 開発中は debug=True で自動リロード
    app.run(debug=True)
