# -*- encoding: utf-8 -*-

from config import app
from blueprints.authentication import routes as auth
from blueprints.home import routes as home


# blueprints (api)
app.register_blueprint(auth.blueprint)
app.register_blueprint(home.blueprint)

if __name__ == "__main__":
    app.run()
