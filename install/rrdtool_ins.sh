#!/bin/bash

#define variable
Rrdtool_Dir=$1
Log_File="/tmp/tri_install.log"
Err_Log="/tmp/tri_install_err.log"

install_rrdtool(){
    #install rpm packet
    yum install cairo-devel libxml2-devel pango-devel pango libpng-devel freetype freetype-devel libart_lgpl libart_lgpl-devel intltool -y >>$Log_File 2>&1
    
    tar zxf rrdtool-1.4.7.tar.gz  >>$Log_File 2>&1
    cd rrdtool-1.4.7
    ./configure --prefix=$Rrdtool_Dir >>$Log_File 2>&1
    [ $? -ne 0 ] && tail -30 $Log_File |tee -a $Err_Log && exit 1;
    make >>$Log_File 2>&1
    [ $? -ne 0 ] && tail -30 $Log_File |tee -a $Err_Log && exit 1;
    make install >>$Log_File 2>&1
    [ $? -ne 0 ] && tail -30 $Log_File |tee -a $Err_Log && exit 1;

    #rename
    [ -f /usr/bin/rrdtool ] && rename rrdtool rrdtool-1.2_bak /usr/bin/rrdtool;
    #ln -s /usr/local/rrdtool/bin/rrdtool /usr/bin/rrdtool  
    /bin/cp $Rrdtool_Dir/bin/rrdtool /usr/bin/rrdtool  
    cd ../
    rm -rf rrdtool-1.4.7
}

install_rrdtool
