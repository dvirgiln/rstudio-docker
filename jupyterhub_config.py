# Configuration file for jupyterhub (postgres example).
import time
time.sleep(30)

c = get_config()
# Set the log level by value or name.
c.JupyterHub.log_level = 'DEBUG'

# Enable debug-logging of the single-user server
c.Spawner.debug = True

# Enable debug-logging of the single-user server
c.LocalProcessSpawner.debug = True
# Add some users.
c.JupyterHub.admin_users = {'admin'}
c.Authenticator.whitelist = {'ganymede', 'io', 'rhea'}

# These environment variables are automatically supplied by the linked postgres
# container.
import os
pg_user = os.getenv('POSTGRES_USER')
pg_pass = os.getenv('POSTGRES_PASSWORD')
pg_host = 'postgres'
pg_db = os.getenv('POSTGRES_DB')
c.JupyterHub.db_url = 'postgresql://{}:{}@{}:5432/{}'.format(pg_user, pg_pass, pg_host, pg_db)
