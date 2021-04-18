import re
from app.config import parameter


def validate_request(func):
    def wrapper(*args):
        # Retrieve Authorization header and query parameter
        request = args[0]
        req_token = request.headers.get('Authorization')
        path = request.path
        req_parameter = re.search(f'[?]({parameter})[=]', path)
        if req_parameter:
            req_parameter = path[req_parameter.span(0)[1]:]
        # Clean from trailing and leading blanks
        req_token = req_token.strip() if req_token else req_token
        req_parameter = req_parameter.strip() if req_parameter else req_parameter
        # If any is missing throw Bad Request error
        if not req_token:
            request.response(400, "Required 'Authorization' header is missing or empty")
        elif not req_parameter:
            request.response(400, f"Required query parameter '{parameter}' is missing or empty")
        else:
            return func(req_parameter, req_token, *args)

    return wrapper
