from flask import Flask, render_template, request
import io
import csv

app = Flask(__name__)

# def generate_username(prefix, index, padding):
#     if len(str(index)) == 1:
#         return f"{prefix}{index}"
#     else:
#         return f"{prefix}{index:02}"

# def generate_username(prefix, sequence_number):
#     return f"{sequence_number:02d}"
def generate_username(prefix, sequence_number):
    return f"{prefix}{sequence_number:02d}"

def generate_password():
    return "Cloudera123"

def generate_workspace():
    return "pkoworkspace"

def process_participants(input_data, username_prefix, start_index, end_index):
    participant_names = input_data.strip().split('\n')
    padding = len(str(end_index))

    output_rows = []
    for index, name in enumerate(participant_names, start=start_index):
        username = generate_username(username_prefix, index)
        password = generate_password()
        workspace = generate_workspace()

        output_rows.append({
            'Participant Name': name,
            'Username': username,
            'Password': password,
            'Workspace Name': workspace
        })

    return output_rows

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        username_prefix = request.form['username_prefix']

        if file and file.filename.endswith('.txt'):
            input_data = file.read().decode('utf-8')
            output_rows = process_participants(input_data, username_prefix, 1, 150)

            return render_template('output.html', rows=output_rows, username_prefix=username_prefix)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
