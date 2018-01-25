# import github3
# from BaseHTTPServer import HTTPServer
# from BaseHTTPServer import BaseHTTPRequestHandler
# import json
#
# class RestHTTPRequestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#
#         res = {}
#         l = {}
#         k = None
#         li = []
#         gh = github3.login("sanket386", "consultadd505")
#         org = gh.organization("att")
#         repos = list(org.iter_repos(type="public"))  # Or type="private"
#         for r in repos:
#             # print r.name
#             k = r.name
#             issuess = gh.iter_repo_issues("att", r.name)
#
#             for iss in issuess:
#                 # print iss.title , iss.number
#                 if iss.comments > 0:
#                     # print iss.comments
#                     l['issues'] = {'title': iss.title, 'number': iss.number, 'Comments': iss.comments}
#                 else:
#                     l['issues'] = {'title': iss.title, 'number': iss.number}
#                 li.append(l['issues'])
#             res[k] = li
#             # print k
#         r = json.dumps(res)
#
#         self.wfile.write(json.dumps({'data': r}))
#         return
#
# httpd = HTTPServer(('0.0.0.0', 9001), RestHTTPRequestHandler)
# while True:
#     httpd.handle_request()
import github3
# from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import json
import os
import SocketServer

PORT = 80


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
        # print org
        repos = list(org.iter_repos(type="public"))  # Or type="private"
        for r in repos:
            # print r.name
            k = r.name
            issuess = gh.iter_repo_issues("att", r.name)

            for iss in issuess:
                # print iss.title , iss.number
                if iss.state == "open":
                    if iss.comments > 0:
                        # print iss.comments
                        l['issues'] = {'title': iss.title, 'number': iss.number, 'Comments': iss.comments}
                    else:
                        l['issues'] = {'title': iss.title, 'number': iss.number}
                    li.append(l['issues'])
                res[k] = li
                # print k
        r = json.dumps(res)

        self.wfile.write(json.dumps({'data': r}))
        return


httpd = SocketServer.TCPServer(('', PORT), RequestHandlerClass=RestHTTPRequestHandler)
httpd.serve_forever()
while True:
    httpd.handle_request()
