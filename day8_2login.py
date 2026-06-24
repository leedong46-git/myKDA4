from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Login(BaseModel):
    userid: str
    password: str

@app.post('/login/')
async def login(login: Login):
    if login.userid != 'user':
        return {'message': '로그인 실패'}
    elif login.password != '1234':
        return {'message': '비밀번호가 다릅니다.'}
    else:
        return {'message': '로그인에 성공하셨습니다.'}
