import app, requests


class ProductApi:
    """商品分类"""

    def __init__(self):
        self.product_classify_url = app.base_url + "/category/all"
        self.classify_product_url = app.base_url + "/product/by_category"
        self.product_detail_url = app.base_url + "/product/{}"

    def product_classify_api(self):
        """"商品分类"""
        return requests.get(self.product_classify_url)

    def classify_product_api(self, classify_id=2):
        """分类系商品"""
        # 请求数据
        data = {"id": classify_id}
        return requests.get(self.classify_product_url, params=data)

    def product_detail_api(self, product_id=2):
        """"商品信息 """
        return requests.get(self.product_detail_url.format(product_id))
