import os
import random
import time
import logging

from flask import Flask

app = Flask(__name__)


def generate_log():
    logs = [
        "Success",
        "Created",
        "Failed",
    ]
    return random.choice(logs)


@app.route("/api_1")
def api_call():
    log_message = generate_log()
    print(f"Operation log: {log_message}")
    time.sleep(0.5)  # Wait for half a second.
    return f"completed: {log_message}"


@app.route("/download_external_logs", methods=["GET"])
def download_external_logs():
    external_integration_url = os.getenv("EXTERNAL_INTGERATION_URL")
    external_integration_key = os.getenv("EXTERNAL_INTGERATION_KEY")

    # of course, such a value would never be plainly returned in production,
    # this is only to demonstrate that we are able to read the secret.
    return {
        "external_integration_url": external_integration_url,
        "external_integration_key": external_integration_key,
    }


@app.route("/health_check")
def health_check():
    return f"healthy"


if __name__ == "__main__":
    app.logger.setLevel(logging.INFO)
    app.run(host="0.0.0.0", debug=True)
