from flask import Flask, jsonify
app = Flask (__name__)

@app.route("/")
def hello():
    return jsonify({"key": "value"}), 200

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/default/<name>')
#     def default(name):
#         return  