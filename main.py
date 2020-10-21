from api.app_restx import app
from data_acquisition.data_creation import populate_database
import os

if __name__ == '__main__':
  # creating and populating database, if it not exists
  populate_database()
  # running api
  app.run(debug=True)
