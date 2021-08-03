from flask import jsonify,request,make_response
from app.api import bp
from app.model import Product, db
from app.api.error import errormessage,successmessage
from datetime import date,datetime
from flask_restful import reqparse
from sqlalchemy.sql import and_


def __init__(self):
    self.parser = reqparse.RequestParser()
    self.parser.add_argument('position', type=str)
# 获得product信息
@bp.route('/product',methods=['GET'])
def getproduct():
    position= request.args.get('position')
    # print(position)
    filter_status = Product.id > 0
    if position is not None:
        filter_status = and_(filter_status,Product.position == position)
    findproductinfo = Product.query.filter(filter_status)
    total = Product.query.filter(filter_status).count()
    messagelist = []
    for x in findproductinfo:
        firsttime2 = datetime.strftime(x.firsttime,'%Y-%m-%d')
        newtime2 = datetime.strftime(x.newtime,'%Y-%m-%d')
        xmessage ={
            'id':x.id,
            "productname":x.productname,
            "position":x.position,
            "rank":x.rank,
            "company":x.company,
            "type":x.type,
            "firsttime":firsttime2,
            "newtime":newtime2,
            "downcount":x.downcount,
            "info":x.info,
            "gzh":x.gzh,
            "xcx":x.xcx,
            "cloudfirm":x.cloudfirm,
            "tencent":x.tencent
        }
        # print(xmessage)
        messagelist.append(xmessage)
    message = {
        "total":total,
        "data":messagelist
    }
    return jsonify(message)

# 增加product信息
@bp.route('/product',methods=['POST'])
def addproduct():
    params = request.get_json()
    # print(params)
    try:
        if params["firsttime"] is not None:
            firsttime = params['firsttime']
            firsttime1 = datetime.strptime(firsttime, "%Y-%m-%d")
        if params['newtime'] is not None:
            newtime = params['newtime']
            newtime1 = datetime.strptime(newtime, "%Y-%m-%d")
        newproductinfo = Product(productname=params['productname']
                                 ,position=params['position']
                                 ,rank = params['rank']
                                 ,company=params['company']
                                 ,type=params['type'],
                                 firsttime=firsttime1
                                 ,newtime=newtime1
                                 ,downcount=params['downcount']
                                 ,info=params['info']
                                 ,gzh=params['gzh'],
                                 xcx=params['xcx']
                                 ,cloudfirm=params['cloudfirm'],tencent=params['tencent'])
        # print(newproductinfo)
        # for i in params.keys():
        #     setattr(newproductinfo,i,params[i])
        db.session.add(newproductinfo)

        db.session.commit()
    except:
        db.session.rollback()
        return make_response(errormessage("参数缺失"))
    else:
        return make_response(successmessage("添加成功"))
    finally:
        db.session.close()

# 修改product信息
@bp.route('/product',methods=['PUT'])
def modifyproduct():
    params = request.get_json()
    try:
        id = params['id']
        productname = params['productname']
        position = params['position']
        rank = params ['rank']
        company = params['company']
        type = params['type']
        firsttime = params['firsttime']
        newtime = params['newtime']
        downcount = params['downcount']
        info = params['info']
        gzh = params['gzh']
        xcx = params['xcx']
        cloudfirm = params['cloudfirm']
        tencent = params['tencent']
    except:
        return make_response(errormessage("参数缺失"))
    product = Product.query.get(id)
    if product is None:
        return make_response(errormessage("客户{id}的信息不存在".format(id=id)))
    try:
        product.productname = productname
        product.position = position
        product.rank = rank
        product.company = company
        product.type = type
        product.firsttime = firsttime
        product.newtime = newtime
        product.downcount =downcount
        product.info = info
        product.gzh =gzh
        product.xcx = xcx
        product.cloudfirm = cloudfirm
        product.tencent = tencent
        db.session.commit()
        return make_response(successmessage('修改成功'))
    except:
        db.session.rollback()
        return make_response(errormessage("修改失败"))
# 删除product信息
@bp.route('/product',methods=['DELETE'])
def deleteproduct():
    params = request.get_json()
    # print(params)
    try:
        id = params['id']
    except:
        return make_response(errormessage("参数缺失"))
    if len(str(id)) == 0:
        return make_response(errormessage("请选择要删除的客户信息"))
    product = Product.query.get(id)
    if product is None:
        return make_response(errormessage("客户的信息不存在"))
    else:
        db.session.delete(product)
    db.session.commit()
    db.session.close()
    return make_response(successmessage("删除成功"))

@bp.route('/map',methods=['GET'])
def productmap():
    chinamap =["北京","天津",'上海','重庆','黑龙江','吉林','辽宁','内蒙古','河北','河南','山东','山西','陕西',
               "宁夏",'甘肃','湖南','湖北','江苏','安徽','浙江','福建','江西','四川','贵州','云南','广东','广西',
               '青海','新疆','西藏','海南']
    res = []
    for i in chinamap:
        filter_status = Product.id > 0
        filter_status = and_(filter_status, Product.position == i)
        total = Product.query.filter(filter_status).count()
        res.append({'name':i,"value":total})
    return jsonify(res)
