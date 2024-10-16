from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, models, schemas
from .. import utils
# Creating Router Instances
router = APIRouter(
    prefix="/api/v1/admin",
    tags=["Authentication"],
)


@router.post('/user/create', response_model=schemas.ShowUser)
def add_adminuser(request: schemas.CreateUser,
             db: Session = Depends(database.get_db)):
    new_user = models.User(
        name = request.name,
        email=request.user_email,
        password=utils.Hash.bcrypt(request.password),
        is_admin=True
    )
    db.add(new_user)
    db.commit()
    return new_user


@router.post('/login', response_model=schemas.Token, status_code=status.HTTP_201_CREATED)
def login_user(request: OAuth2PasswordRequestForm = Depends(),
               db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        return f"No User in DB with {request.email}"
    if not utils.Hash.verify(user.password, request.password):
        return f"No User with {request.email} and {request.password}"
    access_token = utils.create_access_token(
        data={"message": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
