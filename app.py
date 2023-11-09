from flask import Flask

app = Flask(__name__)

call_count = 0

@app.route('/')
def count_calls():
    global call_count
    call_count += 1
    return f'Total calls: {call_count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
