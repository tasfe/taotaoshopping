# -*- coding: utf-8 -*-


import urllib
import urllib2
import string
import time
import md5
import re
import types
import logging
import simplejson as json


API_KEY = '12002052'
APP_SECRET ='122519af68fe1ded1b178aa2b5a03cd8'

########################################################################
class TaobaoApi:
    """taobao平台api"""
        
    def taobaoke_items_get(self,paramArray):
	"""taobao.taobaoke.items.get (查询淘宝客推广商品)"""
	try:
	    paramArray['app_key'] = API_KEY
	    paramArray['method'] = 'taobao.taobaoke.items.get'
	    paramArray['format'] = 'json'
	    paramArray['timestamp'] = time.strftime('%Y-%m-%d %X', time.localtime())
	    paramArray['v'] = '1.0'
	    sign = self._sign(paramArray, APP_SECRET);
	    paramArray['sign'] = sign
	    
	    if  paramArray.has_key('area'):
		area = paramArray['area'] 
		paramArray['area']  = area.encode('utf-8')
	     
	    #组装参数
	    form_data = urllib.urlencode(paramArray)
	     
	    #访问服务
	    urlopen = urllib2.urlopen('http://gw.api.taobao.com/router/rest', form_data)
	     
	    rsp = urlopen.read()
	    rsp = rsp.decode('UTF-8')
	    
	    if  rsp:
		rsp_obj =  json.loads(rsp)['rsp']
		if rsp_obj:
		    return rsp_obj['taobaokeItems']
	except Exception, e:
	    import traceback
	    traceback.print_exc()
	    return None
	              

        
    def _sign(self,param,sercetCode):
	import hashlib
	src = sercetCode + ''.join(["%s%s" % (k, v) for k, v in sorted(param.items())])
	return hashlib.md5(src.encode('utf-8')).hexdigest().upper()

