from wsgiref.simple_server import make_server
from jinja2 import FileSystemLoader, Environment, Template
from pyramid.config import Configurator
from pyramid.response import Response



HOST = 'localhost'
PORT = 8000
env=Environment(loader=FileSystemLoader('HTML'))

def IndexPage(request):
    return Response(env.get_template('/index.html').render(link="""<a href="about/aboutme.html">click to aboutme</a>""",
        head="""<h1>THIS PAGE INDEX</h1>"""))

def AboutmePage(request):
    return Responce(env.get_template('/about/aboutme.html').render(link="""<a href="/index.html">click to index</a>""",
        head="""<h1>THIS PAGE ABOUTME</h1>"""))

if __name__ == "__main__":
    config = Configurator()
    config.add_route('index', '/')
    config.add_route('index', '/index.html')
    config.add_route('aboutme','/aboutme/aboutme.html')
    config.add_view(IndexPage, route_name='index')
    config.add_view(AboutmwPage, route_name='aboutme')
    app = config.make_wsgi_app()
    server = make_server(HOST, PORT, app)
    server.serve_forever()  
