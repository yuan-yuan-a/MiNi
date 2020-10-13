from Api.apiFactory import ApiFactory
import app,untils

class TestUserApi:

    def test_get_tokrn(self):
        """获取token"""
        # 响应对象
        res = ApiFactory.get_user_api().get_token_api()
        # 断言响应状态码
        untils.common_assert_code(res)
        # 断言token存在
        assert len(res.json().get("token")) > 0
        # 保存token
        app.headers["token"] = res.json().get("token")
        print("app.headers:{}".format(app.headers))

    def test_verify_token(self):
        """验证token"""
        # 响应对象
        res = ApiFactory.get_user_api().verify_token_api()
        # 断言状态码
        untils.common_assert_code(res)
        # 断言有效
        assert res.json().get("isValid") is True

    def test_user_address(self):
        # 响应对象
        res = ApiFactory.get_user_api().user_address_api()
        # 断言状态码
        untils.common_assert_code(res)
        # 断言信息
        assert False not in [i in res.text for i in ["大大","13888888888","上海市","上海市","浦东新区","2102"]]