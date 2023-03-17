from sqlalchemy import create_engine, text
import os


db_connection_string = os.getenv("DB_CONNECTION_STR")

engine = create_engine(
    db_connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}
)


def load_projects_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from projects"))

        projects = []
        for row in result:
            projects.append(dict(zip(result.keys(), row)))
        return  projects
