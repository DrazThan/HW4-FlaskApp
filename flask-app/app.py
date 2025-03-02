import os
from flask import Flask
import logging

app = Flask(__name__)

# Get environment variables from ConfigMap
app_env = os.environ.get('APP_ENV', 'production')
log_level = os.environ.get('LOG_LEVEL', 'info')

# Get secret from Secret
db_password = os.environ.get('DB_PASSWORD', 'default')

# Configure logging
if log_level == 'debug':
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello():
    app.logger.debug('Debug log message')
    return f'Hello from Flask! Running in {app_env} mode. DB connection is {"successful" if db_password != "default" else "failed"}'

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)