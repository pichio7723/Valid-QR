from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioLogin, Token


from core.database import get_db
from schemas.usuario import UsuarioCrear, UsuarioOut, UsuarioUpdate
from services.usuarios.usuario_service import (
    registrar_usuario,
    login_usuario,
    actualizar_usuario_service,
    eliminar_usuario_service,
)

router = APIRouter(prefix="/usuarios", tags=["usuarios"])
