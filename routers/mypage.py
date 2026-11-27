# 로그인한 사람만 볼 수 있는 페이지
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from templating import get_login_user, render
from users import users

router = APIRouter()


@router.get("/mypage")
def mypage(request: Request):
    user = get_login_user(request)
    if user is None:  # 로그인 안 했으면 로그인 페이지로
        return RedirectResponse("/login", status_code=303)
    return render(request, "mypage.html")


@router.get("/admin")
def admin(request: Request):
    user = get_login_user(request)
    if user is None:
        return RedirectResponse("/login", status_code=303)
    if user["role"] != "admin":  # 관리자가 아니면 홈으로
        return RedirectResponse("/", status_code=303)
    return render(request, "admin.html", {"members": users.values()})
