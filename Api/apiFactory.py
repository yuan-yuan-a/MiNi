from Api.home import HomeApi
from Api.product import ProductApi
from Api.user import UserApi
from Api.order import orderApi


class ApiFactory:
    @classmethod
    def get_home_api(cls):
        """返回首页api"""
        return HomeApi()

    @classmethod
    def get_product_api(cls):
        return ProductApi()

    @classmethod
    def get_user_api(cls):
        """返回用户api"""
        return UserApi()

    @classmethod
    def get_order_api(cls):
        return orderApi()
