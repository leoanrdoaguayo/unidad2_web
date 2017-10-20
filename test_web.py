from flask import Flask, render_template, request, redirect
from module import area_cilindro, volumen_cilindro

app = Flask(__name__)

@app.route('/')
def hello() -> '302':
    return redirect('/entry')

@app.route('/entry')
def entry_page()-> 'html':
    return render_template('entry.html', the_tittle='The Practice of Unity 2')

@app.route('/area', methods=['POST'])
def area()->'html':
    R = float(request.form['R'])
    h = float(request.form['h'])
    tittle = 'The result of area of cilindro is: '
    a= area_cilindro(h,R)
    return render_template('result.html',
                           the_tittle = tittle,
                           the_h = h,
                           the_R = R,
                           the_area = a)




app.run(debug=True)
