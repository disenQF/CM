import xadmin as admin

from order.models import Address, Order

# Register your models here.
class AddressAdmin():
    list_display = ('address', 'city', 'phone', 'user')
    search_fields = ('address', 'phone')

class OrderAdmin():
    list_display = ('user',
                    'title',
                    'price',
                    'address',
                    'pay_type_name',
                    'pay_state_name',
                    'add_time',
                    'order_sn')

    search_fields = ('title', 'order_sn')


admin.site.register(Address, AddressAdmin)
admin.site.register(Order, OrderAdmin)



