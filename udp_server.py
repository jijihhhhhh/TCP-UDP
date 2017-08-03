
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, threading, time

# 创建端口 (SOCK_DGRAM指定端口为UDP)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:
	# 接受数据
	data, addr = s.recvfrom(1024) # 返回数据和客户端地址和端口
	print('Received from %s:%s.' % addr)
	s.sendto(b'Hello, %s!' % data, addr)
