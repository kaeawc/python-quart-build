import os
import sys
from core.logging import logger
from quart import Quart, jsonify
from quart_cors import cors

# Create a Quart app
app = Quart(__name__)

# Enable CORS using quart-cors
app = cors(app)


@app.route("/status", methods=["GET"])
def status():
    logger.debug("Status endpoint was accessed")
    return jsonify({"status": "OK", "message": "The application is running smoothly"})


def get_port():
    if len(sys.argv) > 1:
        return int(sys.argv[1])
    return int(os.getenv("PORT", 5000))


def get_debug_flag():
    if len(sys.argv) > 2:
        return int(sys.argv[2])

    return os.getenv("DEBUG", "false").lower() == "true"


# Start the app
if __name__ == "__main__":
    port = get_port()
    is_debug = get_debug_flag()
    logger.info(f"Starting the Quart app on port {port} with debug={is_debug}")
    app.run(host="0.0.0.0", port=port, debug=is_debug)
