from flask import Flask

app = Flask(__name__)

@app.route('/teste')
def teste():
    return 'Teste de rota com Flask'

if __name__ == '__main__':
    app.run(debug=True)