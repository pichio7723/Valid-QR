from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db

from schemas.codigo_qr import (
    CodigoQRCreate,
    CodigoQRout,
)

from services.codigos_qr.codigo_qr_service import (
    crear_codigo_qr_service,
    obtener_codigo_qr_service,
    listar_codigos_service,
    listar_codigos_ficha_service,
    listar_codigos_instructor_service,
    eliminar_codigo_qr_service,
)

router = APIRouter(
    prefix="/codigos_qr",
    tags=["Codigos QR"]
)


@router.post("/", response_model=CodigoQRout)
def crear_codigo(
    codigo: CodigoQRCreate,
    db: Session = Depends(get_db),
):
    return crear_codigo_qr_service(db, codigo)


@router.get("/", response_model=list[CodigoQRout])
def listar_codigos(
    db: Session = Depends(get_db),
):
    return listar_codigos_service(db)


@router.get("/{codigo_id}", response_model=CodigoQRout)
def obtener_codigo(
    codigo_id: str,
    db: Session = Depends(get_db),
):
    return obtener_codigo_qr_service(db, codigo_id)


@router.get("/ficha/{ficha_id}", response_model=list[CodigoQRout])
def listar_por_ficha(
    ficha_id: int,
    db: Session = Depends(get_db),
):
    return listar_codigos_ficha_service(db, ficha_id)


@router.get("/instructor/{instructor_id}", response_model=list[CodigoQRout])
def listar_por_instructor(
    instructor_id: int,
    db: Session = Depends(get_db),
):
    return listar_codigos_instructor_service(db, instructor_id)


@router.delete("/{codigo_id}")
def eliminar_codigo(
    codigo_id: str,
    instructor_id: int,
    db: Session = Depends(get_db),
):
    eliminar_codigo_qr_service(
        db,
        codigo_id,
        instructor_id,
    )

    return {
        "mensaje": "Código QR eliminado correctamente"
    }