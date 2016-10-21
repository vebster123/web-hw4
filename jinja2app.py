from wsgiref.simple_server import make_server
from jinja2 import FileSystemLoader, Environment, Template

HOST = 'localhost'
PORT = 8000

def app(environ, start_response):

    
    address = environ["PATH_INFO"]
    print address
    template = ''
    env = Environment(loader=FileSystemLoader('pages'))
    if(address == '/about/aboutme.html'):
        start_response('200 OK', [('Content-type', 'text/HTML')])
        template = env.get_template('/about/aboutme.html').render(link="""<a href="/index.html">click to index</a>""",
                                                                head="""<h1>THIS PAGE ABOUTME</h1>""")         

    elif(address == '/index.html' or '/'):
        start_response('200 OK', [('Content-type', 'text/HTML')])
        template = env.get_template('/index.html').render(link="""<a href="about/aboutme.html">click to aboutme</a>""",
                                                                head="""<h1>THIS PAGE INDEX</h1>""")
    else:
        start_response('404 Not Found', [("Content-Type", "text/html")])

    return [template.encode('utf-8')]

    

if __name__ == '__main__':
    _server = make_server(HOST, PORT, app)
    _server.serve_forever()

