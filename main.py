from flask import Flask, render_template, request

app = Flask(__name__)

# Securely store Entry data
valid_entries = {
    "106": "Sandhyamol PK",
    "107": "keerthana jobin",
    "109": "Saranya Manoj Plappally",
    "119": "Leenu Binoy",
    "120": "Shalu Rajendraprasad",
    "121": "Renju Valleetta",
    "123": "Ambly Jomon Wembly",
    "133": "Krishnanand MR",
    "134": "Linimol Ligi Koottickal",
    "137": "Sathi Ravi",
    "144": "vineetha ps Thalunkal",
    "159": "Leenu Akhil",
    "165": "Sandrakrishna S Koottickal",
    "169": "Anugraha Manesh Poovanchi",
    "176": "Ajeesh T V  Chathenplappally",
    "188": "Arya Asish Yenthayar",
    "194": "SNEHA LALRAJ Kuttiplangadu",
    "196": "ARYA SURESH KOKKAYAR",
    "197": "Akhila Vijayan",
    "199": "Sreedevi Thalumkal"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    entry_no = request.form.get('entry')
    name = valid_entries.get(entry_no)
    if name:
        first_two_words = ' '.join(name.split()[:2])
        return render_template('result.html', success=True, name=first_two_words, entry_no=entry_no)
    else:
        return render_template('result.html', success=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
