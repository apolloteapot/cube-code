# https://gist.github.com/HaiyangXu/ec88cbdce3cdbac7b8d5

# Local server for testing

import http.server
import socketserver
import os

os.chdir('web')

PORT = 8080

handler = http.server.SimpleHTTPRequestHandler

handler.extensions_map = \
{
    '.manifest': 'text/cache-manifest',
	'.html': 'text/html',
    '.png': 'image/png',
	'.jpg': 'image/jpg',
	'.svg':	'image/svg+xml',
	'.css':	'text/css',
	'.js':	'application/x-javascript',
    '.min.js':	'application/x-javascript',
	'': 'application/octet-stream',
}

httpd = socketserver.TCPServer(("", PORT), handler)

print("Serving at port", PORT)
httpd.serve_forever()