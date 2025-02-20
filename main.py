from flask import Flask, request, jsonify
from model_loader import generate_code_completion

app = Flask(__name__)

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    """API to get AI-generated code completions."""
    data = request.json
    input_code = data.get("input_code", "")

    if not input_code:
        return jsonify({"error": "No input code provided"}), 400

    suggestion = generate_code_completion(input_code)
    return jsonify({"suggestion": suggestion})

if __name__ == '__main__':
    app.run(debug=True)
