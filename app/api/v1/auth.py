from fastapi import APIRouter

router = APIRouter()


@router.post('/login')
async def login():
    pass

@router.post('/register')
async def register():
    pass
