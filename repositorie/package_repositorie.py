from sqlalchemy.orm import Session
from model.package_model import Package


class PackageRepository:

    def create(self, db: Session, package: Package):
        db.add(package)
        db.commit()
        db.refresh(package)
        return package

    def find_all(self, db: Session):
        return db.query(Package).all()

    def find_by_id(self, db: Session, id: int):
        return db.query(Package).filter(Package.id == id).first()

    def update(self, db: Session, package: Package, name: str, description: str, image_url: str):
        package.name = name
        package.description = description
        package.image_url = image_url
        db.commit()
        db.refresh(package)
        return package

    def delete(self, db: Session, package: Package):
        db.delete(package)
        db.commit()
        return package
