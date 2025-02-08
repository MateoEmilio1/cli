from fastapi import FastAPI
from networks import router as networks_router
from operators import router as operators_router
from vaults import router as vaults_router

app = FastAPI()

app.include_router(networks_router)
app.include_router(operators_router)
app.include_router(vaults_router)
