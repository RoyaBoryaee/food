from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.utils import timezone
import uuid
from django.urls import reverse , reverse_lazy


def upload_location(instance, filename):
    print('upload location')
    return str(instance.id)+'/'

class Worker(models.Model):
    positions = {'MCH': 'Master Chef',
                 'CH': 'Chef',
                 'W': 'Waitress',
                 'CA': 'Cashier'}

    name = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    position = models.CharField(positions, max_length=3)
    home_addr = models.CharField(max_length=1000)
    regex_phoneNumber = RegexValidator(regex=r"0(21|26|25|86|24|23|81|28|31|44|11|74|83|51|45|17|41|54|87|71|66|34"
                                             r"|56|13|77|76|61|38|58|35|84)\d{8}$")
    regex_mobileNumber = RegexValidator(regex=r"^(\+98|0)?9\d{9}$",
                                        message="""your number isn't correct.
                                        true formats :
                                        1) +989999999999 2)09999999999""")
    regex_nationalcode=RegexValidator(regex=r"^\d{10}$", message=" should be number with 10 digit")
    national_code = models.CharField(unique = True, max_length = 10, validators=[regex_nationalcode])
    # how many times using our service???
    phone_number = models.CharField(max_length=100, validators=[regex_phoneNumber])
    mobile_number = models.CharField(max_length=100, validators=[regex_mobileNumber])
    profile = models.ImageField(blank=False, null=False, upload_to =upload_location)
    published_date = models.DateField(default=timezone.now())


    def __str__(self):
        return self.name+" "+self.f_name

    def get_absolute_url(self):
        return reverse('restaurant_admin:Worker_detail', args=[self.id])



# ??????
class Table(models.Model):
    table_number = models.IntegerField(primary_key=True)
    table_availability = models.BooleanField(default=True)
    #table_ready = models.BooleanField(default=True)
    reservation_state = models.BooleanField(default=False)

    def __str__(self):
        return str(self.table_number)

    def get_absolute_url(self):
        print('yes')
        return reverse('restaurant_admin:Table_detail', args=[self.table_number])

class FoodCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        print(self.id)
        return reverse('restaurant_admin:FoodCategory_detail', args=[self.id])


class Food(models.Model):
    food_name = models.CharField(unique=True, max_length=100)
    food_details = models.CharField(max_length=1000, validators=[MinLengthValidator(50)])
    food_availability = models.BooleanField(default=True)
    cost = models.IntegerField(default=0)
    food_category = models.ForeignKey(FoodCategory, related_name='Food_FoodCategory', on_delete=models.CASCADE)
    food_img = models.ImageField(blank=False, null=True,  upload_to =upload_location)
    takeaway_price = models.BooleanField(default=True)

    def __str__(self):
        print(self.food_name)
        return self.food_name

    def get_absolute_url(self):
        return reverse('restaurant_admin:Food_detail', args=[self.id])


class OrderList(models.Model):
    STATUSES = (('NO','Not Ordered'),
                ('CH','Change Order'),
                ('OR','Ordered'),
                ('PR','Preparing'),
                ('RE', 'Ready'),
                ('DE','Delivered'),)
    # table or null
    table = models.ForeignKey(Table, related_name="OrderList_Table", on_delete=models.CASCADE)
    details = models.CharField(max_length=1000)
    # if takeaway= 1 then table ???
    takeaway = models.BooleanField(default=False)
    status = models.CharField(max_length=2, default='NO',choices=STATUSES)
    cost = models.PositiveIntegerField(default=1)


class FoodOrder(models.Model):
    food = models.ForeignKey(Food,related_name='ordered_food', on_delete=models.CASCADE)
    number = models.IntegerField()
    order_list = models.ForeignKey(OrderList, related_name='FoodOrder_list', on_delete=models.CASCADE, blank=True, null=True)
    cost = models.PositiveIntegerField()

    def __str__(self):
        return self.food.food_name

class Subscription(models.Model):
    # or national code ????
    sub_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sub_name = models.CharField(max_length=100)
    sub_birthDate = models.DateField()
    sub_address = models.CharField(max_length=1000)
    regex_phoneNumber = RegexValidator(regex=r"0(21|26|25|86|24|23|81|28|31|44|11|74|83|51|45|17|41|54|87|71|66|34"
                                             r"|56|13|77|76|61|38|58|35|84)[0-9]+")
    regex_mobileNumber = RegexValidator(regex=r"^(\+98|0)?9\d{9}",
                                        message="""your number isn't correct.
                                        true formats :
                                        1) +989999999999 2)09999999999""")
    # how many times using our service???
    sub_phone = models.CharField(max_length=100, validators=[regex_phoneNumber])
    sub_mobile_phone = models.CharField(max_length=100, validators=[regex_mobileNumber])

class Cost(models.Model):
    tax = models.PositiveIntegerField(default=1)
    service_charge = models.PositiveIntegerField(default=1)
    packaging_cost =  models.PositiveIntegerField(default=1)

    def get_absolute_url(self):
        return reverse('restaurant_admin:Cost_detail', args=[self.id])
