import os.path
import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return {'msg': 'Hello world!', "anisha":"insert text input here"}

    @cherrypy.expose
    def generate(self, url=""):
        print url
        return {"msg": "url is", "anisha": url}
        
if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8090})
    # Register the Jinja2 plugin
    from jinja2 import Environment, FileSystemLoader
    from jinja2plugin import Jinja2TemplatePlugin
    env = Environment(loader=FileSystemLoader('.'))
    Jinja2TemplatePlugin(cherrypy.engine, env=env).subscribe()

    # Register the Jinja2 tool
    from jinja2tool import Jinja2Tool
    cherrypy.tools.template = Jinja2Tool()

    # We must disable the encode tool because it
    # transforms our dictionary into a list which
    # won't be consumed by the jinja2 tool
    cherrypy.quickstart(Root(), '', {'/': {'tools.template.on': True,
                                           'tools.template.template': 'index.html',
                                           'tools.encode.on': False},
                                     "/generate":{"tools.template.on":True, 
                                                  "tools.template.template": "render.html",
                                                  "tools.encode.on":False}})
