# coding: utf-8
# Nueva receta

import webapp2
import time
from model.usuario import Usuario
from google.appengine.api import images

from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.receta import Receta

class NuevaRecetaHandler(webapp2.RequestHandler):
    def get(self):
        user = Usuario.get_current_user()

        if user:
            url_user = users.create_logout_url("/")
            valores_plantilla = {
                "user": user,
                "url_user": url_user
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("nueva_receta.html", **valores_plantilla))
        else:
            return self.redirect("/")

    def post(self):
        user = Usuario.get_current_user()

        if user:
            # url_user = users.create_logout_url("/")
            titulo = self.request.get("edTitulo", "")
            descripcion = self.request.get("edDescripcion", "")
            pasos = self.request.get("edPasos", "")
            imagen = self.request.get("edImagen", "")

            if not(titulo) or not(descripcion) or not(pasos) or not(imagen):
                return self.redirect("/")
            else:
                receta = Receta(titulo=titulo, descripcion=descripcion, pasos=pasos, usuario=user.user_id, imagen=imagen)
                receta.put()
                time.sleep(1)
                return self.redirect("/")
        else:
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/recetas/nueva', NuevaRecetaHandler)
], debug=True)