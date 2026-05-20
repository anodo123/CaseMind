from database.base import Base
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
    Text,
    Date,
    Boolean,
    JSON,
    TIMESTAMP,
    ForeignKey
)

from sqlalchemy.orm import relationship

class JudgmentMetadata(Base):

    __tablename__ = "judgment_metadata"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    tid = Column(
        BigInteger,
        unique=True,
        nullable=False
    )

    title = Column(
        Text,
        nullable=False
    )

    doctype = Column(
        Integer
    )
    
    court_id = Column(
        Integer,
        ForeignKey("courts.id"),
        nullable=True,
        index=True
    )

    docsource = Column(
        String
    )

    catids = Column(
        String,
        nullable=True
    )

    authorid = Column(
        String,
        nullable=True
    )

    bench = Column(
        String,
        nullable=True
    )

    publish_date = Column(
        Date
    )

    headline = Column(
        Text,
        nullable=True
    )

    numcites = Column(
        Integer,
        default=0
    )

    numcitedby = Column(
        Integer,
        default=0
    )

    docsize = Column(
        Integer
    )

    fragment = Column(
        Boolean,
        default=False
    )

    raw_json = Column(
        JSON,
        nullable=True
    )

    fetched_at = Column(
        TIMESTAMP(timezone=True),
        nullable=True
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    
    court = relationship(
        "Court",
        back_populates="judgments"
    )