# coding: utf-8
# Elimina favorito

import webapp2
import time
from model.usuario import Usuario
from model.favorito import Favorito
from model.receta import Receta

from webapp2_extras import jinja2

from model.receta import Receta

class EliminaFavoritoHandler(webapp2.RequestHandler):
    def get(self):
        user = Usuario.get_current_user()
        if user:
            receta = Receta.recupera(self.request)
            favoritos = Favorito.query(Favorito.usuario == user.user_id, Favorito.receta_id == receta.key.id())
            if favoritos:
                for i in favoritos:
                    i.key.delete()
                time.sleep(1)
            return self.redirect("/")
        else:
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/favoritos/elimina', EliminaFavoritoHandler)
], debug=True)