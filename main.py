import logging, os
from flask import Flask
from flask_restful import Api
#
from resoucres.latencybkend import LatencyBkend

class Web():
    def __init__(self) -> None:
        # Init flask app
        self.app = Flask(__name__)
        self.api = Api(self.app)
        #
        self.api.add_resource(
            LatencyBkend,
            '/api/httptest'
        )

    def run(self):
        self.app.run(
            host='0.0.0.0',
            port='8080',
            debug=False,
            threaded=True,
        )


if __name__ == "__main__":
    app = Web()
    app.run()