from fastapi import FastAPI
from read_commands.networks import router as networks_router
from read_commands.operators import router as operators_router
from read_commands.vaults import router as vaults_router
from read_commands.stakers import router as stakers_router

app = FastAPI()

app.include_router(networks_router)
app.include_router(operators_router)
app.include_router(vaults_router)
app.include_router(stakers_router)
