from django.contrib import admin
from .models import FoodOrder, Food, FoodCategory, OrderList, Table, Subscription, Worker


admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(FoodOrder)
admin.site.register(OrderList)
admin.site.register(Table)
admin.site.register(Subscription)
admin.site.register(Worker)
