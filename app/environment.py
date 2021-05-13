import os

# Server settings
address="0.0.0.0"
port="8080"
server_name='jup-download'
server_zone='us-central1-b'

debug=True
static_path = os.path.join(os.path.dirname(__file__), "static")
template_path = os.path.join(os.path.dirname(__file__), "templates")

# logging settings
log_dir = os.path.join(os.getcwd(), 'logs')
log_file_size = 1024 * 20 * 1000
log_count = 10

# levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
access_level = 'INFO'
application_level = 'INFO'
general_level = 'INFO'

# directory to store user data
data_dir = '/data'

# directory for utility scripts (bash)
utils = os.path.join(os.path.dirname(__file__), "utils")

# kubernetes cluster namespace
cluster_namespace = 'summa-jhub'

# postgres
db_user = 'jhdownloader'
db_pwd = 'mma19casl!_as)'
db_dbname = 'logging'
db_ip = '127.0.0.1'
