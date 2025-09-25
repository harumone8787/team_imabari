from flask import Flask, render_template
import os

# Flaskアプリケーション生成（templates/static を同階層に置く想定）
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    # 必要ならここでデータを渡すことも可能
    return render_template("index.html")

if __name__ == "__main__":
    # 環境変数 PORT があれば使い、なければ 5000 を使う
    port = int(os.environ.get("PORT", 5000))
    # 開発中は debug=True で自動リロード
    app.run(host="127.0.0.1", port=port, debug=True)
