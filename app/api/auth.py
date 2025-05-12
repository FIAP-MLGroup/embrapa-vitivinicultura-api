from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.jwt_manager import create_access_token
from app.models.token_response import TokenResponse

router = APIRouter()

@router.post(
    "/auth",
    response_model=TokenResponse,
    summary="Autenticar usuário",
    description="Realiza a autenticação do usuário e retorna um token JWT válido.",
    tags=["Autenticação"]
)
def login(form: OAuth2PasswordRequestForm = Depends()) -> TokenResponse:
    # TODO: substituir pela validação real (banco, LDAP etc.)
    if form.username == "admin" and form.password == "admin":
        token = create_access_token(subject=form.username)
        return TokenResponse(access_token=token, token_type="bearer")
    
    raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
