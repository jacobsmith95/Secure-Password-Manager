from pydantic import BaseModel, Field
from typing import Optional
import uuid


# Payload Schemas

class UserSchema(BaseModel):
    """
    The model for a user in the mongodb Users collection:

    email - user's email entered on account creation saved as a string
    hash  - user's unique master hash generated on account creation saved as a string
    """
    email: str = Field(...)
    hash: str = Field(...)
    token: str = Field(...)
    vault: dict = Field(...)

    class Config:
        populate_by_name = True
    

class UserUpdate(BaseModel):
    """
    The model for updating a user in the mongodb Users collection:
    
    email - necessary
    hash  - optional to update
    token - optional to update
    """
    email: str
    hash: Optional[str]
    token: Optional[str]


class HashSchema(BaseModel):
    """
    Allows functions to parse request bodies that only include a hash
    """
    hash: str = Field(...)


class VaultSchema(BaseModel):
    """
    Allows functions to parse request bodies that only include a vault
    """
    hash: str = Field(...)
    vault: dict = Field(...)


# Successful Response Schemas

def LoginResponseSchema(vault):
    """
    Defines the dictionary reponse sent back as the response body for routes:

    login_result - whether the operation resulted in success or not
    login_body   - None
    token        - the user's authentication token
    """
    login_response = {
        "login_result" : "success",
        "login_body"   : None,
        "encrypted_vault" : vault
    }

    return login_response


def AuthResponseSchema(vault):
    """
    Defines the dictionary reponse sent back as the response body for routes:

    login_result    - whether the operation resulted in success or not
    login_body      - None
    encrypted vault - the user's encrypted vault and IV
    """
    auth_response = {
        "login_result"    : "success",
        "login_body"      : None,
        "encrypted_vault" : vault
    }

    return auth_response


def CreateResponseSchema():
    """
    Defines the dictionary reponse sent back as the response body for routes:

    account_create_result - whether the operation resulted in success or not
    """
    create_response = {
        "account_create_result" : "success"
    }

    return create_response


def UpdateResponseSchema():
    """
    Defines the dictionary reponse sent back as the response body for routes:

    account_update_result - whether the operation resulted in success or not
    """
    update_response = {
        "account_update_result" : "success"
    }

    return update_response


def VaultResponseSchema():
    """
    Defines the dictionary reponse sent back as the response body for routes:

    vault_update_result - whether the operation resulted in success or not
    """
    vault_response = {
        "vault_update_result" : "success"
    }

    return vault_response


def DeleteResponseSchema():
    """
    Defines the dictionary reponse sent back as the response body for routes:

    account_delete_result - whether the operation resulted in success or not
    """
    delete_response = {
        "account_delete_result" : "success"
    }

    return delete_response


# Error Response Schema

def LoginErrorSchema(message):
    """
    Defines the dictionary error response sent back as the error body for routes:

    login_result - the error that occurred
    """
    login_error = {
        "login_result" : message
    }

    return login_error


def AuthErrorSchema(message):
    """
    Defines the dictionary error response sent back as the error body for routes:

    auth_result - the error that occurred
    """
    auth_error = {
        "auth_result" : message
    }

    return auth_error


def CreateErrorSchema(message):
    """
    Defines the dictionary error response sent back as the error body for routes:

    account_create_result - the error that occurred
    """
    create_error = {
        "account_create_result" : message
    }

    return create_error


def UpdateErrorSchema(message):
    """
    Defines the dictionary error response sent back as the error body for routes:

    account_update_result - the error that occurred
    """
    update_error = {
        "account_update_result" : message
    }

    return update_error


def VaultErrorSchema(message):
    """
    Defines the dictionary error response sent back as the error body for routes:

    vault_update_result - the error that occurred
    """
    vault_error = {
        "vault_update_result" : message
    }

    return vault_error


def DeleteErrorSchema(message):
    """
    Defines the dictionary error response sent back as the error body for routes:

    account_delete_result - the error that occurred
    """
    delete_error = {
        "account_delete_result" : message
    }

    return delete_error

