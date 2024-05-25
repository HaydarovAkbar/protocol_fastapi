import uuid

from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from config.database import Base


class WeightCategory(Base):
    __tablename__ = "weight_categories"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)


class AgeCategory(Base):
    __tablename__ = "age_categories"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)


class CompetitionStatus(Base):
    __tablename__ = "competition_statuses"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)


class Competition(Base):
    __tablename__ = "competitions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    attr = Column(String, nullable=True)
    sport_type_id = Column(UUID(as_uuid=True), nullable=True)

    user_id = Column(UUID(as_uuid=True), nullable=True)

    status_id = Column(UUID(as_uuid=True), nullable=True)

    sport_type = relationship("SportType", back_populates="competitions")
    user = relationship("UserProfile", back_populates="competitions")
    status = relationship("CompetitionStatus", back_populates="competitions")

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)


class ApplicationStatus(Base):
    __tablename__ = "application_statuses"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)


class Application(Base):
    __tablename__ = "applications"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=True)
    competition_id = Column(UUID(as_uuid=True), nullable=True)
    weight_category_id = Column(UUID(as_uuid=True), nullable=True)
    age_category_id = Column(UUID(as_uuid=True), nullable=True)
    status_id = Column(UUID(as_uuid=True), nullable=True)
    is_active = Column(Boolean, default=False)

    user = relationship("UserProfile", back_populates="applications")
    competition = relationship("Competition", back_populates="applications")
    weight_category = relationship("WeightCategory", back_populates="applications")
    age_category = relationship("AgeCategory", back_populates="applications")
    status = relationship("ApplicationStatus", back_populates="applications")

    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)