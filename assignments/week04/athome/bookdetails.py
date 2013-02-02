#!/usr/bin/python


from bookdb import BookDB


books = BookDB()

body = """<html>
<head>
<title>Book information - WSGI experiments</title>
</head>
<body>
<h3> Book Details</h3>
</hr>
</hr>
</hr>
%s
</body>
</html>"""

def formatData(bookDetails):
    data = ''
    for keys in bookDetails:
        data+="<p>"+keys+" :  "+bookDetails[keys]+ "</p>"
    return data

def application(environ, start_response):
    path = environ.get('PATH_INFO','Unset')
    if path != 'Unset':
        book =  path[1:]
        response_body = body % (
         formatData(books.title_info(book))
         )
    else :
        response_body ="Book Not Found"
    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8083, application)
    srv.serve_forever()

