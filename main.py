import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

from database import Base, engine

from router.package_router import router as controller_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Project Traveller")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(controller_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
