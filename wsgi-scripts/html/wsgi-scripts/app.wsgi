import sys

sys.path.insert(0, '/var/www/html')
sys.path.insert(1, '/var/www/html/wsgi-scripts')

sys.stdout = sys.stderr

from routes import app as application
