from flask_restful import Resource

from flask_jwt import jwt_required
from models.wine import WineModel


class QualityCountPlot(Resource):
    @jwt_required()
    def get(self):
        list_data = []
        list_data2 = []
        # dict_data = {}
        data = WineModel.qualityCountPlot()
        for variable in data:
            list_data += [variable[0]]
        categories = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for category in categories:
            list_data2 += [list_data.count(category)]

        return {"data": list_data2}

        # return {"quality": list_data}


# class AlcoholHistogram(Resource):
#     @jwt_required()
#     def get(self):
#         list_data = []
#         data = WineModel.alcoholHistogramPlot()
#         for variable in data:
#             list_data += [variable[0]]
#         return {"alcohol": list_data}


class SulphurScatter(Resource):
    @jwt_required()
    def get(self):
        list_data = []
        data = WineModel.tsdvsfsdScatterPlot()
        for variable in data:
            list_data += [[variable[0], variable[1]]]
        return {"sulphur": list_data}


class densityPhScatter(Resource):
    @jwt_required()
    def get(self):
        list_data = []
        data = WineModel.densityvsphScatterPlot()
        for variable in data:
            list_data += [[variable[0], variable[1]]]
        return {"density&ph": list_data}


class LabelCountPlot(Resource):
    @jwt_required()
    def get(self):
        list_data = []
        list_data2 = []
        # dict_data = {}
        data = WineModel.labelcountplot()
        for variable in data:
            list_data += [variable[0]]
        categories = ["bad", "good", "very good"]
        for category in categories:
            list_data2 += [list_data.count(category)]

        return {"data": list_data2}
