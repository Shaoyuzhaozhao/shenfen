#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
udp通信例程：udp client端，修改udp_addr元组里面的ip地址，即可实现与目标机器的通信，
此处以单机通信示例，ip为127.0.0.1，实际多机通信，此处应设置为目标服务端ip地址
"""
 
from time import sleep
import socket
 
def main():
    # udp 通信地址，IP+端口号
    udp_addr = ('127.0.0.1', 9999)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    data = bytes.fromhex("AA 55 06 01 00 05")
    # 发送数据到指定的ip和端口,每隔1s发送一次，发送10次
    for i in range(10):
        udp_socket.sendto(data, udp_addr)
        print("send %d message" % i)
        sleep(1)
 
    # 5. 关闭套接字
    udp_socket.close()
 


def send(data):
    # udp 通信地址，IP+端口号
    udp_addr = ('127.0.0.1', 9999)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
    # 发送数据到指定的ip和端口,每隔1s发送一次，发送10次
    
    udp_socket.sendto(data, udp_addr)
    print("send message:"+ str(data))
 
    # 5. 关闭套接字
    udp_socket.close()
 
if __name__ == '__main__':
    # print("当前版本： ", __version__)
    print("udp client ")
    main()