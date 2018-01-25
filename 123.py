import github3
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import json
import os
import socketserver

PORT = 8000


class RestHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        res = {}
        l = {}
        k = None
        li = []
        gh = github3.login("yaswanthus93@gmail.com", "yaswanth12")  # enter your github username and password
        org = gh.organization("att")
        print(org)
        repos = list(org.iter_repos())  # Or type=private
        repos = list(org.iter_repos(type="public"))  # Or type=private
        for r in repos[:1]:
            print(r.name)
            k = r.name
            issuess = gh.iter_repo_issues("att", r.name)

            for iss in issuess:
                # print iss.title , iss.number
                if iss.comments == 0:
                    # print iss.comments
                    l['issues'] = {'title': iss.title, 'number': iss.number, 'Comments': iss.comments}
                else:
                    l['issues'] = {'title': iss.title, 'number': iss.number}
                li.append(l['issues'])
            res[k] = li
            print(k, li)

        self.wfile.write(json.dumps({'data': res}).encode('utf-8'))
        return


httpd = socketserver.TCPServer(('',int(os.environ.get('PORT', 17995)), RestHTTPRequestHandler)
while True:
    httpd.handle_request()
