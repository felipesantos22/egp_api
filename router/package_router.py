from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema.package_schema import PackageCreate, PackageResponse ,PackageUpdate
from service.package_service import PackageService
from dependencies import get_db

router = APIRouter(prefix="/packages", tags=["Packages"])
service = PackageService()

@router.post("/", response_model=PackageResponse)
def create(package: PackageCreate, db: Session = Depends(get_db)):
    return service.create(db, package)


@router.get("/", response_model=list[PackageResponse])
def list(db: Session = Depends(get_db)):
    return service.list(db)


@router.get("/{id}", response_model=PackageResponse)
def list_id(id: int, db: Session = Depends(get_db)):
    return service.list_by_id(db, id)


@router.put("/{id}")
def update(id: int, package: PackageUpdate, db: Session = Depends(get_db)):
    return service.update(db, id, package.name, package.description, package.image_url)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    deleted = service.delete(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Package not found")
    return {"message": "Package removed"}
