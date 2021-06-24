# Loging into heroku container
heroku container:login

# Creates heroku app
heroku create rekcod-ukoreh-ksalf

# Push heroku app based on Dockerfile defined locally
heroku container:push:latest web --app rekcod-ukoreh-ksalf

# Release heroku app
heroku container:release web --app rekcod-ukoreh-ksalf

# Open heroku app
heroku open --app rekcod-ukoreh-ksalf

# Delete heroku app
heroku apps:delete --app rekcod-ukoreh-ksalf
