# coding: utf-8
# Añade a favorito

import webapp2
import time
from model.usuario import Usuario
from model.favorito import Favorito

from webapp2_extras import jinja2

from model.receta import Receta

class AddFavoritoHandler(webapp2.RequestHandler):
    def get(self):
        user = Usuario.get_current_user()
        if user:
            receta = Receta.recupera(self.request)
            if receta:
                favorito = Favorito(usuario=user.user_id, receta_id=receta.key.id())
                favorito.put()
                time.sleep(1)
            return self.redirect("/")
        else:
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/favoritos/add_favorito', AddFavoritoHandler)
], debug=True)