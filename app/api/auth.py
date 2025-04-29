from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.jwt_manager import create_access_token

router = APIRouter()

@router.post("/auth")
def login(form: OAuth2PasswordRequestForm = Depends()):
    # TODO: substituir pela validação real (banco, LDAP etc.)
    if form.username == "admin" and form.password == "admin":
        token = create_access_token(subject=form.username)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
