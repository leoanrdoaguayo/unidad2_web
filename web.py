from flask import Flask, render_template, request, redirect
from triangle import rectangulo_area

app = Flask(__name__)

@app.route('/')
def hello() -> '302':
    return redirect('/entry')

@app.route('/entry')
def entry_page()-> 'html':
    return render_template('entry.html', the_tittle='The Practice of Unity 2')

@app.route('/area', methods=['POST'])
def area()->'html':
    a = float(request.form['a'])
    b = float(request.form['b'])
    tittle = 'The result of area  is: '
    result= rectangulo_area(a,b)
    return render_template('result.html',
                           the_tittle = tittle,
                           the_a = a,
                           the_b = b,
                           the_result = result)




app.run(debug=True)
