from fastapi import APIRouter

router = APIRouter()

@router.post('/ig')
async def insert_ig_account():
    pass

@router.get('/ig')
async def get_ig_account():
    pass

@router.get('/ig/{id}')
async def get_ig_account_detail(id):
    pass
