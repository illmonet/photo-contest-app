from flask import Flask, render_template, request

app = Flask(__name__)

entries = {
    "106": "Sandhyamol PK",
    "107": "keerthana jobin",
    "109": "Saranya Manoj",
    "119": "Leenu Binoy",
    "120": "Shalu Rajendraprasad",
    "121": "Renju Shalu",
    "123": "Ambly Jomon",
    "133": "Krishnanand MR",
    "134": "Linimol Igi",
    "137": "Sathi Ravi",
    "144": "vineetha ps",
    "159": "Leenu Akhil",
    "165": "Sandrakrishna s",
    "169": "Anugraha Manesh",
    "176": "Ajeesh T V",
    "188": "Arya Asish",
    "194": "SNEHA LALRAJ",
    "196": "ARYA SURESH",
    "197": "Akhila Vijayan",
    "199": "Sreedevi Thalumkal"
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entry_no = request.form.get('entry_no')
        name = entries.get(entry_no)
        if name:
            return render_template('result.html',
                                   success=True,
                                   name=name,
                                   entry_no=entry_no)
        else:
            return render_template('result.html', success=False)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
