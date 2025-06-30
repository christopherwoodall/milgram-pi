"""
Runs a local http flask webserver calls the tools in `tools.py`.
"""
import os
import RPi.GPIO as GPIO

from flask import Flask, request, jsonify

from tools.relay import toggle as toggle_relay


app = Flask(__name__)
PIN = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)


@app.route('/activate', methods=['POST'])
def activate():
    data = request.json
    duration = data.get('duration', 1)

    toggle_relay(PIN, timeout=duration)

    return jsonify({"status": "success", "message": f"Relay activated for {duration} seconds"})


def main():
    """
    Starts the Flask web server.
    """
    port = int(os.getenv("MILGRAM_PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    GPIO.cleanup()


if __name__ == "__main__":
    main()
