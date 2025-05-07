from flask import Flask, render_template, request

app = Flask(__name__)

# Entry database
entries = {
    "106": "Sandhyamol PK",
    "107": "Keerthana Jobin",
    "109": "Saranya Manoj",
    "119": "Leenu Binoy",
    "120": "Shalu Rajendraprasad",
    "121": "Renju Shalu",
    "123": "Ambly Jomon",
    "133": "Krishnanand MR",
    "134": "Linimol Igi",
    "137": "Sathi Ravi",
    "144": "Vineetha PS",
    "159": "Leenu Akhil",
    "165": "Sandrakrishna S",
    "169": "Anugraha Manesh",
    "176": "Ajeesh T V",
    "188": "Arya Asish",
    "194": "Sneha Lalraj",
    "196": "Arya Suresh",
    "197": "Akhila Vijayan",
    "199": "Sreedevi Thalumkal"
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    entry_number = ""
    name = ""
    if request.method == "POST":
        entry_number = request.form.get("entry")
        name = entries.get(entry_number)
        if name:
            result = "valid"
        else:
            result = "invalid"
    return render_template("index.html", result=result, name=name, entry_number=entry_number)

if __name__ == "__main__":
    app.run(debug=True)
