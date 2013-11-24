#!/bin/sh

#define variable
Log_File="/tmp/tri_install.log"
Err_Log="/tmp/tri_install_err.log"


install_setuptool(){
    tar zxf setuptools-0.6c10.tar.gz >>$Log_File 2>&1
    cd setuptools-0.6c10/
    python setup.py install >>$Log_File 2>&1
    [ $? -ne 0 ] && tail -30 $Log_File |tee -a $Err_Log && exit 1;
    cd ../
    rm -rf setuptools-0.6c10/
}

install_mysqldb(){
    tar zxf MySQL-python-1.2.3.tar.gz >>$Log_File 2>&1
    cd MySQL-python-1.2.3/
    python setup.py build >>$Log_File 2>&1
    [ $? -ne 0 ] && tail -30 $Log_File |tee -a $Err_Log && exit 1;
    python setup.py >>$Log_File 2>&1
    [ $? -ne 0 ] && tail -30 $Log_File |tee -a $Err_Log && exit 1;
    cd ../
    rm -rf MySQL-python-1.2.3/
}

install_setuptool
install_mysqldb
