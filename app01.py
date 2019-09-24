from random import choice, randint

from flask import Flask, render_template

app = Flask(__name__)


# @ : デコレータ（関数に装飾することができる機能(pythonの機能)）
# app.route : ルーティング(Flaskの機能)
@app.route('/hello')
def hello():
    return '<h1>Hello world</h1>'  # 動的にHTMLを更新


@app.route('/goodbye')
def goodbye():
    return 'goodbye'


@app.route('/add/<a>/<b>')
def add(a, b):
    return str(int(a) + int(b))


@app.route('/omikuji')
def omikuji():  # ←ViewFunction
    results = ['大吉', '吉', '凶']
    idx = randint(0, len(results) - 1)
    result = results[idx]

    return render_template('omikuji.html', result=result)


@app.route('/omikuji_ans')
def omikuji_ans():  # ←ViewFunction
    運 = ['大吉', '吉', '凶']
    result = choice(運)
    return '今日の運勢は...' + result


if __name__ == '__main__':
    app.run(debug=True, port=7777)  # debug=Trueデバックモードを起動。サーバを落とさなくても変更が更新される。port=開くポートを指定
