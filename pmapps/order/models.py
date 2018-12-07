from datetime import datetime

from django.db import models, connection

from user.models import UserProfile


# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=100,
                               verbose_name='地址')

    city = models.CharField(max_length=20,
                            verbose_name='城市')

    phone = models.CharField(max_length=12,
                             verbose_name='电话')

    is_default = models.BooleanField(verbose_name='是否默认',
                                     default=False)

    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE,
                             verbose_name='所属用户')

    def __str__(self):
        return self.address

    class Meta:
        db_table = 't_address'
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name


class OrderNumAutoField(models.CharField):
    def get_db_prep_value(self, value, connection, prepared=False):
        today = datetime.today().strftime('%Y%m%d')  # 20181207
        cursor = connection.cursor()

        cursor.execute('select max(order_sn) from t_order')
        max_order_sn = cursor.fetchone()[0]  # ('20181212000001',)  或 (None,)

        cursor.close()

        if max_order_sn:
            max_order_date = max_order_sn[:8]  # yyyymmdd
            if today == max_order_date:
                sn = str(int(max_order_sn[8:])+1)
                return today + sn.rjust(6, '0')

        return today + '000001'  # 今天的第一单




class Order(models.Model):
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE,
                             verbose_name='用户')
    title = models.CharField(max_length=100,
                             verbose_name='标题')

    # 自动生成： yyyymmdd000001
    order_sn = OrderNumAutoField(max_length=20,
                                 editable=False,
                                 verbose_name='订单号')

    price = models.DecimalField(verbose_name='金额(元)',
                                max_digits=10,
                                decimal_places=2)

    # 根据实际情况是否关联"地址表"
    # 常见：在页面时选择地址， 在订单存储时，只存储地址内容
    address = models.ForeignKey(Address,
                                on_delete=models.SET_NULL,
                                null=True,
                                verbose_name='收货地址')

    pay_states = ((0, '待支付'),
                  (1, '已支付'),
                  (2, '正在支付'),
                  (3, '待退款'),
                  (4, '已退款'))

    pay_state = models.IntegerField(verbose_name='支付状态',
                                    choices=pay_states,
                                    default=0)

    pay_types = ((0, '余额'),
                 (1, '网银'),
                 (2, '支付宝'),
                 (3, '微信'))

    pay_type = models.IntegerField(verbose_name='支付类型',
                                   choices=pay_types,
                                   default=0)
    @property
    def pay_state_name(self):
        return self.pay_states[self.pay_state][1]

    @property
    def pay_type_name(self):
        return self.pay_types[self.pay_type][1]

    add_time = models.DateTimeField(verbose_name='下单时间',
                                    auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_order'
        verbose_name = '用户订单'
        verbose_name_plural = verbose_name