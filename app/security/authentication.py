from app.config import api_key


def authenticate_token(func, *args):
    def wrapper(req_parameter, req_token, *args):
        request = args[0]
        split_token = req_token.split()
        if len(split_token) != 2 or split_token[0].lower() != 'bearer':
            request.response(400, 'Authorization header missing or token in incorrect format')
        elif split_token[1] != api_key:
            request.response(401, 'Authorization token is incorrect')
        else:
            return func(*args, req_parameter)

    return wrapper
