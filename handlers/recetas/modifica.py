# coding: utf-8
# Modifica receta

import webapp2
import time
from model.usuario import Usuario

from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.receta import Receta

class ModificaRecetaHandler(webapp2.RequestHandler):
    def get(self):
        user = Usuario.get_current_user()

        if user:
            url_user = users.create_logout_url("/")
            receta = Receta.recupera(self.request)
            valores_plantilla = {
                "url_user":url_user,
                "receta": receta,
                "user": user
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("modifica_receta.html", **valores_plantilla))
        else:
            self.redirect("/")

    def post(self):
        user = Usuario.get_current_user()

        if user:
            titulo = self.request.get("edTitulo", "")
            descripcion = self.request.get("edDescripcion", "")
            pasos = self.request.get("edPasos", "")
            imagen = self.request.get("edImagen", "")

            if not(titulo) or not(descripcion) or not(pasos):
                return self.redirect("/")
            else:
                receta = Receta.recupera(self.request)
                if receta.usuario == user.user_id:
                    receta.titulo = titulo
                    receta.descripcion = descripcion
                    receta.pasos = pasos
                    if imagen:
                        receta.imagen = imagen
                    receta.put()
                    time.sleep(1)
                return self.redirect("/")
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/recetas/modifica', ModificaRecetaHandler)
], debug=True)