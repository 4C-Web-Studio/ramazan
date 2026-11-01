from contextlib import contextmanager
from threading import Thread
from werkzeug.serving import make_server
@contextmanager
def serve(app):
    httpd = make_server('127.0.0.1', 0, app, threaded=True)
    worker = Thread(target=httpd.serve_forever, daemon=True)
    worker.start()
    try:
        yield f'http://127.0.0.1:{httpd.server_port}'
    finally:
        httpd.shutdown()
        worker.join(timeout=5)
        httpd.server_close()
