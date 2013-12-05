import textwrap,Termina_size

HeadLine='''\033[32;1m
+=============================================================================================================================+
|															      |
|						       TriConn				         			      |
|                                             The command line version                                                        |
|                                                                                                                             |
|\tWelcome to log in TriConn console.                                                                                    |    
|												                              |\033[0m
|\t\033[31;1m[1] Remote login server operations.\033[0m                                                                                   |	
|\t\033[31;1m[2] The operation log audit.\033[0m                                                                                          |
\033[32;1m|											Report bug: Triaquae@gmail.com        |
|_____________________________________________________________________________________________________________________________|
\033[0m'''

HeadLine100 = '''\033[32;1m
+==============================================================================================+
|											       |
|					TriConn  					       |
|				 The command line version                                      |
|											       |
|  \tWelcome to log in TriConn console.                                                     |
|											       |\033[0m
|\t\033[31;1m[1] Remote login server operations.\033[0m                                                    |	
|\t\033[31;1m[2] The operation log audit.\033[0m                                                           |
\033[32;1m|                                                    Report bug: Triaquae@gmail.com            |
|                                                                                              |
|______________________________________________________________________________________________|
\033[0m'''

HeadLine80 =  '''\033[32;1m
+==============================================================================+
|                                                                              |
|                                   TriConn                                    |
|                            The command line version                          |
|                                                                              |
|  \tWelcome to log in TriConn console.                                     |    
|							         	       |\033[0m
|\t\033[31;1m[1] Remote login server operations.\033[0m                                    |	
|\t\033[31;1m[2] The operation log audit.\033[0m                                           |
\033[32;1m|                                        Report bug: Triaquae@gmail.com        |
|                                                                              |
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


