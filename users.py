# 회원 정보 저장소 (DB 대신 파이썬 딕셔너리 사용)
# 서버를 껐다 켜면 가입한 회원은 사라집니다.
from security import hash_password

# { "아이디": {"username": 아이디, "name": 이름, "password": 해시된 비밀번호, "role": 권한} }
users = {}


def add_user(username, name, password, role="user"):
    users[username] = {
        "username": username,
        "name": name,
        "password": hash_password(password),  # 비밀번호는 해시로 바꿔서 저장
        "role": role,
    }


def find_user(username):
    return users.get(username)  # 없으면 None


# 처음부터 관리자 계정 하나 만들어 두기
add_user("admin", "관리자", "admin1234", role="admin")
