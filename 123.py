from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import json
import urllib


class ReadIssuesPublicsRepos(BaseHTTPRequestHandler):
    #Api will invoke on get request
    def do_GET(self):

        #Read API url from the source given
        link = "https://api.github.com/repos/vmg/redcarpet/issues?state=open"
        f = urllib.urlopen(link)
        myfile = f.read()
        print myfile
        self.send_response(200)
        self.end_headers()

        #dump the data on the address of the running app
        self.wfile.write(json.dumps({'data': myfile}))
        return
 
# run class on the local server
httpd = HTTPServer(('0.0.0.0', 8003), ReadIssuesPublicsRepos)
while True:
    httpd.handle_request()