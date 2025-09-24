# app.py
from flask import Flask, render_template
import os

# Flaskにtemplates/staticの場所を明示（同階層にある想定）
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    # 必要ならここでデータを渡せます: render_template("index.html", spots=...)
    return render_template("index.html")

if __name__ == "__main__":
    # 環境変数 PORT があればそれを使い、なければ 5000
    port = int(os.environ.get("PORT", 5000))
    # 開発中は debug=True で自動リロード
    app.run(host="127.0.0.1", port=port, debug=True)
