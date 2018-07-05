from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

from nbp.models.meta import Base
from sqlalchemy import (
    Column,
    Float,
    Unicode,
    )

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))

Base = Base

class ExchangeRates(Base):
    __tablename__ = 'rates'
    currency = Column(Unicode(255), unique=False, nullable=False)
    code = Column(Unicode(255),  primary_key=True, unique=True, nullable=False)
    mid = Column(Float, unique=False, nullable=False)
