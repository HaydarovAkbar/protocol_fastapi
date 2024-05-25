from config.database import Base, engine
from models.utils import Country, Region, District
from models.sport import SportType
from models.account import User, UserProfile, DocumentType, DocumentId
from models.app import WeightCategory, AgeCategory, CompetitionStatus, Competition, ApplicationStatus, Application


def create_tables():
    """
    Creates all database tables defined in the application.
    """
    Region.metadata.create_all(bind=engine)
    Country.metadata.create_all(bind=engine)
    District.metadata.create_all(bind=engine)
    SportType.metadata.create_all(bind=engine)
    User.metadata.create_all(bind=engine)
    UserProfile.metadata.create_all(bind=engine)
    DocumentType.metadata.create_all(bind=engine)
    DocumentId.metadata.create_all(bind=engine)
    WeightCategory.metadata.create_all(bind=engine)
    AgeCategory.metadata.create_all(bind=engine)
    CompetitionStatus.metadata.create_all(bind=engine)
    Competition.metadata.create_all(bind=engine)
    ApplicationStatus.metadata.create_all(bind=engine)
    Application.metadata.create_all(bind=engine)
