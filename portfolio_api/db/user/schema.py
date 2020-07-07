import sqlalchemy

from portfolio_api.db import SchemaBase


# Schema of UserGet in Database
class UserSchema(SchemaBase):
    __tablename__ = "users"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    first_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    last_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    is_admin = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    def get_table(self):
        return self.__table__

    # items = relationship("Item", back_populates="owner")
