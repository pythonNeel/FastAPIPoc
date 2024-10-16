from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, models
from .. import utils

router = APIRouter(
    prefix="/api/v1/org",
    tags=["Organization"]
)


@router.post('/create', response_model=schemas.ShowOrg)
def create_organization(request: schemas.CreateOrg,
             db: Session = Depends(database.get_db)):
    new_org = models.Organization(
        name=request.name, email=request.email, password=utils.Hash.bcrypt(request.password))
    new_user = models.User(
        name=request.name, 
        email=request.email,
        password=utils.Hash.bcrypt(request.password),
        is_admin=True
    )
    db.add(new_org)
    db.add(new_user)
    db.commit()
    return new_org


@router.post('/get')
def get_organization(request: schemas.GetOrg,
                db: Session = Depends(database.get_db)):
    org = db.query(models.Organization).filter(models.Organization.name == request.organization_name).first()
    if org:
        return schemas.ShowOrg.from_orm(org)
    else:
        return f"No Organization with name '{request.organization_name}' found in the database."
