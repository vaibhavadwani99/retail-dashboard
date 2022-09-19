from models.user import UserModel
import hmac


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        return user


def identity(payload):
    # payload is the content inside JWT(jason web token)
    # we need to access user id from token
    userid = payload["identity"]
    return UserModel.find_by_id(userid)
