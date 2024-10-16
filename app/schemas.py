from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class CreateUser(BaseModel):
    token: str
    name: str
    user_email: str
    password: str

    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    email: str
    is_admin: bool

    class Config():
        orm_mode = True

class CreateOrg(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        orm_mode = True

class GetOrg(BaseModel):
    organization_name: str
    class Config():
        orm_mode = True

class ShowOrg(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True
        from_attributes = True 
        
class VerifyUser(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode = True
