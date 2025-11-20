from database import SessionLocal
from models import Question
from datetime import datetime

db = SessionLocal()
for i in range(300):
    q = Question(subject='테스트 더미데이터 입니다 : [%03d]' % i, content='내용 없음', created_date=datetime.now())
    db.add(q)
db.commit()