# Receta de cocina

from google.appengine.ext import ndb


class Receta(ndb.Model):
    titulo = ndb.StringProperty(indexed=True)
    descripcion = ndb.StringProperty(required=True)
    pasos = ndb.StringProperty(required=True)
    usuario = ndb.StringProperty(required=True, indexed=True)
    imagen = ndb.BlobProperty(required=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

    @staticmethod
    def recupera_imagen(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()