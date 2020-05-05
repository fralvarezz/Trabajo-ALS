# Receta de cocina

from google.appengine.ext import ndb


class Receta(ndb.Model):
    titulo = ndb.StringProperty(indexed=True)
    descripcion = ndb.StringProperty(required=True)
