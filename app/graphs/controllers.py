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
        value_list = []
        time_list = []

        for i in range (len(data_reads) - 1, -1, -1): 
            if data_reads[i].create_time.isocalendar()[0] == year:     
                temp_day = data_reads[i].create_time.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)     
                temp_day_index = temp_day.isocalendar()[1]*7+temp_day.isocalendar()[2]
                print(temp_day_index)
                if day_index == temp_day_index:
                    value_list.append(data_reads[i].uv)
                    time_list.append(temp_day)
                else:
                    i = -1

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
        value_list = []
        time_list = []

        for i in range (len(data_reads) - 1, -1, -1): 
            if data_reads[i].create_time.isocalendar()[0] == year:
                temp_day = data_reads[i].create_time.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)     
                temp_day_index = temp_day.isocalendar()[1]*7+temp_day.isocalendar()[2]
                if temp_day_index >= limit_day_index:
                    value_list.append(data_reads[i].uv)
                    time_list.append(temp_day)
                else:
                    i = -1
        print(time_list)
        return {"value_list" : value_list, "time_list":time_list}, 200




class MaxUvByDayGraph(MethodView):

    #decorators = [jwt_required()]

    def get(self,number_of_days_before):
        data_reads = DataRead.query.filter_by(sensor_id = 1).order_by("create_time").all()
        if not data_reads:
            return {"error" : "No read on storage"},400
        
        today = datetime.date.today().isocalendar()
        year = today[0]
        today_index = (today[1]*7 + today[2])
        limit_day_index = today_index - number_of_days_before  
        value_list = []
        time_list = []
        uv_max = 0
        changed_index = False
        last_item = data_reads[len(data_reads) - 1].create_time.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
        day_index_now = last_item.isocalendar()[1]*7+last_item.isocalendar()[2]

        for i in range (len(data_reads) - 1, -1, -1): 
            if data_reads[i].create_time.isocalendar()[0] == year:
                temp_day = data_reads[i].create_time.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)     
                temp_day_index = temp_day.isocalendar()[1]*7+temp_day.isocalendar()[2]
                    
                if temp_day_index >= limit_day_index:
                    if temp_day_index != day_index_now:
                        print("Entrei aqui --------- 0")
                        print(uv_max)
                        print(temp_day_index)
                        print(i)
                        print(day_index_now)
                        print(changed_index)
                        changed_index = True
                        day_index_now = temp_day_index

                    uv_now = data_reads[i].uv

                    if changed_index == True :
                        print("Entrei aqui --------- 1")
                        print(uv_max)
                        print(temp_day_index)
                        print(i)
                        print(day_index_now)
                        print(changed_index)
                        value_list.append(uv_max)
                        time_list.append(uv_max_datetime)
                        uv_max = uv_now
                        uv_max_datetime = temp_day
                        changed_index = False

                    if uv_now > uv_max:
                        print("Entrei aqui --------- 2")
                        print(uv_max)
                        print(temp_day_index)
                        print(i)
                        print(day_index_now)
                        print(changed_index)
                        uv_max = uv_now
                        uv_max_datetime = temp_day
                        


                    if(i == 0):
                        print("Entrei aqui --------- 3")
                        print(uv_max)
                        print(temp_day_index)
                        print(i)
                        print(day_index_now)
                        print(changed_index)
                        value_list.append(uv_now)
                        time_list.append(temp_day)                    

                else:
                    print("Entrei aqui --------- 4")
                    print(uv_max)
                    print(temp_day_index)
                    print(i)
                    print(day_index_now)
                    print(changed_index)
                    value_list.append(uv_max)
                    time_list.append(uv_max_datetime)
                    break

        return {"value_list" : value_list, "time_list":time_list}, 200