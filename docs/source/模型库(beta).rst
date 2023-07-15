模型库(beta)
=======

现金流模型库是集中化的现金流模型仓库,abs用户可以通过API调用获取经过测试验证的现金流模型。

.. note::

   通过Python发起Web API调用,在服务器进行现金流计算，并且返回结果。


范围
--------
* 模型库目前支持订阅模式
    * 通过邮件 (见 “支持”页面)
    * 微信公众号(微信：`ABS工匠`)


使用方式 
--------

1. 登陆

.. code-block:: python

    library_url = "https://absbox.org/library/latest"
    # 测试账户： 用户名test/密码test
    localAPI.loginLibrary("test","test",deal_library=library_url)


2. 查询

传入债券ID

.. code-block:: python

    localAPI.queryLibrary(["22吉时代3A2_bc"],deal_library=library_url)

3. 运行

`22JSD03` 为 前序步骤 查询的产品ID

.. code-block:: python

    r = localAPI.runLibrary("22JSD03"
                           ,deal_library=library_url
                           ,pricing = {"贴现日":"2023-06-22","贴现曲线":[["2020-01-01",0.03]]}
                           ,assump = [{"CPR":0.01}  # 年化早偿付率 1%
                                     ,{"CDR":0.01}  # 年化违约率  1%
                                     ,{"回收":(0.7,18)}]
                           ,reader="china.SPV",read=True)


