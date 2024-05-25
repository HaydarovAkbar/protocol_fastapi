import uuid

from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from config.database import Base


class Country(Base):
    __tablename__ = "countries"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    attr = Column(String, nullable=True)

    code = Column(String, nullable=True)
    flag = Column(String, nullable=True)

    status = Column(Boolean, default=True)


class Region(Base):
    __tablename__ = "regions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    country = relationship("Country", back_populates="regions")

    status = Column(Boolean, default=True)


class District(Base):
    __tablename__ = "districts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    region = relationship("Region", back_populates="districts")

    status = Column(Boolean, default=True)
