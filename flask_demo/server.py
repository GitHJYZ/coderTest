from flask import Flask,request
from flask_restful import Resource,Api
app = Flask(__name__)
api = Api(app)
#类代表哪个接口资源，每个方法，代表对此资源的操作
class TestCaseService(Resource):
# #查询
# @app.route("/testcase",methods = ["get"])
# def get_case():
#     app.logger.warning("get success")
#     app.logger.info("get success")
#     return {"error": 0,"msg":"get success"}
# #新增
# @app.route("/testcase",methods = ["post"])
# def post_case():
#     return {"error": 0,"msg":"post success"}
# #修改
# @app.route("/testcase",methods = ["put"])
# def put_case():
#     return {"error": 0,"msg":"put success"}
# #删除
# @app.route("/testcase",methods = ["delete"])
# def delete_case():
#     return {"error": 0,"msg":"delete success"}
#
# if __name__ == "__main__":
#     app.run(debug = True)
    #查询
    def get(self):
        app.logger.warning("get success")
        app.logger.info("get success")
        return {"error": 0,"msg":"get success"}
    #新增
    def post(self):
        return {"error": 0,"msg":"post success"}
    #修改
    def put(self):
        return {"error": 0,"msg":"put success"}
    #删除
    def delete(self):
        return {"error": 0,"msg":"delete success"}

if __name__ == "__main__":
    # 参数一添加接口服务，参数二指定对应接口服务的路由
    api.add_resource(TestCaseService, "/testcase")
    #把服务app添加到flask中
    app.run(debug = True)
