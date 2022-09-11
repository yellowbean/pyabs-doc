JY_RMBS_01 = 信贷ABS(
    "建元"
    ,("2022-10-02","2022-10-02","2022-11-02")
    ,"每月"
    ,{"清单":[["按揭贷款"
          ,{"放款金额":18_000_000_000,"放款利率":["固定",0.0485],"初始期限":180
          ,"频率":"每月","类型":"等额本息","放款日":"2020-06-01"}
          ,{"当前余额":17_000_000_000
          ,"当前利率":0.04
          ,"剩余期限":180
          ,"状态":"正常"}]]
     }
    ,(("本金分账户",{"余额":0})
      ,("储备账户",{"余额":0})
      ,("收入分账户",{"余额":0})
      ,("信托税收",{"余额":0}))
    ,(("A1",{"当前余额":3_000_000_000
                             ,"当前利率":0.03
                             ,"初始余额":3_000_000_000
                             ,"初始利率":0.03
                             ,"起息日":"2020-01-03"
                             ,"利率":{"浮动":["LPR5Y",0.01,{"重置月份":3}]}
                             ,"债券类型":{"过手摊还":None}
                            })
      ,("A2",{"当前余额":5_000_000_000
                             ,"当前利率":0.03
                             ,"初始余额":5_000_000_000
                             ,"初始利率":0.03
                             ,"起息日":"2020-01-03"
                             ,"利率":{"浮动":["LPR5Y",0.01,{"重置月份":3}]}
                             ,"债券类型":{"过手摊还":None}
                            })
      ,("A3",{"当前余额":6_999_000_000
                             ,"当前利率":0.03
                             ,"初始余额":5_000_000_000
                             ,"初始利率":0.03
                             ,"起息日":"2020-01-03"
                             ,"利率":{"浮动":["LIBOR1M",0.01,{"重置月份":3}]}
                             ,"债券类型":{"过手摊还":None}
                            })
      ,("次级",{"当前余额":2_123_875_534.53
                             ,"当前利率":0.03
                             ,"初始余额":2_123_875_534.53
                             ,"初始利率":0.03
                             ,"起息日":"2020-01-03"
                             ,"利率":{"固定":0.0}
                             ,"债券类型":{"过手摊还":None}
                            }))
    ,(("增值税",{"类型":{"百分比费率":["资产池当期利息",0.0325]}})
      ,("服务商费用",{"类型":{"年化费率":["资产池余额",0.02]}}))
    ,{"未违约":[
         ["支付费用限额",["收入分账户"],["服务商费用"],{"应计费用百分比":0.5}]
         ,["支付利息","收入分账户",["A1","A2","A3"]]
         ,["支付费用",["收入分账户"],["服务商费用"]]
         ,["账户转移","收入分账户","本金分账户"]
         ,["支付本金","本金分账户",["A1"]]
         ,["支付本金","本金分账户",["A2"]]
         ,["支付本金","本金分账户",["A3"]]
         ,["支付本金","本金分账户",["次级"]]
         ,["支付收益","本金分账户","次级"]],
     "回款后":[["支付费用",["收入分账户"],["增值税"]]]
     }
    ,(["利息回款","收入分账户"]
      ,["本金回款","本金分账户"]
      ,["早偿回款","本金分账户"]
      ,["回收回款","本金分账户"])
    ,None
)