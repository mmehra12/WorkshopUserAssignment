from flask import Flask, render_template, request, redirect, url_for
from io import StringIO

app = Flask(__name__)

def generate_username(sequence_number):
    return f"pkou{sequence_number:02d}"

def generate_password():
    return "Cloudera123"

def generate_workspace():
    return "pkoworkspace"

def process_text_file(file):
    lines = file.read().splitlines()
    output = StringIO()

    for index, line in enumerate(lines, start=1):
        participant_name = line.strip()
        username = generate_username(index)
        password = generate_password()
        workspace = generate_workspace()
        
        output.write(f"<tr><td>{participant_name}</td><td>{username}</td><td>{password}</td><td>{workspace}</td></tr>")

    return output.getvalue()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        
        processed_data = process_text_file(file)
        
        return f"""
        <h3>Processed Data:</h3>
        <table>
            <thead>
                <tr>
                    <th>Participant Name</th>
                    <th>Username</th>
                    <th>Password</th>
                    <th>Workspace Name</th>
                </tr>
            </thead>
            <tbody>
                {processed_data}
            </tbody>
        </table>
        """
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

