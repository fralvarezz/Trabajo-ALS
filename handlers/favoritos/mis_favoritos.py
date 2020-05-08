import webapp2
from webapp2_extras import jinja2

from webapp2_extras.users import users
import time

from model.receta import Receta
from model.usuario import Usuario
from model.favorito import Favorito


class MisFavoritosHandler(webapp2.RequestHandler):
    def get(self):
        user = Usuario.get_current_user()
        if user:
            url_user = users.create_logout_url("/")
            recetas = []
            listafavs = []
            favoritos = Favorito.query(Favorito.usuario == user.user_id)
            for favorito in favoritos:
                listafavs.append(favorito.receta_id)

            for favorito in favoritos:
                recetas.append(Receta.get_by_id(favorito.receta_id))

            valores_plantilla = {
                "favoritos": listafavs,
                "user": user,
                "url_user": url_user,
                "recetas": recetas
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("mis_favoritos.html", **valores_plantilla))
        else:
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/favoritos/mis_favoritos', MisFavoritosHandler)
], debug=True)
