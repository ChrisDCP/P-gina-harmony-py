from fireconfig import db


def get_users():
    users_ref = db.reference('users')
    users = users_ref.get()

    users_list = []

    if users:
        for user_id, user_data in users.items():
            user_data['id'] = user_id
            users_list.append(user_data)
    return users_list


def post_user(data):
    user_ref = db.reference('users')
    new_user_ref = user_ref.push(data)
    return new_user_ref

def put_user(user_id, data):
    user_ref = db.reference(f'users/{user_id}')
    user_ref.update(data)

def delete_user(user_id):
    user_ref = db.reference(f'users/{user_id}')
    user_ref.delete()