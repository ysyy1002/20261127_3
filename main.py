# 앱 시작 파일
# 실행: uvicorn main:app --reload   →  http://127.0.0.1:8000
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from routers import auth, home, mypage

app = FastAPI()

# 세션: 로그인한 사용자를 기억하는 기능 (브라우저 쿠키에 저장됨)
app.add_middleware(SessionMiddleware, secret_key="my-secret-key")

# CSS 같은 정적 파일
app.mount("/static", StaticFiles(directory="static"), name="static")

# 기능별 라우터 등록
app.include_router(home.router)    # 홈
app.include_router(auth.router)    # 회원가입, 로그인, 로그아웃
app.include_router(mypage.router)  # 마이페이지, 관리자
