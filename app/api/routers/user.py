from fastapi import APIRouter, Depends, HTTPException

from app.schemas.user import UserOutWithLists, UserCreate, UserUpdate, UserOut, UserChangePassword
from app.services.user import UserServices

router = APIRouter()


@router.post("/users", tags=['Users'], response_model=UserOut)
async def create_user(input_schema: UserCreate, service: UserServices = Depends(UserServices)):
    user = await service.create_user(input_schema)

    return user


@router.get("/users/{id}", tags=['Users'], response_model=UserOutWithLists)
async def retrieve_user(user_id: int, service: UserServices = Depends(UserServices)):
    user = await service.retrieve_user(user_id)

    return user


@router.get("/users/", tags=['Users'], response_model=list[UserOut])
async def retrieve_all_users(service: UserServices = Depends(UserServices)):
    users = await service.retrieve_all_users()

    return users


@router.patch("/users/{id}", tags=['Users'], status_code=204)
async def update_user(user_id: int, input_schema: UserUpdate, service: UserServices = Depends(UserServices)):
    result = await service.update_user(user_id, input_schema)

    if result.rowcount < 1:
        raise HTTPException(status_code=404)


@router.delete("/users/{id}", tags=['Users'], status_code=204)
async def delete_user(user_id: int, service: UserServices = Depends(UserServices)):
    result = await service.delete_user(user_id)

    if result.rowcount < 1:
        raise HTTPException(status_code=404)
    

@router.post("/users/{id}/change_password", tags=['Users'], status_code=204)
async def change_password(user_id: int, input_schema: UserChangePassword, service: UserServices = Depends(UserServices)):
    result = await service.change_password(user_id, input_schema)

    if result.rowcount < 1:
        raise HTTPException(status_code=404)
