import untils
from Api.apiFactory import ApiFactory


class TestOrderApi:

    def test_order_list(self):
        """订单列表"""

        # 响应对象
        res = ApiFactory.get_order_api().order_list_api()
        # 断言 状态码
        untils.common_assert_code(res)

        # 断言页面是否是第一个
        assert res.json().get("current_page") == 1
        # 断言 订单数据大于0 根据用户数据决定
        assert len(res.json()) > 0
        # 断言关键字段

        assert False not in [i in res.text for i in ["id", "order_no", "total_price"]]

    def test_order_api(self):
        """创建订单"""
        # 商品id
        product_id = 7
        # 购买数量
        count = 3
        # 响应对象
        res = ApiFactory.get_order_api().create_order_api(product_id, count)

        # 断言 状态码
        untils.common_assert_code(res)

        # 订单编号 和 订单id 不为空
        assert len(res.json().get("order_no")) > 0 and len(res.json().get("order_id")) > 0

        # 断言订单是否通过
        assert res.json().get("pass") is True

    def test_query_order(self):
        """查询订单"""
        # 订单id
        order_id = 115
        # 响应对象
        res = ApiFactory.get_order_api().query_order_api(order_id)

        # 断言 状态码
        untils.common_assert_code(res)

        # 断言订单id
        assert res.json().get("id") == 115

        # 断言地址 用户名 手机号
        assert res.json().get("snap_address").get("name") == "大大"
        assert res.json().get("snap_address").get("mobile") == "13888888888"
