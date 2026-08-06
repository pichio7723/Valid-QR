from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.codigo_qr import CodigoQRCreate
from repositories.codigos_qr.codigo_qr_repository import (
    crear_codigo_qr,
    obtener_por_id,
    listar_codigos,
    listar_por_ficha,
    listar_por_instructor,
    eliminar_codigo_qr,
)


def crear_codigo_qr_service(db: Session, codigo_data: CodigoQRCreate):
    return crear_codigo_qr(db, codigo_data)


def obtener_codigo_qr_service(db: Session, codigo_id: str):
    codigo = obtener_por_id(db, codigo_id)

    if not codigo:
        raise HTTPException(
            status_code=404,
            detail="Código QR no encontrado"
        )

    return codigo


def listar_codigos_service(db: Session):
    return listar_codigos(db)


def listar_codigos_ficha_service(db: Session, ficha_id: int):
    return listar_por_ficha(db, ficha_id)


def listar_codigos_instructor_service(db: Session, instructor_id: int):
    return listar_por_instructor(db, instructor_id)


def eliminar_codigo_qr_service(
    db: Session,
    codigo_id: str,
    instructor_id: int,
):
    codigo = obtener_codigo_qr_service(db, codigo_id)

    if codigo.instructor_id != instructor_id:
        raise HTTPException(
            status_code=403,
            detail="No tienes permisos para eliminar este código QR"
        )

    eliminar_codigo_qr(db, codigo)