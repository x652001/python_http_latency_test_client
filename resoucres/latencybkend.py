from flask_restful import reqparse, abort, Resource
from flask import request, jsonify
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser
import json
import logging
from datetime import datetime


class LatencyBkend(Resource):
    get_args = {
        'timestamp': fields.Int(required=True, validate=lambda p: ( 10**12 <= p < 10**13))
        #'timestamp': fields.Int()
    }

    @use_kwargs(get_args, location='query')
    def get(self,timestamp):
        current_time = int(datetime.now().timestamp()*1000)
        request_time = timestamp
        if request_time > current_time:
            return None
        latency = current_time - request_time
        #
        return_data = {
            'remote_addr': request.remote_addr,
            'latency_ms': latency
        }
        return jsonify(return_data)

    @parser.error_handler
    def handle_error(error, req, schema, *, error_status_code, error_headers):
        raise ValueError(error.messages)