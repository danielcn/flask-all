from main import db, User, Reward

db.create_all()

one = User(name='User One')
two = User(name='User Two')
db.session.add_all([one, two])
db.session.commit()

first = Reward(reward_name='Reward 1', user=one)
second = Reward(reward_name='Reward 2', user=one)
third = Reward(reward_name='Reward 3', user=one)
db.session.commit()
