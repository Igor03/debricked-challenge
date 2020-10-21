from api.app_restx import app
from data_acquisition.data_creation import populate_database
import os

populate_database()

app.run(debug=True)