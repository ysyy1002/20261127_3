# 비밀번호 관련 기능
# 비밀번호를 그대로 저장하면 위험하므로, 알아볼 수 없는 값(해시)으로 바꿔서 저장합니다.
import hashlib


def hash_password(password):
    # "1234" → "03ac674216f3e15c..." 처럼 바뀜 (다시 원래대로 되돌릴 수 없음)
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(password, hashed):
    # 입력한 비밀번호를 똑같이 해시해서 저장된 값과 비교
    return hash_password(password) == hashed
