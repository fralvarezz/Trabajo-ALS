# Receta de cocina

from google.appengine.ext import ndb


class Favorito(ndb.Model):
    receta_id = ndb.IntegerProperty(required=True, indexed=True)
    usuario = ndb.StringProperty(required=True, indexed=True)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.receta_id == other
        elif isinstance(other, Favorito):
            return other.receta_id == self.receta_id and other.usuario == self.usuario

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()