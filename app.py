from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')  # ✅ HTML 렌더링

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
