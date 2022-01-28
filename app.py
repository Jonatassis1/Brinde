from flask import Flask, render_template

app = Flask(__name__)

# Criar a 1° pagina do site
# route -> hashtag treinamento
# função

@app.route('/')
def hello_world():  # put application's code here
    return render_template("homepage.html")

@app.route('/brinde/<number_brinde>')
def brinde(number_brinde):
    return render_template("brinde.html", number_brinde=number_brinde)

if __name__ == '__main__':
    app.run(debug=True)