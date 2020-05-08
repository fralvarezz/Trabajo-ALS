# coding: utf-8
# Modifica receta

import webapp2
import time
from model.usuario import Usuario
from webapp2_extras.users import users
from webapp2_extras import jinja2

from model.receta import Receta

class DetalleRecetaHandler(webapp2.RequestHandler):
    def get(self):
        user = Usuario.get_current_user()
        if user:
            url_user = users.create_logout_url("/")
            receta = Receta.recupera(self.request)
            valores_plantilla = {
                "user":user,
                "url_user": url_user,
                "receta": receta
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("detalle_receta.html", **valores_plantilla))
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/recetas/detalle', DetalleRecetaHandler)
], debug=True)