from http.client import InvalidURL
from http.server import BaseHTTPRequestHandler
from urllib.error import URLError
from urllib.request import urlopen
import json

from app.config import xml_api_uri, xml_attributes, xml_query_parameter
from app.security.authentication import authenticate_token
from app.validation.request_validation import validate_request


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    @validate_request
    @authenticate_token
    def do_GET(self, req_parameter):
        try:
            # Prepare request url and retrieve data from target server
            url = f'{xml_api_uri}&{xml_query_parameter}={req_parameter}'
            with urlopen(url) as request:
                response = request.read()
            # Parse retrieved data
            content = str(response, 'utf-8')
            if '<error>Movie not found!</error>' in content:
                self.response(404, 'Movie not found!')
            elif '<error>Incorrect IMDb ID.</error>' in content:
                self.response(400, 'Incorrect IMDb ID.')
            else:
                movie_data = dict()
                for attr in xml_attributes:
                    attr_lindex = content.find(attr)
                    vale_lindex = attr_lindex + len(attr) + len('="')
                    value_rindex = vale_lindex + content[vale_lindex:].find('"')
                    movie_data[attr] = content[vale_lindex:value_rindex]
                self.response(200, movie_data)
        except URLError:
            self.response(500, 'Error while processing request')
        except InvalidURL as e:
            self.response(400, str(e))
        except Exception:
            self.response(500, 'Unknown server error')

    def response(self, status_code=200, message=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(message).encode('utf-8'))
