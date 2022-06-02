from motive import db
from motive.models.user import User

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()
