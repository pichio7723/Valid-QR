from fastapi import FastAPI


from routes.asistencias.asistencia_routes import router as asistencia_router


app = FastAPI()







app.include_router(asistencia_router)