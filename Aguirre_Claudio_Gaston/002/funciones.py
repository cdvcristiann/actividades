# -*- coding: utf-8 -*-
#Realizar un funci�n que reciba como par�metro una cantidad de segundos, y devuelva una tupla con la cantidad de segundos expresada en hh,mm,ss.

def conversor_horario(segundos):
	horas=segundos//3600
	minutos=(segundos%3600)//60
	segundos=(segundos%3600)%60
	return (horas, minutos, segundos)
	
#Realizar una funci�n que reciba como par�metros cantidades de horas, minutos y/o segundos. Y que retorne la suma de estos expresanda en segundos. (Los par�metros, son opcionales y por defecto sus valores 0.)
	
def conversor_segundos(horas=0, minutos=0, segundos=0):
	segundos=(horas*3600)+(minutos*60)+segundos
	return segundos


