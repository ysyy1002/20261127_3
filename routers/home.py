# 홈 페이지
from fastapi import APIRouter, Request

from templating import render

router = APIRouter()


@router.get("/")
def home(request: Request):
    return render(request, "home.html")
