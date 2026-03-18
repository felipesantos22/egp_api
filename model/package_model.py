from sqlalchemy import Column, Integer, String
from database import Base

class Package(Base):
    __tablename__ = "package"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(String(500), nullable=False)
    image_url = Column(String(500), nullable=False)
