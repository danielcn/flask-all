I'm assuming that you want to be able to view data present in your container everytime you connect to it from outside. To do this, you will have to persist data on the postgres image.

If you dont have persistant data, you will have to repeat everything you did the first time.
Steps 3, 5, 6, 7, and 8 answer your question directly.

Here is the detailed overview of the entire process I followed on Windows 10 powershell (commands are the same in Linux and macOS as well):

Step 1: Start powershell in non-admin mode

Step 2: Download postgres docker image:
```
docker pull postgres:latest
```

Step 3: Start docker container in detached mode and persist data on postgres image by creating a volume and binding it to a destination
(Note: by default 5432 is the default port that is used; but state it explicitly to prevent connection errors from clients like pgadmin, dbeaver, etc.)
```
docker run --name postgres-test -e POSTGRES_PASSWORD=password -p 5432:5432 -v postgres-data:/var/lib/postgresql/data -d postgres:latest
```

Step 4: Check status of running containers
```
docker ps -a
```

Step 5: Go inside container_name in interactive mode
(Note: commands like ls, pwd, etc. can be executed here if you've checked linux containers during installation)
```
  docker exec -it postgres-test psql -U postgres
```

Step 6: Create sample data. At this point, you can play with psql commands in the following manner:

```
  CREATE DATABASE test;
  \c test
  CREATE TABLE test_table(something int);
  INSERT INTO test_table VALUES (123);
  SELECT * FROM test_table;
  \q
```

Step 7: Open a database client application like pgadmin or dbeaver and enter the below in the connection fields:

Host: localhost
Database: test
User: postgres
Password: password
Step 8: Enter the query select * from test_table in the query editor and you should be able to see the output 123