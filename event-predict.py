from flask import Flask
from home.views import home_view

def create_app():
	app = Flask(__name__)  # Create application object
	app.register_blueprint(home_view)  # Register url's so application knows what to do
	return app

if __name__ == '__main__':
	app = create_app()  # Create application with our config file
	app.run()  # Run our application