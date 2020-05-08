from google.appengine.ext import ndb
from webapp2_extras.users import users


class Usuario(ndb.Model):
    user_id = ndb.StringProperty(required=True, indexed=True)
    nombre = ndb.StringProperty(required=True, indexed=True)


    @staticmethod
    def get_current_user():
        toret = None
        user = users.get_current_user()

        if(user):
            try:
                usuario_localizado = Usuario.query(Usuario.user_id == user.user_id()).fetch(1)
                if usuario_localizado:
                    toret = usuario_localizado[0]
                else:
                    toret = Usuario(user_id = user.user_id(), nombre = user.nickname())
                    toret.put()
            except Exception as e:
                print(e)
        return toret
