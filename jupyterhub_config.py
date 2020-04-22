# Configuration file for jupyterhub (postgres example).

c = get_config()

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
