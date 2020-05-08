import webapp2
from webapp2_extras import jinja2
from google.appengine.ext import ndb

from webapp2_extras.users import users
import time

from model.receta import Receta
from model.usuario import Usuario
from model.favorito import Favorito

class ImageHandler(webapp2.RequestHandler):
    def get(self):
        receta_key = ndb.Key(urlsafe=self.request.GET['id'])
        receta = receta_key.get()
        print(receta)
        if receta.imagen:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(receta.imagen)
        else:
            self.response.out.write('No image')

app = webapp2.WSGIApplication([
    ('/imagen',ImageHandler)
], debug=True)
