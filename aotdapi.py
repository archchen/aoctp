
class AoTdApi(TraderApi):
    def __init__(self):
        pass
    
    def Create(self, pszFlowPath=''):
        """创建TraderApi
        @param pszFlowPath 存贮订阅信息文件的目录，默认为当前目录
        @return 创建出的UserApi
        """

    def Release(self):
        """删除接口对象本身
        @remark 不再使用本接口对象时,调用该函数删除接口对象
        """

    def Init(self):
        """初始化
        @remark 初始化运行环境,只有调用后,接口才开始工作
        """

    def Join(self):
        """等待接口线程结束运行
        @return 线程退出代码
        """
        return 0

    def GetTradingDay(self):
        """获取当前交易日
        @retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日
        """
        return ''

    def RegisterFront(self, pszFrontAddress):
        """注册前置机网络地址
        @param pszFrontAddress：前置机网络地址。
        @remark 网络地址的格式为：“protocol:
        ipaddress:port”，如：”tcp:
        127.0.0.1:17001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        """

    def SubscribePrivateTopic(self, nResumeType):
        """订阅私有流。
        @param nResumeType 私有流重传方式
                SECURITY_TERT_RESTART:从本交易日开始重传
                SECURITY_TERT_RESUME:从上次收到的续传
                SECURITY_TERT_QUICK:只传送登录后私有流的内容
        @remark 该方法要在Init方法前调用。若不调用则不会收到私有流的数据。
        """

    def SubscribePublicTopic(self, nResumeType):
        """订阅公共流。
        @param nResumeType 公共流重传方式
                SECURITY_TERT_RESTART:从本交易日开始重传
                SECURITY_TERT_RESUME:从上次收到的续传
                SECURITY_TERT_QUICK:只传送登录后公共流的内容
        @remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
        """

    def ReqUserLogin(self, pReqUserLogin, nRequestID):
        """用户登录请求"""
        return 0

    def ReqUserLogout(self, pUserLogout, nRequestID):
        """登出请求"""
        return 0

    def ReqOrderInsert(self, pInputOrder, nRequestID):
        """报单录入请求"""
        return 0

    def ReqOrderAction(self, pInputOrderAction, nRequestID):
        """报单操作请求"""
        return 0

    def ReqUserPasswordUpdate(self, pUserPasswordUpdate, nRequestID):
        """用户口令更新请求"""
        return 0

    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, nRequestID):
        """资金账户口令更新请求"""
        return 0

    def ReqQryExchange(self, pQryExchange, nRequestID):
        """请求查询交易所"""
        return 0

    def ReqQryInstrument(self, pQryInstrument, nRequestID):
        """请求查询合约"""
        return 0

    def ReqQryInvestor(self, pQryInvestor, nRequestID):
        """请求查询投资者"""
        return 0

    def ReqQryTradingCode(self, pQryTradingCode, nRequestID):
        """请求查询交易编码"""
        return 0

    def ReqQryTradingAccount(self, pQryTradingAccount, nRequestID):
        """请求查询资金账户"""
        return 0

    def ReqQryDepthMarketData(self, pQryDepthMarketData, nRequestID):
        """请求查询行情"""
        return 0

    def ReqQryBondInterest(self, pQryBondInterest, nRequestID):
        """请求查询债券利息"""
        return 0

    def ReqQryMarketRationInfo(self, pQryMarketRationInfo, nRequestID):
        """请求查询市值配售信息"""
        return 0

    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate, nRequestID):
        """请求查询合约手续费率"""
        return 0

    def ReqQryOrder(self, pQryOrder, nRequestID):
        """请求查询报单"""
        return 0

    def ReqQryTrade(self, pQryTrade, nRequestID):
        """请求查询成交"""
        return 0

    def ReqQryInvestorPosition(self, pQryInvestorPosition, nRequestID):
        """请求查询投资者持仓"""
        return 0

    def ReqFundOutByLiber(self, pInputFundTransfer, nRequestID):
        """Liber发起出金请求"""
        return 0

    def ReqQryFundTransferSerial(self, pQryFundTransferSerial, nRequestID):
        """资金转账查询请求"""
        return 0

    def OnFrontConnected(self):
        """当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。"""

    def OnFrontDisconnected(self, nReason):
        """当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
        @param nReason 错误原因
                0x1001 网络读失败
                0x1002 网络写失败
                0x2001 接收心跳超时
                0x2002 发送心跳失败
                0x2003 收到错误报文
        """

    def OnHeartBeatWarning(self, nTimeLapse):
        """心跳超时警告。当长时间未收到报文时，该方法被调用。
        @param nTimeLapse 距离上次接收报文的时间
        """

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        """错误应答"""

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        """登录请求响应"""

    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        """登出请求响应"""

    def OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        """报单录入请求响应"""

    def OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
        """报单操作请求响应"""

    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        """用户口令更新请求响应"""

    def OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        """资金账户口令更新请求响应"""

    def OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast):
        """请求查询交易所响应"""

    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        """请求查询合约响应"""

    def OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast):
        """请求查询投资者响应"""

    def OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast):
        """请求查询交易编码响应"""

    def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        """请求查询资金账户响应"""

    def OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast):
        """请求查询行情响应"""

    def OnRspQryBondInterest(self, pBondInterest, pRspInfo, nRequestID, bIsLast):
        """请求查询债券利息响应"""

    def OnRspQryMarketRationInfo(self, pMarketRationInfo, pRspInfo, nRequestID, bIsLast):
        """请求查询市值配售信息响应"""

    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
        """请求查询合约手续费率响应"""

    def OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast):
        """请求查询报单响应"""

    def OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast):
        """请求查询成交响应"""

    def OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
        """请求查询投资者持仓响应"""

    def OnRtnOrder(self, pOrder):
        """报单通知"""

    def OnRtnTrade(self, pTrade):
        """成交通知"""

    def OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        """报单录入错误回报"""

    def OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
        """报单操作错误回报"""

    def OnRspFundOutByLiber(self, pInputFundTransfer, pRspInfo, nRequestID, bIsLast):
        """Liber发起出金应答"""

    def OnRtnFundOutByLiber(self, pFundTransfer):
        """Liber发起出金通知"""

    def OnErrRtnFundOutByLiber(self, pInputFundTransfer, pRspInfo):
        """iber发起出金错误回报"""

    def OnRtnFundInByBank(self, pFundTransfer):
        """银行发起入金通知"""

    def OnRspQryFundTransferSerial(self, pFundTransfer, pRspInfo, nRequestID, bIsLast):
        """资金转账查询应答"""
