from functools import partial
from time import time
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.data_read.model import DataRead
from app.data_read.schemas import DataReadSchema
from app.utils.filters import filters

import datetime 

class OneDayGraph(MethodView):

    #decorators = [jwt_required()]

    def get(self,number_of_days_before):
        data_reads = DataRead.query.filter_by(sensor_id = 1).order_by("create_time").all()
        
        if not data_reads:
            return {"error" : "No read on storage"},400
        
        today = datetime.date.today().isocalendar()
        year = today[0]
        today_index = (today[1]*7 + today[2])
        day_index = today_index - number_of_days_before  
        print(day_index)
        value_list = []
        time_list = []

        for i in range (len(data_reads) - 1, -1, -1): 
            if data_reads[i].create_time.isocalendar()[0] == year:     
                temp_day_index = data_reads[i].create_time.isocalendar()[1]*7+data_reads[i].create_time.isocalendar()[2]
                print(temp_day_index)
                if day_index == temp_day_index:
                    value_list.append(data_reads[i].uv)
                    time_list.append(data_reads[i].create_time)
                else:
                    i = 0

        return {"value_list" : value_list, "time_list":time_list}, 200




class ManyDaysGraph(MethodView):

    #decorators = [jwt_required()]

    def get(self,number_of_days_before):
        data_reads = DataRead.query.filter_by(sensor_id = 1).order_by("create_time").all()
        
        if not data_reads:
            return {"error" : "No read on storage"},400
        
        today = datetime.date.today().isocalendar()
        year = today[0]
        today_index = (today[1]*7 + today[2])
        limit_day_index = today_index - number_of_days_before  
        print(limit_day_index)
        value_list = []
        time_list = []

        for i in range (len(data_reads) - 1, -1, -1): 
            if data_reads[i].create_time.isocalendar()[0] == year:     
                temp_day_index = data_reads[i].create_time.isocalendar()[1]*7+data_reads[i].create_time.isocalendar()[2]
                print(temp_day_index)
                if temp_day_index >= limit_day_index:
                    value_list.append(data_reads[i].uv)
                    time_list.append(data_reads[i].create_time)
                else:
                    i = 0

        return {"value_list" : value_list, "time_list":time_list}, 200