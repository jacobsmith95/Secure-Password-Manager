from fastapi import FastAPI, HTTPException, status, Response, Body
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from models import UserSchema, UserUpdate, HashSchema, LoginResponseSchema, CreateResponseSchema, UpdateResponseSchema, VaultResponseSchema, DeleteResponseSchema, LoginErrorSchema, CreateErrorSchema, UpdateErrorSchema, VaultErrorSchema, DeleteErrorSchema
from database import add_user, find_user, auth_user, find_vault, update_user, update_vault, delete_user

app = FastAPI()

origins = [
    "https://frontend-ngnhr6tt3a-ul.a.run.app"
]


@app.post(path="/login/", status_code=status.HTTP_200_OK)
async def login(hash: HashSchema = Body(...)):
    """
    
    """
    master_hash = jsonable_encoder(hash)
    result = await auth_user(master_hash["hash"])
    if result == "success":
        vault = await find_vault(master_hash["hash"])
        return LoginResponseSchema(vault)
    else:
        return LoginErrorSchema("Login Failed")


#@app.post(path="/account-create/", status_code=status.HTTP_201_CREATED)
#async def create_user(user: UserSchema = Body(...)):
#    """
#    
#    """
    




app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

    