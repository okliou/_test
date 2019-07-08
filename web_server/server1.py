# -*- coding:utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys, os
import subprocess


class ServerException(Exception):
    pass


class case_no_file(object):
    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{}' not found".format(handler.path))


class case_existing_file(object):
    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        handler.handle_file(handler.full_path)


class case_always_fail(object):
    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown object '{}'".format(handler.path))


class case_directory_index_file(object):
    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')

    def test(self, handler):
        return os.path.isdir(handler.full_path) and os.path.isfile(self.index_path(handler))

    def act(self, handler):
        handler.handle_file(self.index_path(handler))


class case_cgi_file(object):
    def test(self, handler):
        return os.path.isfile(handler.full_path) and handler.full_path.endswith('.py')

    def act(self, handler):
        handler.run_cgi(handler.full_path)


class RequestHandler(BaseHTTPRequestHandler):
    ''''''

    #
    Error_Page = '''\
    <html>
	<body>
	<h1>Error accessing {path}</h1>
	<p>{msg}</p>
	</body>
	</html>
    '''

    Cases = [case_no_file(),
             case_cgi_file(),
             case_existing_file(),
             case_directory_index_file(),
             case_always_fail()]

    def run_cgi(self, full_path):

        data = subprocess.check_output(["python3", full_path], shell=False)
        self.send_content(data)

    def do_GET(self):
        try:
            self.full_path = os.getcwd() + self.path
            for case in self.Cases:
                if case.test(self):
                    case.act(self)
                    break
        except Exception as msg:
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content.encode("utf-8"), 404)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{}' cannot be read: {}".format(self.path, msg)
            self.handle_error(msg)

    def create_page(self):
        value = {
            'date_time': self.date_time_string(),
            'client_host': self.client_address[0],
            'client_port': self.client_address[1],
            'command': self.command,
            'path': self.path
        }
        page = self.Page.format(**value)
        return page

    # ????GET??
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()