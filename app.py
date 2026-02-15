from flask import Flask, jsonify
import scanner

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <body style="font-family:sans-serif; background:#121212; color:white; text-align:center;">
        <h1>Solana Brute Automation</h1>
        <div style="font-size:24px; border:1px solid #333; display:inline-block; padding:20px;">
            <p>Checked: {scanner.stats['checked']}</p>
            <p style="color:#00ff00;">Found: {scanner.stats['found']}</p>
            <p style="font-size:14px;">Last: {scanner.stats['last_address']}</p>
        </div>
        <script>setTimeout(() => location.reload(), 1000);</script>
    </body>
    """

if __name__ == '__main__':
    scanner.start_threads(5)
    app.run(host='0.0.0.0', port=347)
