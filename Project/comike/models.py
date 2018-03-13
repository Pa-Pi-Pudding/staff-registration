from django.db import models
# from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


GENDER_CHOICES = [
    (1, '男'),
    (2, '女')
]
USE_CHOICES = [
    (1, '使用する'),
    (0, '使用しない')
]
ASSIGNMENT_HOLE_CHOICES = [
    #  これってホールテーブル作る必要があったのでは...
    (0, '東1ホール'),
    (1, '東2ホール'),
    (2, '東3ホール'),
    (3, '東4ホール'),
    (4, '東5ホール'),
    (5, '東6ホール'),
    (6, '東7ホール'),
    (7, '東8ホール'),
]
CARRIER0_SHIFT_CHOICES = [
    (0, '選択してください'),
    (1, '晴'),
    (2, '雨')
    # 0のときは許容しない、もしくはNULLだと許容なしとか作る
]
ORGANIZATION_CHOICES = [
    (0, '統括部'),
    (1, '設営部'),
    (2, '防災防犯'),
    (3, '販売担当'),
    # etc...
]


class StaffData(models.Model):
    id = models.AutoField(primary_key=True)  # 主キーが自動生成されるはず
    staff_name = models.CharField(max_length=64)
    staff_name_kana = models.CharField(max_length=200)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    birth_day = models.DateField(null=False)
    mail_address = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=10)
    post_code = models.CharField(max_length=7)
    address = models.CharField(max_length=255)
    e_name = models.CharField(max_length=64)
    e_relationship = models.CharField(max_length=10)
    e_phone_number = models.CharField(max_length=10)
    join_day_0 = models.BooleanField(default=False)
    join_day_1 = models.BooleanField(default=False)
    join_day_2 = models.BooleanField(default=False)
    join_day_3 = models.BooleanField(default=False)
    assignment_1 = models.IntegerField(choices=ASSIGNMENT_HOLE_CHOICES)
    assignment_2 = models.IntegerField(choices=ASSIGNMENT_HOLE_CHOICES, null=True)
    partner = models.CharField(max_length=64, null=True)  # charfield は固定長で、メモリを確保
    parking = models.IntegerField(choices=USE_CHOICES)
    hotel = models.IntegerField(choices=USE_CHOICES)
    password = models.CharField(max_length=20)
    memo = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class Information(models.Model):
    id = models.AutoField(primary_key=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    organization = models.IntegerField(choices=ORGANIZATION_CHOICES)  # そんなに可変しないので、定数として作るか、DBで別テーブルとして作るか
    title = models.CharField(max_length=255)
    content = models.TextField(null=False)
    # hierarchic_flag = models.IntegerField()
    # hole_id = models.IntegerField()
    # block_id = models.IntegerField()


class Weather(models.Model):
    # id = models.AutoField(primary_key=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    carrier_shift = models.IntegerField(choices=CARRIER0_SHIFT_CHOICES)


# class AuthUserManager(BaseUserManager):
#     def create_user(self, username, email, password, last_name, first_name):
#         """
#         ユーザ作成
#
#         :param username: ユーザID
#         :param email: メールアドレス
#         :param password: パスワード
#         :param last_name: 苗字
#         :param first_name: 名前
#         :return: AuthUserオブジェクト
#         """
#         if not email:
#             raise ValueError('Users must have an email')
#         if not username:
#             raise ValueError('Users must have an username')
#
#         user = self.model(username=username,
#                           email=email,
#                           password=password,
#                           last_name=last_name,
#                           first_name=first_name)
#         user.is_active = True
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, email, password, last_name, first_name):
#         """
#         スーパーユーザ作成
#
#         :param username: ユーザID
#         :param email: メールアドレス
#         :param password: パスワード
#         :param last_name: 苗字
#         :param first_name: 名前
#         :return: AuthUserオブジェクト
#         """
#         user = self.create_user(username=username,
#                                 email=email,
#                                 password=password,
#                                 last_name=last_name,
#                                 first_name=first_name)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
#
# @python_2_unicode_compatible
# class AuthUser(AbstractBaseUser, PermissionsMixin):
#     """
#     ユーザ情報を管理する
#     """
#     class Meta:
#         verbose_name = 'ユーザ'
#         verbose_name_plural = 'ユーザ'
#
#     def get_short_name(self):
#         """
#               ユーザの苗字を取得する
#
#               :return: 苗字
#               """
#         return self.last_name
#
#     def get_full_name(self):
#         """
#         ユーザのフルネームを取得する
#
#         :return: 苗字 + 名前
#         """
#         return self.last_name + self.first_name
#
#     username = models.CharField(verbose_name='ユーザID',
#                                 unique=True,
#                                 max_length=30)
#     last_name = models.CharField(verbose_name='苗字',
#                                  max_length=30,
#                                  default=None)
#     first_name = models.CharField(verbose_name='名前',
#                                   max_length=30,
#                                   default=None)
#     email = models.EmailField(verbose_name='メールアドレス',
#                               null=True,
#                               default=None)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(verbose_name='有効フラグ',
#                                     default=True)
#     is_staff = models.BooleanField(verbose_name='管理サイトアクセス権限',
#                                    default=False)
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'last_name', 'first_name']
#     objects = AuthUserManager()
#
#     def __str__(self):
#         return self.last_name + ' ' + self.first_name
