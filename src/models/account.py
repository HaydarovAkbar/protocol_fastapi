import uuid

from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from config.database import Base


class DocumentType(Base):
    __tablename__ = "document_types"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)


class DocumentId(Base):
    __tablename__ = "document_ids"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    document_type_id = Column(UUID(as_uuid=True), nullable=True)

    document_type = relationship("DocumentType", back_populates="document_ids")


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
