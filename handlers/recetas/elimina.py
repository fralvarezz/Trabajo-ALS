# coding: utf-8
# Elimina receta

import webapp2
import time
from model.usuario import Usuario

from webapp2_extras import jinja2

from model.receta import Receta

class EliminaRecetaHandler(webapp2.RequestHandler):
    def get(self):
        user = Usuario.get_current_user()
        if user:
            receta = Receta.recupera(self.request)
            if receta.usuario == user.user_id:
                receta.key.delete()
                time.sleep(1)
            return self.redirect("/")
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/recetas/elimina', EliminaRecetaHandler)
], debug=True)