from sqlmodel import Session, create_engine, SQLModel

class User(SQLModel, table=True):
    id: int = None
    name: str
    email: str

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)

def create_user(name: str, email: str):
    with Session(engine) as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()

def get_users():
    with Session(engine) as session:
        return session.query(User).all()
