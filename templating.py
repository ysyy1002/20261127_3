# HTML 템플릿 설정 (여러 라우터에서 같이 사용)
from fastapi.templating import Jinja2Templates

from users import find_user

templates = Jinja2Templates(directory="templates")


def get_login_user(request):
    """세션에 저장된 아이디로 로그인한 사용자 찾기. 로그인 안 했으면 None"""
    username = request.session.get("username")
    if username is None:
        return None
    return find_user(username)


def render(request, page, data=None):
    """HTML 페이지 보여주기. 모든 페이지에 로그인 사용자(user)를 자동으로 넘겨줌"""
    data = data or {}
    data["user"] = get_login_user(request)
    return templates.TemplateResponse(request, page, data)
