from flask_restful import Resource, reqparse
from models import UserModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

parse = reqparse.RequestParser()
parse.add_argument('username', help = 'This field cannot be black', required = True)
parse.add_argument('password', help = 'This field cannot be black', required = True)

class UserRegistration(Resource):
  def post(self):
    data = parse.parse_args()

    if UserModel.find_by_username(data['username']):
      return {'message': 'Username {} already exists'.format(data['username'])}

    new_user = UserModel(
        username = data['username'],
        password = UserModel.generate_hash(data['password'])
    )
    try:
      new_user.save_to_db()
      access_token = create_access_token(identity = data['username'])
      refresh_token = create_refresh_token(identity = data['username'])
      return {
        'message': 'User {} was created'.format(data['username']),
        'acess_token': access_token,
        'refresh_token': refresh_token
      }
    except:
      return {'message': 'Something went wrog'}, 500
    return data

class UserLogin(Resource):
  def post(self):
    data = parse.parse_args()
    current_user = UserModel.find_by_username(data['username'])
    if not current_user:
      return {'message': 'User {} doesn\'t exist'.format(data['username'])}

    if UserModel.verify_hash(data['password'], current_user.password):
      access_token = create_access_token(identity = data['username'])
      refresh_token = create_refresh_token(identity = data['username'])
      return {
        'message': 'Logged in as {}'.format(current_user.username),
        'acess_token': access_token,
        'refresh_token': refresh_token
      }
    else:
      return {'message': 'Wrong credentials'}

class UserLogoutAcess(Resource):
  def post(self):
    return {'message':'User logout'}

class UserLogoutRefresh(Resource):
  def post(self):
    return {'message':'User logout'}

class TokenRefresh(Resource):
  def post(self):
    current_user = get_jwt_identity()
    access_token = create_access_token(identity = current_user)
    return {'access_token': access_token}

class AllUsers(Resource):
  def get(self):
    return UserModel.return_all()

  def delete(self):
    return UserModel.delete_all()

class SecretResource(Resource):
  @jwt_required
  def get(self):
    return {
      'anseer': 42
    }
