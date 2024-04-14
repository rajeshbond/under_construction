import os
import sys
from a2wsgi import ASGIMiddleware
from app.main import app


# Add the directory containing the `passenger_wsgi.py` file to the Python path
sys.path.insert(0, os.path.dirname(__file__))
# Wrap the FastAPI app with ASGIMiddleware
application = ASGIMiddleware(app)