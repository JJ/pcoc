from google.appengine.ext import db

class Param(db.Model):
    name = db.StringProperty()
    value = db.FloatProperty()

class Experiment(db.Model):
    #experiment_id serial primary key,
    descripcion = db.StringProperty(multiline=True)
    generaciones = db.IntegerProperty()
    poblacion = db.IntegerProperty()
    total_generados = db.IntegerProperty()
    maximo_generados = db.IntegerProperty()
    crossover_priority = db.IntegerProperty()
    mutation_priority = db.IntegerProperty()
    mutation_rate = db.FloatProperty()
    chromosome_size = db.IntegerProperty()
    target_fitness = db.FloatProperty()

class Guy(db.Model):
    chromosome = db.StringProperty() # db.TextProperty() if > 500
    fitness = db.FloatProperty()

def init_ga_params(force=False):
    init_values = {
        'generaciones': 10,
        'poblacion': 100,
        'total_generados': 0,
        'maximo_generados': 20000,
        'crossover_priority':  4,
        'mutation_priority':  1,
        'mutation_rate':  0.01,
        'chromosome_size':  128,
        'experiment_id':  0,
        'target_fitness':  0,
    }

    for (k,v) in init_values:
        param = Params.filter('name =', k).get()
        if not param:
            param = Param()
            param.name = k
            param.value = v
            param.put()
        elif force and param:
            param.value = v
            param.put()

def get_param(name):
    return Param.filter("name=",name).one()

