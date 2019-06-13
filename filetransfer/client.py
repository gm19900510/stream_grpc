#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
from filetransfer import filetransfer_pb2, filetransfer_pb2_grpc
import numpy as np
import cv2
import datetime

_HOST = '192.168.3.56'
_PORT = '8883'

def run():
    start = datetime.datetime.now()
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = filetransfer_pb2_grpc.FileTransferServiceStub(channel=conn)
    response = client.ServerSideStreamFun(filetransfer_pb2.RequestData(text='服务启动'))
    for obj in response:
        print("received: ",obj.deviceId)
        print("received: ",obj.requestId)
        # with open(obj.requestId+'.jpg', 'wb') as f:
        #    f.write(obj.fileData)
        image = np.asarray(bytearray(obj.fileData), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
    end = datetime.datetime.now()
    print('--------------->', (end - start)) 

if __name__ == '__main__':
    run()