from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Configuration
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for user registration
class UserCreate(BaseModel):
    email: str
    password: str

# Pydantic model for user login
class UserLogin(BaseModel):
    email: str
    password: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/register/")
async def register_user(user: UserCreate):
    # For now, just print the user data to the console
    print(f"Received registration for user: {user.email}")
    # In a real app, you would hash the password and save the user to a database
    return {"message": f"User {user.email} registered successfully"}

@app.post("/login")
async def login_user(user: UserLogin):
    # For now, just print the user data to the console
    print(f"Received login for user: {user.email}")
    # In a real app, you would verify the password and return a token
    return {"message": f"User {user.email} logged in successfully"}
