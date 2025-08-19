from flask import Flask, request, render_template, jsonify
import json
import os
import pandas as pd
import datetime
import math

app = Flask(__name__)

DATA_FILE = 'faculty_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def parse_faculty_schedule(file_path):
    df = pd.read_excel(file_path, header=None)
    
    name = df.iloc[6, 2] if not pd.isna(df.iloc[6, 2]) else ''
    code = df.iloc[6, 10] if not pd.isna(df.iloc[6, 10]) else ''
    if not name or not code:
        return None
    
    designation = df.iloc[7, 2] if not pd.isna(df.iloc[7, 2]) else ''
    room = df.iloc[7, 10] if not pd.isna(df.iloc[7, 10]) else ''
    email = df.iloc[8, 2] if not pd.isna(df.iloc[8, 2]) else ''
    
    undergrad_cols = [1, 3, 5, 7, 9, 11]
    undergrad_times = [str(df.iloc[12, col]) if not pd.isna(df.iloc[12, col]) else '' for col in undergrad_cols]
    schedule_under = {}
    undergrad_days_rows = range(13, 18)
    for r in undergrad_days_rows:
        day = str(df.iloc[r, 0]) if not pd.isna(df.iloc[r, 0]) else ''
        if day:
            slots = [str(df.iloc[r, col]) if not pd.isna(df.iloc[r, col]) else '' for col in undergrad_cols]
            schedule_under[day] = slots
    
    grad_cols = [1, 5, 9]
    grad_times = [str(df.iloc[21, col]) if not pd.isna(df.iloc[21, col]) else '' for col in grad_cols]
    schedule_grad = {}
    grad_days_rows = range(22, 25)
    for r in grad_days_rows:
        day = str(df.iloc[r, 0]) if not pd.isna(df.iloc[r, 0]) else ''
        if day:
            slots = [str(df.iloc[r, col]) if not pd.isna(df.iloc[r, col]) else '' for col in grad_cols]
            if any(slots):
                schedule_grad[day] = slots
    
    return {
        'code': str(code),
        'name': str(name),
        'designation': str(designation),
        'room': str(room),
        'email': str(email),
        'undergrad': {
            'times': undergrad_times,
            'schedule': schedule_under
        },
        'grad': {
            'times': grad_times,
            'schedule': schedule_grad
        }
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    data = load_data()
    found = None
    for code, fac in data.items():
        if query == fac['name'].lower() or query == code.lower():
            found = fac
            break
    if not found:
        return render_template('index.html', error='Faculty not found')
    
    today = datetime.date.today().strftime('%a').upper()
    return render_template('schedule.html', faculty=found, today=today)

@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get('query', '').lower()
    data = load_data()
    suggestions = []
    for code, fac in data.items():
        if query in fac['name'].lower() or query in code.lower():
            suggestions.append({'name': fac['name'], 'code': code})
    return jsonify(suggestions)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        files = request.files.getlist('files')
        data = load_data()
        for file in files:
            if file and file.filename.endswith('.xlsx'):
                temp_path = os.path.join('uploads', file.filename)
                os.makedirs('uploads', exist_ok=True)
                file.save(temp_path)
                try:
                    fac_data = parse_faculty_schedule(temp_path)
                    if fac_data:
                        data[fac_data['code']] = fac_data
                except Exception as e:
                    print(f"Error parsing {file.filename}: {e}")
                finally:
                    os.remove(temp_path)
        save_data(data)
        return render_template('admin.html', message='Files uploaded and data updated')
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)