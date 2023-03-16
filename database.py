from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://as8hlxzcsku5z7ruw5ve:pscale_pw_QF2668d6EfMwpPDgyhioazwuH7DThoxCfcll3qb2JJh@ap-southeast.connect.psdb.cloud/mosesportfolio?charset=utf8mb4"

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
