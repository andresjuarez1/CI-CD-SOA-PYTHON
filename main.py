from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/welcome')
def welcome():
    return 'Hola mundo a todos desde master'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
