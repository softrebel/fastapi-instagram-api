from fastapi import FastAPI, Body, HTTPException, status
from bson import json_util
import json





class Response():

    @staticmethod
    def get_response(message,data={},status_code=status.HTTP_200_OK):
        response={
            'message':message,
            'status':status_code,
            'data':data

        }
        json_response = json.loads(json_util.dumps(response))
        # json_response =response
        return json_response
    @staticmethod
    def ok(data={},message='successful'):
        return Response.get_response(message,data,status.HTTP_200_OK)
    @staticmethod
    def bad_request(data={},message='bad request'):
        return Response.get_response(message,data,status.HTTP_400_BAD_REQUEST)
    @staticmethod
    def server_error(data={},message='bad request'):
        return Response.get_response(message,data,status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def created(data={},message='Item Created'):
        return Response.get_response(message,data,status.HTTP_201_CREATED)
