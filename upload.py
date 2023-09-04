from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result/<filename>')
def result(filename):
    from s import check_plagiarism_file
    print(filename)
    data = check_plagiarism_file(filename)
    print(data)
    return render_template('result.html', filename=filename, data = data)

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(f"result/{uploaded_file.filename}")


app.run()