模型库(beta)
============

`模型库` 是部署于云端，包含已建模的产品集合,用户通过absbox API调用现金流模型进行测算,估值。

.. note::

   通过Python发起Web API调用,在服务器进行现金流计算,并且返回结果。
   模型库也可以单独部署于公网或者内网。


范围
--------

目前 `模型库` 公募信贷ABS市场慢速拓展中。如果有产品需要优先建模,请通过公众号进行留言

    * 微信公众号 ``ABS工匠``

对于特殊产品仅对个别用户开放，需单独创建用户和权限，请在公众号留言。

使用方式 
--------

认证
^^^^^^^^^

`library_url` 指向模型库服务器地址。

.. code-block:: python

    library_url = "https://absbox.org/library/latest"
    # 测试账户： 用户名test/密码test
    localAPI.loginLibrary("test","test",deal_library=library_url)


查询
^^^^^^^^^

用户可以通过传入债券ID,以及选择性参数,对模型库中的模型进行查询。

.. code-block:: python

    localAPI.queryLibrary(["22吉时代3A2_bc"],deal_library=library_url)

其他可选参数：

.. code-block:: python

    localAPI.queryLibrary(["22吉时代3A2_bc"]
                          ,deal_library=library_url
                          ,read=True  # 是否返回为dataframe
                          ,prod=True  # 是否只包括正式模型 
                          ,history=False # 是否包括历史模型 
                          ,and_tags=[]  # 必须包含所有列举的标签
                          ,or_tags=[]   # 任意包含列举的标签
                          )


运行
^^^^^^^^^
此步骤只需要传入

* 产品ID : `22JSD03` 为 前序步骤 查询的产品ID
* 模型库地址: 即 deal_library 
* 假设: 同 :ref:`2. assumptions`
* 定价假设: :ref:`3. pricing assumption`
* reader: 如果中国产品选择 "china.SPV"

.. code-block:: python

    r = localAPI.runLibrary("22JSD03"
                           ,deal_library=library_url
                           ,pricing = {"贴现日":"2023-06-22","贴现曲线":[["2020-01-01",0.03]]}
                           ,assump = [{"CPR":0.01}  # 年化早偿付率 1%
                                     ,{"CDR":0.01}  # 年化违约率  1%
                                     ,{"回收":(0.7,18)}]
                           ,reader="china.SPV"
                           ,read=True)

返回值和 API.run() 一致。
