# -*- coding: UTF-8 -*-
import top.api

req = top.api.TbkItemGetRequest("http://gw.api.tbsandbox.com/router/rest")
req.set_app_info(top.appinfo("24534648", "13d58dc30ba4de9302ede6981ad66911"))

req.fields = "num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
req.q = "女装"
req.cat = "16,18"
req.itemloc = "杭州"
req.sort = "tk_rate_des"
req.is_tmall = False
req.is_overseas = False
req.start_price = 10
req.end_price = 10
req.start_tk_rate = 123
req.end_tk_rate = 123
req.platform = 1
req.page_no = 123
req.page_size = 20
try:
    resp = req.getResponse()
    print(resp)
except Exception, e:
    print(e)