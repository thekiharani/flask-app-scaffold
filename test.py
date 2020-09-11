from app import db
from app.models import User, Contact

db.drop_all()
db.create_all()

user_1 = User(name='Joe Gitonga', email='gitongajay@gmail.com', password='Password')
user_2 = User(name='Jay Kiharani', email='thekiharani@gmail.com', password='Password')
user_3 = User(name='Norah Kendi', email='nkendi@gmail.com', password='Password')
user_4 = User(name='Aria Kawira', email='akawi@gmail.com', password='Password')
db.session.add_all([user_1, user_2, user_3, user_4])
db.session.commit()

print(User.query.all())
