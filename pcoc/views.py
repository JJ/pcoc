from google.appengine.ext import webapp
import simplejson
from models import Guy, Param, get_param

class get_guy(webapp.RequestHandler):
    def get(self):
        chromosome = self.request.get("chromosome")
        fitness = self.request.get("fitness")
        if not chromosome or not fitness:
            self.error(500)
        fitness = float(fitness)

        este_guy = Guy.all().filter("chromosome = ", chromosome).get()
        if not este_guy:
            este_guy = Guy()
            este_guy.chromosome = chromosome
            este_guy.fitness = fitness
            este_guy.put()

        total_generados = get_param("total_generados")
        generaciones = get_param("generaciones")
        poblacion = get_param("poblacion")
        maximo_generados = get_param("maximo_generados")

        nuevo_total = total_generados.value + generaciones.value + poblacion.value
        total_generados.value = nuevo_total
        total_generados.put()

        masca_obj = Guy.all().order('-fitness').get()
        masca = {}
        masca['chromosome'] = masca_obj.chromosome
        masca['fitness'] = masca_obj.fitness        
        if nuevo_total < maximo_generados.value:
            masca['generaciones'] = generaciones.value
        else:
            masca['generaciones'] = 0

        self.response.headers['content-type'] = 'text/javascript'
        self.response.out.write(simplejson.dumps(masca))

if False:
    class start_ga(webapp.RequestHandler):
        def get(self):
            self.response.headers['content-type'] = 'text/plain'
            self.response.out.write('hello, webapp world!')

    class end_ga(webapp.RequestHandler):
        def get(self):
            self.response.headers['content-type'] = 'text/plain'
            self.response.out.write('hello, webapp world!')

    class manage_ga(webapp.RequestHandler):
        def get(self):
            self.response.headers['content-type'] = 'text/plain'
            self.response.out.write('hello, webapp world!')

    class reset_ga(webapp.RequestHandler):
        def get(self):
            self.response.headers['content-type'] = 'text/plain'
            self.response.out.write('hello, webapp world!')

    class get_info(webapp.RequestHandler):
        def get(self):
            self.response.headers['content-type'] = 'text/plain'
            self.response.out.write('hello, webapp world!')

    class get_guy(webapp.RequestHandler):
        def get(self):
            self.response.headers['content-type'] = 'text/plain'
            self.response.out.write('hello, webapp world!')

    class generate_ga_js(webapp.RequestHandler):
        def get(self):
            self.response.headers['content-type'] = 'text/plain'
            self.response.out.write('hello, webapp world!')

