import textwrap,Termina_size

HeadLine='''\033[32;1m
+=============================================================================================================================+
|															      |
|						TriAquae Auditing Console			     			      |
|                                                    Version: 3.0.1    	                                                      |
|                                                                                                                             |
|    Welcome using TriAquae auditing system.                                                                                  |  
|											Report bug: Triaquae@gmail.com        |
|_____________________________________________________________________________________________________________________________|
\033[0m'''

HeadLine100 = '''\033[32;1m
+==============================================================================================+
|											       |
|				 TriAquae Auditing Console                                     |
|				 	Version: 3.0.1                                         |
|											       |
|    Welcome using TriAquae auditing system.                                                   | 
|                                                               Report bug: Triaquae@gmail.com |
|______________________________________________________________________________________________|
\033[0m'''

HeadLine80 =  '''\033[32;1m
+==============================================================================+
|                                                                              |
|                            TriConn Auditing Console                          |
|                            	Version: 3.0.1                                 |
|                                                                              |
|    Welcome using TriAquae auditing system.                                   |  
|							         	       |
|                                              Report bug: Triaquae@gmail.com  |
|______________________________________________________________________________|
\033[0m'''

def head_line():
	T_size = Termina_size.terminal_size()
	if T_size[0] >= 127:
		print HeadLine
	elif T_size[0] >= 100:
		print HeadLine100 
	else: 
		print HeadLine80
		#print T_size

head_line()


