from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

database_url="mysql+pymysql://root:yourpassword@localhost/fastapi"
engine=create_engine(database_url)
sessionlocal=sessionmaker(bind=engine)
base=declarative_base()
