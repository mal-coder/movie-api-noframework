from http.server import HTTPServer

from app.request_handler.handler import CustomHTTPRequestHandler


def simple_rest_service(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler):
    server_address = ('0.0.0.0', 5000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    simple_rest_service()
