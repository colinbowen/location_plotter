import settings
import os
from flask import Flask

# GMAIL API
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


app = Flask(__name__)

# HOME - Display map
@app.route("/")
def index():
    print(CLIENT_ID)
    print(CLIENT_SECRET)
    return 'Hello World'


# API - get location
# API - post location
# API - delete location

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)