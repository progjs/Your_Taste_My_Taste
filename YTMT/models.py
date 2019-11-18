from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

# 메뉴
class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank = False, null = False)
    img_url = models.TextField(null=True)
    text = models.TextField(null=True)
    def __str__(self):
        return self.name

class Menu2(models.Model):
    menu_id = models.IntegerField(blank = False, null = False, primary_key=True)
    name = models.CharField(max_length=50, blank = False, null = False)
    text = models.CharField(max_length=1000)
    img = models.CharField(max_length=10000)

class Ingredient(models.Model):
    ingre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank = False, null = False)
    # type(유제품/육류/어류)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    ingre_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    def __str__(self):
        return self.menu_id.name + " " + self.ingre_id.name

# 회원정보
class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)

    Gender_TYPE = (
        (1, "남자"),
        (2, "여자"),
    )

    Religion_TYPE = (
        (1, "힌두교"), (2, "불교"),
        (3, "기독교"), (4, "천주교"),
        (5, "이슬람교"), (6, "유대교"),
        (7, "시크교도"), (8, "무교"),
    )

    Vegetarian_TYPE = (
        (1, "비건"), (2, "락토 베지테리언"),
        (3, "오보 베지테리언"), (4, "락토 오보 베지테리언"),
        (5, "페스코 베지테리언"), (6, "플로 베지테리언"),
        (7, "플렉시테리언"), (8, "해당사항없음"),
    )

    gender = models.IntegerField(blank = False, null = False, choices=Gender_TYPE, default=1)
    birth = models.DateTimeField(blank = False, null = False)
    reli_id = models.IntegerField(choices=Religion_TYPE, default=8)
    vege_id = models.IntegerField(choices=Vegetarian_TYPE, default=8)
    def __str__(self):
        return self.user_id


class Allergy(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    ingre_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_id.username + ":" + self.ingre_id.name

class Hate_menu(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_id.username + ":" + self.menu_id.name

class Hate_ingredient(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    ingre_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username+ ":" + self.ingre_id.name

class History(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_id.username + ":" + self.menu_id.name

# class Friend(models.Model):
#     user_id=models.ForeignKey(User, on_delete=models.CASCADE)
#     friend_id=models.ForeignKey(Friend, on_delete=models.CASCADE)
# class Relation(models.Model):
#     user_id = models.OneToOneField(User, on_delete = models.CASCADE)
#     friend_id = models.ForeignKey(User, on_delete=models.CASCADE)

# class restaurant():
