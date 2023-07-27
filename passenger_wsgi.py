import os
import sys
from imvb_web.wsgi import application

sys.path.insert(0, os.path.dirname(__file__))
environ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imvb_web.settings")