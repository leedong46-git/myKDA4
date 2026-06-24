from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # 실제 배포시에는 허용할 프론트엔드 도메인만 지정하는 것이 좋습니다.
    allow_credentials=False, #(인증정보 허용, 쿠키, jWT토큰 등등)
    allow_methods=["*"],     #허용할 HTTP메서드(get, post, patch, put, delete)
    allow_headers=["*"],     #허용할 http헤더(Content-Type, Authorization)
)

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
