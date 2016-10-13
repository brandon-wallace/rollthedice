#!/usr/bin/python
#title			:rolethedice.py
#description	:This will simulate the rolling of two dice cubes.
#date			:20110508
#version		:0.2
#notes			:
#python_version	:2.6.6
#==========================================================================

import random
import os

def clear_screen():
    os.system('clear')

clear_screen()


print '''
      ___           ___           ___       ___ 
     /\  \         /\  \         /\__\     /\__\,
    /::\  \       /::\  \       /:/  /    /:/  /
   /:/\:\  \     /:/\:\  \     /:/  /    /:/  / 
  /::\~\:\  \   /:/  \:\  \   /:/  /    /:/  /  
 /:/\:\ \:\__\ /:/__/ \:\__\ /:/__/    /:/__/   
 \/_|::\/:/  / \:\  \ /:/  / \:\  \    \:\  \   
    |:|::/  /   \:\  /:/  /   \:\  \    \:\  \  
    |:|\/__/     \:\/:/  /     \:\  \    \:\  \ 
    |:|  |        \::/  /       \:\__\    \:\__\,
     \|__|         \/__/         \/__/     \/__/

      ___           ___           ___     
     /\  \         /\__\         /\  \    
     \:\  \       /:/  /        /::\  \   
      \:\  \     /:/__/        /:/\:\  \  
      /::\  \   /::\  \ ___   /::\~\:\  \ 
     /:/\:\__\ /:/\:\  /\__\ /:/\:\ \:\__\,
    /:/  \/__/ \/__\:\/:/  / \:\~\:\ \/__/
   /:/  /           \::/  /   \:\ \:\__\  
   \/__/            /:/  /     \:\ \/__/  
                   /:/  /       \:\__\    
                   \/__/         \/__/    

      ___                       ___           ___     
     /\  \          ___        /\  \         /\  \    
    /::\  \        /\  \      /::\  \       /::\  \   
   /:/\:\  \       \:\  \    /:/\:\  \     /:/\:\  \  
  /:/  \:\__\      /::\__\  /:/  \:\  \   /::\~\:\  \ 
 /:/__/ \:|__|  __/:/\/__/ /:/__/ \:\__\ /:/\:\ \:\__\,
 \:\  \ /:/  / /\/:/  /    \:\  \  \/__/ \:\~\:\ \/__/
  \:\  /:/  /  \::/__/      \:\  \        \:\ \:\__\  
   \:\/:/  /    \:\__\       \:\  \        \:\ \/__/  
    \::/__/      \/__/        \:\__\        \:\__\    
     ~~                        \/__/         \/__/    

Use these virtual dice when you leave your real dice at home.
'''

def rolling():
        raw_input("Press <Enter> to role the dice. <Ctrl-c> to quit.")

	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)

	if d1 == 1:
		print """
		_________
		|        |
		|        |
		|    *   |
		|        |
		|________|\n"""
	
	
	if d1 == 2:
		print """
		_________
		|        |
		| *      |
		|        |
		|      * |
		|________|\n"""


	if d1 == 3:
		print """
		_________
		|        |
		|      * |
		|    *   |
		| *      |
		|________|\n"""
 

	if d1 == 4:
		print """
		_________
		|        |
		| *    * |
		|        |
		| *    * |
		|________|\n"""
	
	
	if d1 == 5:
		print """
		_________
		|        |
		| *    * |
		|    *   |
		| *    * |
		|________|\n"""
	
	
	if d1 == 6:
		print """
		_________
		|        |
		| *  * * |
		|        |
		| *  * * |
		|________|\n"""
	
	
	if d2 == 1:
		print """
		_________
		|        |
		|        |
		|    *   |
		|        |
		|________|\n"""
	
	if d2 == 2:
		print """
		_________
		|        |
		| *      |
		|        |
		|      * |
		|________|\n"""
	
	
	if d2 == 3:
		print """
		_________
		|        |
		|      * |
		|    *   |
		| *      |
		|________|\n"""
	 
	
	if d2 == 4:
		print """
		_________
		|        |
		| *    * |
		|        |
		| *    * |
		|________|\n"""
	
	
	if d2 == 5:
		print """
		_________
		|        |
		| *    * |
		|    *   |
		| *    * |
		|________|\n"""
	
	
	if d2 == 6:
		print """
		_________
		|        |
		| *  * * |
		|        |
		| *  * * |
		|________|\n"""
		
	if d1 == d2 and d1 != 1:
		print "\nYou're lucky.\n"

	if d1 == 1 and d2 == 1:
		print "SNAKE EYES!!!! You Lose!\n"

rolling()
