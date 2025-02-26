
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/asomiclinic"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_database():
    try:
        Base.metadata.create_all(bind=engine)
        print("La base de datos fue creada con exito")
    except Exception as e:
        print(f"Hubo un error al crear la base de datos: {e}")
