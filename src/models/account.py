import uuid

from sqlalchemy import Column, String, Boolean, Index, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from config.database import Base


class DocumentType(Base):
    __tablename__ = "document_types"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)


class DocumentId(Base):
    __tablename__ = "document_ids"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    document_type_id = Column(UUID(as_uuid=True), nullable=True)

    document_type = relationship("DocumentType", back_populates="document_ids")
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)


class UserProfile(Base):
    __tablename__ = "user_profiles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    birth_date = Column(String, nullable=True, index=True)
    document_sr_id = Column(UUID(as_uuid=True), nullable=True)
    document_num = Column(String, nullable=True, index=True)
    pinfl = Column(String, nullable=True, index=True)

    is_foreigner = Column(Boolean, nullable=True)

    document_sr = relationship("DocumentId", back_populates="user_profiles")

    status = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    indexes = [
        Index("ix_users_username", "username"),
    ]
    __table_args__ = (
        Index("ix_users_username", "username"),
    )
