from database.base import Base
from sqlalchemy.sql import func

from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    Boolean,
    TIMESTAMP,
    UniqueConstraint
)

from sqlalchemy.orm import relationship


class Court(Base):

    __tablename__ = "courts"

    __table_args__ = (
        UniqueConstraint(
            "name",
            "country",
            name="uq_court_name_country"
        ),
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        Text,
        nullable=False
    )

    short_name = Column(
        String,
        nullable=True
    )

    court_type = Column(
        String,
        nullable=False
    )

    jurisdiction_level = Column(
        String,
        nullable=True
    )

    state = Column(
        String,
        nullable=True
    )

    country = Column(
        String,
        nullable=False,
        default="India"
    )

    is_active = Column(
        Boolean,
        default=True
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

    judgments = relationship(
        "JudgmentMetadata",
        back_populates="court"
    )