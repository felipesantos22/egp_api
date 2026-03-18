from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositorie.package_repositorie import PackageRepository
from model.package_model import Package
from schema.package_schema import PackageCreate


class PackageService:

    def __init__(self):
        self.repository = PackageRepository()

    def create(self, db: Session, package_create: PackageCreate) -> Package:
        package = Package(**package_create.model_dump())
        return self.repository.create(db, package)

    def list(self, db: Session):
        return self.repository.find_all(db)

    def list_by_id(self, db: Session, id: int):
        package = self.repository.find_by_id(db, id)
        if not package:
            raise HTTPException(status_code=404, detail="Package not found")
        return package

    def update(self, db: Session, id: int, name: str, description: str, image_url: str):
        package = self.repository.find_by_id(db, id)
        if not package:
            raise HTTPException(status_code=404, detail="Package not found")
        return self.repository.update(db, package, name, description, image_url)

    def delete(self, db: Session, id: int):
        item = self.repository.find_by_id(db, id)
        if not item:
            raise HTTPException(status_code=404, detail="Package not found")
        return self.repository.delete(db, item)