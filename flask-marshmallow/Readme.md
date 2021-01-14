## Creating the database
db.create_all()

from main import User, Reward

one = User(name='User One')
two = User(name='User Two')
db.session.add_all([one, two])
db.session.commit()
first = Reward(reward_name='Reward 1', user=one)
second = Reward(reward_name='Reward 2', user=one)
third = Reward(reward_name='Reward 3', user=one)

## Checking for the data recorded
sqlite3 database.db                                                         
SQLite version 3.28.0 2019-04-15 14:49:49
Enter ".help" for usage hints.

sqlite> select * from user;
1|Úser One
2|User Two

sqlite> select * from reward;
1|Reward 1|1
2|Reward 1|1
3|Reward 2|1
4|Reward 3|1

sqlite> .exit
