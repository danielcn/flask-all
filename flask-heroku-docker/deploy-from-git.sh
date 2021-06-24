# Another way to do that by using of --remote to get from git repo reference
# that is the only difference in here

# Loging into heroku container
heroku container:login

# Creates heroku app
heroku create rekcod-ukoreh-ksalf

# Adds remote 'docker' repo reference
git remote add docker https://git.heroku.com/rekcod-ukoreh-ksalf.git

# Push heroku app based on Dockerfile defined locally
heroku container:push:latest web --remote docker

# Release heroku app
heroku container:release web --remote docker

# Open heroku app
heroku open --remote docker

# Delete heroku app
heroku apps:delete web --remote docker
