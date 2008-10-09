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

    out = []
    for (k,v) in init_values.items():
        param = get_param(k)
        if not param:
            out.append("Setting %s=%3.3f" % (k,float(v)))
            param = Param(
                name = k,
                value = float(v))
            param.put()
        elif force and param:
            out.append("Updating %s=%3.3f" % (k,float(v)))
            param.value = float(v)
            param.put()
        else:
            out.append("Current %s=%3.3f" % (k,float(v)))


    return "\n".join(out)

def get_param(name):
    return Param.all().filter("name =",name).get()

