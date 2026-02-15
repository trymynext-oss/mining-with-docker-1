from flask import Flask, jsonify
import scanner

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Solana Automation Active</h1>
    <p>Checked: {scanner.stats['checked']}</p>
    <p>Found: {scanner.stats['found']}</p>
    <p>Last: {scanner.stats['last_address']}</p>
    <script>setTimeout(() => location.reload(), 2000);</script>
    """

@app.route('/stats')
def get_stats():
    return jsonify(scanner.stats)

if __name__ == '__main__':
    scanner.start_threads(5) # Start 5 worker threads
    app.run(host='0.0.0.0', port=347)
