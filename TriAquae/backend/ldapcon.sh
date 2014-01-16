#!/bin/sh
ldapsearch -LLL -W -x -H ldap://coral.org -D "cn=admin,dc=coral,dc=org" -b "dc=coral,dc=org"
