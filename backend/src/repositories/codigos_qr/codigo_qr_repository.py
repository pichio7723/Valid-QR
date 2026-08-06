from sqlalchemy.orm import Session

from models.codigo_qr import CodigoQR
from schemas.codigo_qr import CodigoQRCreate


def crear_codigo_qr(db: Session, codigo_data: CodigoQRCreate) -> CodigoQR:
    nuevo_codigo = CodigoQR(
        instructor_id=codigo_data.instructor_id,
        ficha_id=codigo_data.ficha_id,
        sede_id=codigo_data.sede_id,
    )

    db.add(nuevo_codigo)
    db.commit()
    db.refresh(nuevo_codigo)

    return nuevo_codigo


def obtener_por_id(db: Session, codigo_id: str) -> CodigoQR | None:
    return db.query(CodigoQR).filter(CodigoQR.id == codigo_id).first()


def listar_codigos(db: Session) -> list[CodigoQR]:
    return db.query(CodigoQR).all()


def listar_por_ficha(db: Session, ficha_id: int) -> list[CodigoQR]:
    return db.query(CodigoQR).filter(
        CodigoQR.ficha_id == ficha_id
    ).all()


def listar_por_instructor(db: Session, instructor_id: int) -> list[CodigoQR]:
    return db.query(CodigoQR).filter(
        CodigoQR.instructor_id == instructor_id
    ).all()


def eliminar_codigo_qr(db: Session, codigo: CodigoQR):
    db.delete(codigo)
    db.commit()