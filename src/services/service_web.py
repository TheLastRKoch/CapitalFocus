from flask import Response
import json


class WebService:

    def response(self, status_code, body):
        return Response(json.dumps(body), status=status_code)
