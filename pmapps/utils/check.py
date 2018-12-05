
def get_login_user_id(request):
    login_user = request.session.get('login_user')
    if login_user:
        return login_user.get('id')