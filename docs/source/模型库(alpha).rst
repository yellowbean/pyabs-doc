模型库（alpha）
====

现金流模型库是集中化的现金流模型仓库，abs用户可以通过API调用获取已经经过测试验证的现金流模型。

.. note::

   通过Python发起Web API调用,从服务器中获取已经持久化的现金流模型对象。


范围
----
* 模型库目前支持订阅模式
    * 通过邮件 (见 “支持”页面)
    * 微信公众号(微信：`ABS工匠`)
* 建模范围：银行间市场汽车贷款，住房贷款类产品

使用方式 
----

1. 调用接口

.. code-block:: python

    from absbox.local.china import 信贷ABS
    信贷ABS.pull("21信融宜居1A1","/local/disk/path",url="https://asset-backed.org/library")
    # 注意，只有建模过的文件才能通过API下载。

2. 分析

本地文件会产生一个 ``.obj`` 结尾的文件。

3. 载入

.. code-block:: python

  ...
  from absbox.local.china import 信贷ABS
  deal = 信贷ABS.load("path/to/file.obj")


