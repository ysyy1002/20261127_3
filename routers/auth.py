# 회원가입, 로그인, 로그아웃
from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse

from security import check_password
from templating import render
from users import add_user, find_user

router = APIRouter()


# ───────── 회원가입 ─────────
@router.get("/signup")  # 회원가입 화면 보여주기
def signup_page(request: Request):
    return render(request, "signup.html")


@router.post("/signup")  # 회원가입 폼 제출 처리
def signup(
    request: Request,
    username: str = Form(),
    name: str = Form(),
    password: str = Form(),
    password2: str = Form(),
):
    # 1. 입력값 검사
    if find_user(username):
        return render(request, "signup.html", {"error": "이미 있는 아이디입니다"})
    if len(password) < 4:
        return render(request, "signup.html", {"error": "비밀번호는 4자 이상이어야 합니다"})
    if password != password2:
        return render(request, "signup.html", {"error": "비밀번호 확인이 다릅니다"})

    # 2. 회원 저장
    add_user(username, name, password)

    # 3. 로그인 페이지로 이동
    return RedirectResponse("/login", status_code=303)


# ───────── 로그인 ─────────
@router.get("/login")  # 로그인 화면 보여주기
def login_page(request: Request):
    return render(request, "login.html")


@router.post("/login")  # 로그인 폼 제출 처리
def login(request: Request, username: str = Form(), password: str = Form()):
    user = find_user(username)

    # 아이디가 없거나 비밀번호가 틀리면 다시 로그인 화면
    if user is None or not check_password(password, user["password"]):
        return render(request, "login.html", {"error": "아이디 또는 비밀번호가 틀렸습니다"})

    # 로그인 성공 → 세션에 아이디 저장 (이게 '로그인 상태')
    request.session["username"] = username
    return RedirectResponse("/mypage", status_code=303)


# ───────── 로그아웃 ─────────
@router.get("/logout")
def logout(request: Request):
    request.session.clear()  # 세션 비우기 = 로그아웃
    return RedirectResponse("/", status_code=303)
