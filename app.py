from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/get-font-family', methods=['POST'])
def get_font_family():
    try:
        url = request.json.get('url')
        print(f"URL received: {url}")

        # Ensure URL is not None or empty
        if not url:
            return jsonify({'error': 'URL is missing'}), 400

        print(['shot-scraper javascript', url, '-i /getFonts.js'])
        result = subprocess.run(
            ['shot-scraper', 'javascript', url, '-i', 'getFonts.js'],
            capture_output=True, text=True
        )

        
        if result.returncode != 0:
            return jsonify({'error': result.stderr}), 500

        return jsonify({'fontFamily': result.stdout.strip()})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
