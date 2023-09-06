from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Define a simple API endpoint
@app.route('/api/data', methods=['GET'])
def api_data():
    data = {'message': 'Hello from the API!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
