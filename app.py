from flask import Flask, render_template, send_from_directory ,request
import pandas as pd
import os

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    csv_file = request.files['csv_file']
    text_data = convert_csv_to_text(csv_file)
    
    return render_template('download.html', text_data=text_data)

def convert_csv_to_text(csv_file):
    text_file = 'file.txt'

    # Đọc dữ liệu từ file CSV bằng pandas
    df = pd.read_csv(csv_file)

    # Căn chỉnh cột trong DataFrame
    df_formatted = df.to_string(index=False)

    with open(text_file, 'w', encoding='utf-8') as file:
        file.write(df_formatted)

    return df_formatted

@app.route('/download')
def download():
    text_file = 'file.txt'
    directory = os.getcwd()  # Lấy đường dẫn thư mục gốc

    return send_from_directory(directory, text_file, as_attachment=True)

if __name__ == '__main__':
    app.run()