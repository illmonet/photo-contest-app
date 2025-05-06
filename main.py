from flask import Flask, render_template, request
import os

app = Flask(__name__)

entry_numbers = {
    106, 107, 109, 119, 120, 121, 123, 133, 134, 137,
    144, 159, 165, 169, 176, 188, 194, 196, 197, 199
}

USED_FILE = "used.txt"

def load_used_numbers():
    if not os.path.exists(USED_FILE):
        return set()
    with open(USED_FILE, "r") as f:
        return set(int(line.strip()) for line in f if line.strip().isdigit())

def mark_used(number):
    with open(USED_FILE, "a") as f:
        f.write(f"{number}\n")

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        user_input = request.form.get("entry_no", "").strip()
        if user_input.isdigit():
            entry_no = int(user_input)
            used = load_used_numbers()
            if entry_no in entry_numbers:
                if entry_no in used:
                    message = "ക്ഷമിക്കണം, ഈ നമ്പർ ഇതിനകം ഉപയോഗിച്ചിരിക്കുന്നു."
                else:
                    mark_used(entry_no)
                    message = "അഭിനന്ദനങ്ങൾ! നിങ്ങൾ വിജയിച്ചിരിക്കുന്നു!"
            else:
                message = "ക്ഷമിക്കണം, നിങ്ങൾ വിജയിച്ചില്ല."
        else:
            message = "ദയവായി ശരിയായ 3-അക്കം നമ്പർ നൽകുക."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
