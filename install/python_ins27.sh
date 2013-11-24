#!/bin/sh

#define variable
Tools_Dir="/usr/local/src"
Python_Dir="/usr/local/python"
Log_File="/tmp/tri_install.log"
Err_Log="/tmp/tri_install_err.log"

install_python(){
    printf "Install Python,Please wait...\n"
    #judge 
    [ -d $Python_Dir ] || mkdir $Python_Dir -p
    #install python2.7 must update python-devel
    yum install python-devel* >>$Log_File 2>&1 
    #install python
    cd $Tools_Dir
    wget http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tgz >>$Log_File 2>&1
    tar zxf Python-2.7.5.tgz >>$Log_File 2>&1
    cd Python-2.7.5
    ./configure --enable-shared --prefix=$Python_Dir >>$Log_File 2>&1
    [ $? -ne 0 ] && tail -30 $Log_File |tee -a $Err_Log && exit 1;
    make >>$Log_File 2>&1
    [ $? -ne 0 ] && tail -30 $Log_File |tee -a $Err_Log && exit 1;
    make install >>$Log_File 2>&1
    [ $? -ne 0 ] && tail -30 $Log_File |tee -a $Err_Log && exit 1;
    ln -s $Python_Dir /usr/local/python
    rename python python2.6_bak /usr/bin/python
    ln -s /usr/local/python/bin/python /usr/bin/python
    ln -s /usr/local/python/lib/libpython2.7.so /usr/lib
    #modifiy yum command content
    sed -i 's@^#!/usr/bin/python$@#!/usr/bin/python2.6@g' /usr/bin/yum
    #load python2.7 lib
    echo "$Python_Dir/lib/" > /etc/ld.so.conf.d/python2.7.conf
    ldconfig
    printf "Install Python Success\n"
}

install_python
