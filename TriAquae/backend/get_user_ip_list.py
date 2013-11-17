#!/usr/bin/env python
#Author: Alex Li
import db_connector

user_list = db_connector.TriaquaeUser.objects.all()

can_access_dic = {} 
for u in user_list:
	can_access_dic[u.email] = []
	for i in u.ip.all():
		can_access_dic[u.email].append( i.ip )
	for g in u.group.all():
		 for i in g.ip_set.all():
			can_access_dic[u.email].append(i.ip)

