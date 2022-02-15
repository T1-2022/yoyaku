from models.Reserve import Reserve
from models.User import User
from models.Register import Register
from models.Conference import Conference
from models.database import db

def show():
    users = User.query.all()
    print(users)

    reserve = Reserve.query.all()
    print(reserve)

    register = Register.query.all()
    print(register)

    conference = Conference.query.all()
    print(conference)
