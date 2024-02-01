from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def hello_name(name):
    return render_template(hi.txt)

@app.route('/products')
def hello(name):
    return ('Hello %s!' % name)

if __name__ == '__main__':
    app.run(debug=True,port=8000)