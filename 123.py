from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import json
import urllib

TODOS = [
    {'id': 1, 'title': 'learn python'},
    {'id': 2, 'title': 'get paid'},
]
 
class ReadIssuesPublicsRepos(BaseHTTPRequestHandler):
    def do_GET(self):

        link = "https://api.github.com/repos/vmg/redcarpet/issues?state=closed"
        f = urllib.urlopen(link)
        myfile = f.read()
        print myfile
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({'data': myfile}))
        return
 
    
httpd = HTTPServer(('0.0.0.0', 8003), ReadIssuesPublicsRepos)
while True:
    httpd.handle_request()