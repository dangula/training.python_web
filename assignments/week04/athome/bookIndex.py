#!/usr/bin/python

from bookdb import BookDB


books = BookDB()

body = """<html>
<head>
<title>Books- WSGI experiments</title>
</head>
<body>
<h3> Book Databaes</h3>
</hr>
</hr>
</hr>
%s
</body>
</html>"""

def formatData(bookinfo):
    data = """<table border="1">
<tr>
<th>BookId</th>
<th>Book Title</th>
</tr>
"""
    for item in bookinfo:
        id =''
        ttile = ''
        data+="<tr>"
        for keys in item:
            key = keys
            if key == 'id':
                id = key
                data+="<th>"+item[id]+"</th>\n"
            if key == 'title':
                title = key
                data+="""<th><a href="http://localhost:8083/"""+item[id]+"""">"""+item[title]+"</a></th>\n"
        data+="</tr>"
    data+="</table>"
    return data

def application(environ, start_response):
    response_body = body % (
         formatData(books.titles())
         )
    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8082, application)
    srv.serve_forever()