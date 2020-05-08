# coding: utf-8
# Modifica receta

import webapp2
import time
from model.usuario import Usuario
from model.favorito import Favorito
from webapp2_extras.users import users
from webapp2_extras import jinja2

from model.receta import Receta

class DetalleRecetaHandler(webapp2.RequestHandler):
    def get(self):
        user = Usuario.get_current_user()
        if user:
            url_user = users.create_logout_url("/")
            receta = Receta.recupera(self.request)
            listafavs = []
            favoritos = Favorito.query(Favorito.usuario == user.user_id)
            for favorito in favoritos:
                listafavs.append(favorito.receta_id)
            valores_plantilla = {
                "favoritos": listafavs,
                "user" : user,
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