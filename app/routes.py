from app import app
from web.routes import web
from api.routes import api

app.register_blueprint(api)
app.register_blueprint(web)