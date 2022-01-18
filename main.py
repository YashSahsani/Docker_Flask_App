from init_db import connect,add_data
from FlaskApp import Run_flask

if __name__ == '__main__':
    connect()
    add_data()
    Run_flask()