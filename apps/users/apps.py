from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # 调用设置密码为密文的方法
    def ready(self):
        import users.signals