from flask import Flask, render_template, request

app = Flask(__name__)

# Valid Entry Numbers
valid_entries = {
    106, 107, 109, 119, 120, 121, 123, 133, 134, 137,
    144, 159, 165, 169, 176, 188, 194, 196, 197, 199
}

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        try:
            entry_no = int(request.form['entry_no'])
            if entry_no in valid_entries:
                message = "അഭിനന്ദനങ്ങൾ! നിങ്ങൾ വിജയിച്ചിരിക്കുന്നു! 🎉"
            else:
                message = "ക്ഷമിക്കണം, നിങ്ങൾ വിജയിച്ചില്ല. വീണ്ടും ശ്രമിക്കൂ."
        except ValueError:
            message = "ദയവായി ശരിയായ 3 അക്ക നമ്പർ നൽകൂ."
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