from PyQt4 import QtCore, QtGui
from taotao_ui import Ui_MainWindow
import dbutils as db
########################################################################
class Taotao:
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.api = TaobaoApi()	

	import sys
	self.app = QtGui.QApplication(sys.argv)
	self.window = QtGui.QMainWindow()
	self.ui = Ui_MainWindow()
	self.ui.setupUi(self.window)
	
	
	self.initEvent()
	self.initInterface()
	self.initTable()

	self.app.setStyle("plastique")
	
	self.window.show()
	sys.exit(self.app.exec_())
      
    def initEvent(self):
	QtCore.QObject.connect(self.ui.submitButton,QtCore.SIGNAL("clicked()"),self.queryItems)
	QtCore.QObject.connect(self.ui.data_view,QtCore.SIGNAL("clicked(QModelIndex)"),self.selectItem)
	
    def initTable(self):
	self.tabModel = QtGui.QStandardItemModel()
	self.fillTableHeader()
	self.ui.data_view.setModel(self.tabModel)
	self.ui.data_view.setSortingEnabled(True)
	self.ui.data_view.resizeColumnsToContents()
	
	
    
    def initInterface(self):
	
	#初始化页数
	self.ui.page_size.setValue(30)
	#初始化排序
	self.ui.sort.addItem(u"默认排序",QtCore.QVariant('default'))
	self.ui.sort.addItem(u"价格从高到低",QtCore.QVariant('price_desc'))
	self.ui.sort.addItem(u"价格从低到高",QtCore.QVariant('price_asc'))
	self.ui.sort.addItem(u"信用等级从高到低",QtCore.QVariant('credit_desc'))

	#初始化商家信用
	self.ui.start_credit.addItem(u"任意")
	self.ui.start_credit.addItem(u"一心",QtCore.QVariant('1heart'))
	self.ui.start_credit.addItem(u"二心",QtCore.QVariant('2heart'))
	self.ui.start_credit.addItem(u"三心",QtCore.QVariant('3heart'))
	self.ui.start_credit.addItem(u"四心",QtCore.QVariant('4heart'))
	self.ui.start_credit.addItem(u"五心",QtCore.QVariant('5heart'))
	self.ui.start_credit.addItem(u"一钻",QtCore.QVariant('1diamond'))
	self.ui.start_credit.addItem(u"二钻",QtCore.QVariant('2diamond'))
	self.ui.start_credit.addItem(u"三钻",QtCore.QVariant('3diamond'))
	self.ui.start_credit.addItem(u"四钻",QtCore.QVariant('4diamond'))
	self.ui.start_credit.addItem(u"五钻",QtCore.QVariant('5diamond'))
	self.ui.start_credit.addItem(u"一冠",QtCore.QVariant('1crown'))
	self.ui.start_credit.addItem(u"二冠",QtCore.QVariant('2crown'))
	self.ui.start_credit.addItem(u"三冠",QtCore.QVariant('3crown'))
	self.ui.start_credit.addItem(u"四冠",QtCore.QVariant('4crown'))
	self.ui.start_credit.addItem(u"五冠",QtCore.QVariant('5crown'))
	self.ui.start_credit.addItem(u"一皇冠",QtCore.QVariant('1goldencrown'))
	self.ui.start_credit.addItem(u"二皇冠",QtCore.QVariant('2goldencrown'))
	self.ui.start_credit.addItem(u"三皇冠",QtCore.QVariant('3goldencrown'))
	self.ui.start_credit.addItem(u"四皇冠",QtCore.QVariant('4goldencrown'))
	self.ui.start_credit.addItem(u"五皇冠",QtCore.QVariant('5goldencrown'))	
	
	self.ui.end_credit.addItem(u"任意")
        self.ui.end_credit.addItem(u"一心",QtCore.QVariant('1heart'))
	self.ui.end_credit.addItem(u"二心",QtCore.QVariant('2heart'))
	self.ui.end_credit.addItem(u"三心",QtCore.QVariant('3heart'))
	self.ui.end_credit.addItem(u"四心",QtCore.QVariant('4heart'))
	self.ui.end_credit.addItem(u"五心",QtCore.QVariant('5heart'))
	self.ui.end_credit.addItem(u"一钻",QtCore.QVariant('1diamond'))
	self.ui.end_credit.addItem(u"二钻",QtCore.QVariant('2diamond'))
	self.ui.end_credit.addItem(u"三钻",QtCore.QVariant('3diamond'))
	self.ui.end_credit.addItem(u"四钻",QtCore.QVariant('4diamond'))
	self.ui.end_credit.addItem(u"五钻",QtCore.QVariant('5diamond'))
	self.ui.end_credit.addItem(u"一冠",QtCore.QVariant('1crown'))
	self.ui.end_credit.addItem(u"二冠",QtCore.QVariant('2crown'))
	self.ui.end_credit.addItem(u"三冠",QtCore.QVariant('3crown'))
	self.ui.end_credit.addItem(u"四冠",QtCore.QVariant('4crown'))
	self.ui.end_credit.addItem(u"五冠",QtCore.QVariant('5crown'))
	self.ui.end_credit.addItem(u"一皇冠",QtCore.QVariant('1goldencrown'))
	self.ui.end_credit.addItem(u"二皇冠",QtCore.QVariant('2goldencrown'))
	self.ui.end_credit.addItem(u"三皇冠",QtCore.QVariant('3goldencrown'))
	self.ui.end_credit.addItem(u"四皇冠",QtCore.QVariant('4goldencrown'))
	self.ui.end_credit.addItem(u"五皇冠",QtCore.QVariant('5goldencrown'))	
	
	#初始化区域
	self.ui.area.addItem(u"所有地区",QtCore.QVariant(u""))
	self.ui.area.addItem(u"江浙沪",QtCore.QVariant(u"江苏,浙江,上海"))
	self.ui.area.addItem(u"港澳台",QtCore.QVariant(u"香港,澳门,台湾"))
	self.ui.area.addItem(u"海外",QtCore.QVariant(u"美国,英国,法国,瑞士,澳洲,新西兰,加拿大,奥地利,韩国,日本,德国,意大利,西班牙,俄罗斯,泰国,印度,荷兰,新加坡,其它国家"))
	
	areas = [u'北京',u'上海',u'杭州',u'广州',u'深圳',u'南京',u'武汉',u'天津',u'成都',u'哈尔滨',u'重庆',u'宁波',u'无锡',u'济南',u'苏州',u'温州',u'青岛',u'沈阳',u'福州',u'西安',u'长沙',u'合肥',u'南宁',u'南昌',u'郑州',u'厦门',u'大连',u'常州',u'石家庄',u'东莞',u'安徽',u'福建',u'甘肃',u'广东',u'广西',u'贵州',u'海南',u'河北',u'黑龙江',u'河南',u'湖北',u'湖南',u'江苏',u'江西',u'吉林',u'辽宁',u'内蒙古',u'宁夏',u'青海',u'山东',u'山西',u'陕西',u'四川',u'新疆',u'西藏',u'云南',u'浙江']
	for a in areas:
	    self.ui.area.addItem(a,QtCore.QVariant(a))


        #初始化分类
	self.ui.cat.addItem(u"所有分类",QtCore.QVariant(""))
	
	cats = {
	    "99":u"网络游戏点卡",
	    "50017708":u"网游装备、游戏币、帐号、代练",
	    "40":u"腾讯QQ专区",
	    "50004958":u"移动联通小灵通充值中心",
	    "50008907":u"IP卡、网络电话、手机号码",
	    "1512":u"品牌手机",
	    "50019321":u"国货精品手机",
	    "50018367":u"手机配件",
	    "11":u"电脑硬件、台式整机、网络设备",
	    "1101":u"笔记本电脑",
	    "50018377":u"笔记本配件",
	    "14":u"数码相机、摄像机、图形冲印",
	    "1201":u"MP3、MP4、iPod、录音笔",
	    "50008090":u"3C数码配件市场",
	    "50007218":u"办公设备、办公用品及耗材",
	    "50018627":u"电子辞典/学习机、文具",
	    "50018908":u"影音电器",
	    "50017285":u"国货精品视听",
	    "50018957":u"生活电器",
	    "50018930":u"厨房电器",
	    "50008168":u"网络服务、电脑软件",
	    "50019393":u"闪存卡、U盘、移动存储",
	    "50010788":u"彩妆/香水/美发/工具",
	    "1801":u"美容护肤/美体/精油",
	    "50015926":u"珠宝、钻石、翡翠、黄金",
	    "50005700":u"品牌手表、流行手表",
	    "1705":u"饰品、流行首饰、时尚饰品",
	    "16":u"女装、女士精品",
	    "50006843":u"女鞋",
	    "50006842":u"男女箱包、单肩包、手提包、旅行箱",
	    "1625":u"女士内衣、男士内衣、家居服",
	    "50016853":u"男鞋/皮鞋/休闲鞋",
	    "30":u"男装",
	    "50010404":u"配件、皮带、围巾、领带、帽子手套",
	    "50010728":u"运动、瑜伽、健身、球迷用品",
	    "50016756":u"运动服、运动包、颈环配件",
	    "50010388":u"运动鞋",
	    "2203":u"户外、登山、野营、涉水",
	    "50018963":u"旅游度假、打折机票、特惠酒店",
	    "50008165":u"童装、童鞋、婴儿服、孕妇装",
	    "35":u"奶粉、尿片、母婴用品",
	    "50005998":u"益智玩具、童车、童床、书包",
	    "21":u"居家日用、厨房餐饮、卫浴洗浴",
	    "2128":u"时尚家饰、工艺品、十字绣",
	    "50019142":u"个人护理保健",
	    "50008164":u"家具、家具定制、宜家代购",
	    "50008163":u"家纺床上用品地毯布艺",
	    "27":u"装潢、灯具、五金、安防、卫浴",
	    "50008825":u"保健食品",
	    "50002766":u"食品、茶叶、零食、特产",
	    "23":u"古董、邮币、字画、收藏",
	    "26":u"汽车、配件、改装、摩托、自行车",
	    "29":u"宠物、宠物食品及用品",
	    "28":u"ZIPPO、瑞士军刀、眼镜",
	    "2813":u"成人用品、避孕用品、情趣内衣",
	    "33":u"书籍、杂志、报纸",
	    "34":u"音乐、影视、明星、乐器",
	    "20":u"电玩、配件、游戏、攻略",
	    "25":u"模型、娃娃、人偶、毛绒、KITTY",	
	    "50008075":u"演出、旅游、吃喝玩乐折扣券",
	    "50007216":u"鲜花速递、蛋糕配送、园艺花艺",								
	    "50003754":u"网店装修、用品、物流快递、图片存储"
	}
	
	for k,v in cats.items():
	    self.ui.cat.addItem(v,QtCore.QVariant(k))


    def selectItem(self,midx):
	item = self.tabModel.itemFromIndex(midx)
	if item and hasattr(item,'item_url'):
	    import cPAMIE 
	    ie= cPAMIE.PAMIE()
	    ie.navigate(item.item_url) 
	    #ietd = IeThread()
	    #ietd.setUrl(item.item_url)
	    
	    #ietd.start()
	    #ietd.wait()
	    self.app.processEvents()
	    #QtCore.QCoreApplication.processEvents()
	
	
	
    def queryItems(self):
	""" 查询商品列表"""
	fields = "iid,title,nick,pic_url,price,click_url"
	nick = "mangoers"
	cid = self.ui.cat.itemData(self.ui.cat.currentIndex()).toString()
	keyword = self.ui.keyword.text()
	start_price = self.ui.start_price.value()
	end_price = self.ui.end_price.value()
	auto_send = self.ui.auto_send.isChecked()
	area = self.ui.area.itemData(self.ui.area.currentIndex()).toString()
	start_credit = self.ui.start_credit.itemData(self.ui.start_credit.currentIndex()).toString()
	end_credit = self.ui.end_credit.itemData(self.ui.end_credit.currentIndex()).toString()
	sort = self.ui.sort.itemData(self.ui.sort.currentIndex()).toString()
	is_guarantee = self.ui.is_guarantee.isChecked()
	page_size = self.ui.page_size.text()
	
	if not cid  and not keyword:
	    return None
	
	
	paramArray = {'fields':fields,'nick':nick}
	if cid : paramArray ['cid'] = cid
	if keyword : paramArray ['keyword'] = keyword
	if start_price>0 : paramArray ['start_price'] = str(start_price)
	if end_price>0 : paramArray ['end_price'] = str(end_price)
	if auto_send : paramArray ['auto_send'] = "true"
	if area : paramArray ['area'] = unicode(area)
	if start_credit : paramArray ['start_credit'] = start_credit
	if end_credit : paramArray ['end_credit'] = end_credit
	if sort : paramArray ['sort'] = sort
	if is_guarantee : paramArray ['is_guarantee'] = "true"
	paramArray ['page_no'] = '1'
	if page_size : paramArray ['page_size'] = page_size
	self.fillTable(self.api.taobaoke_items_get(paramArray))
	
	
    def fillTableHeader(self):
	h0 = QtGui.QStandardItem(u"商品")
	h1 = QtGui.QStandardItem(u"价格")
	#h2 = QtGui.QStandardItem(u"快递")
	#h3 = QtGui.QStandardItem(u"总价")
	#h4 = QtGui.QStandardItem(u"售出")
	#h5 = QtGui.QStandardItem(u"信用")
	#h6 = QtGui.QStandardItem(u"好评")
	h7 = QtGui.QStandardItem(u"商家")
	#h8 = QtGui.QStandardItem(u"区域")
	
	self.tabModel.setHorizontalHeaderItem(0,h0)
	self.tabModel.setHorizontalHeaderItem(1,h1)
	#self.tabModel.setHorizontalHeaderItem(2,h2)
	#self.tabModel.setHorizontalHeaderItem(3,h3)
	#self.tabModel.setHorizontalHeaderItem(4,h4)
	#self.tabModel.setHorizontalHeaderItem(5,h5)
	#self.tabModel.setHorizontalHeaderItem(6,h6)
	self.tabModel.setHorizontalHeaderItem(2,h7)
	#self.tabModel.setHorizontalHeaderItem(8,h8)
	
	self.currentTitleWidth = self.window.width()-300
	h0.setSizeHint(QtCore.QSize(self.currentTitleWidth,20))#商品列动态长度
	h1.setSizeHint(QtCore.QSize(80,20))
	#h2.setSizeHint(QtCore.QSize(50,20))
	#h3.setSizeHint(QtCore.QSize(50,20))
	#h4.setSizeHint(QtCore.QSize(50,20))
	#h5.setSizeHint(QtCore.QSize(50,20))
	#h6.setSizeHint(QtCore.QSize(50,20))
	h7.setSizeHint(QtCore.QSize(120,20))
	#h8.setSizeHint(QtCore.QSize(60,20))
    
    def fillTable(self,tdata):
	
	self.tabModel.clear()

	self.fillTableHeader()
	
	if tdata is None:
	    return
	
        #[u"商品名",u"价格",u"快递",u"总价",u"售出",u"商家信用",u"好评",u"商家",u"所在地"]
	for data in tdata:
	    c1 =  QtGui.QStandardItem(data['title'])
	    c2 =  QtGui.QStandardItem(data['price'])
	    #c3 =  QtGui.QStandardItem("")
	    #c4 =  QtGui.QStandardItem("")
	    #c5 =  QtGui.QStandardItem("")
	    #c6 =  QtGui.QStandardItem("")
	    #c7 =  QtGui.QStandardItem("")
	    c8 =  QtGui.QStandardItem(data['nick'])
	    #c9 =  QtGui.QStandardItem("")
	    c1.setToolTip(data['title'])

	    c1.setForeground(QtCore.Qt.blue)
	    
	    font = QtGui.QFont()
	    font.setUnderline(True)
	    c1.setFont(font)
	    c1.setSizeHint(QtCore.QSize(self.currentTitleWidth,20))#商品列动态长度
	    c1.item_url = data['click_url']
	    
	    self.cs = [c1,c2,c8]
	    for c in self.cs:
		c.setEditable(False)

	    
	    self.tabModel.appendRow(self.cs)

	self.ui.data_view.resizeColumnsToContents()
	

	
    def _getValue(data,key,dvalue):
	if not data:
	    return ""

########################################################################
class IeThread(QtCore.QThread):
    def setUrl(self,url):
        self.url = url
	
    def run(self):
	#exe = QtCore.QProcess()
	#QtCore.QProcess.execute("C:\\Program Files\\Internet Explorer\\iexplore.exe",("-new",self.url)) 
	#exe.waitForFinished()
	import cPAMIE 
	ie= cPAMIE.PAMIE()
	ie.Navigate (self.url) 
	    
  
if __name__ == "__main__":
    taotao = Taotao()
    
    
    
    
    
    