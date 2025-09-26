# team_imabari

仮想環境を新しく作る手順

C:\Users\yukio\Desktop\team_imabari フォルダで、次を実行してください：

py -3.13 -m venv .venv


これで .venv フォルダが作られます。

仮想環境を有効化する

作成後に有効化します：

.\.venv\Scripts\Activate.ps1


→ 成功すると、PowerShell の先頭に (.venv) が付きます。
例：

(.venv) PS C:\Users\yukio\Desktop\team_imabari>

依存パッケージを入れる

有効化した状態で Flask を入れます：

pip install --upgrade pip
pip install flask

Flask アプリ起動

最後に：

python app.py


ブラウザで http://127.0.0.1:5000
 を開けばアプリが動きます 🚀



venvに入る
.\.venv\Scripts\Activate.ps1

実行
python app.py

復帰
deactivate