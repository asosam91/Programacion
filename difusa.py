#!/usr/bin/python


def funBool(X,X0):
	membresia =0.0
	if X <= X0:
		menbresia = 0.0
	else:
		membresia =1.0
	return membresia

def funGrado(X,X0,X1):
	membresia = 0.0
	if X <= X0:
		membresia = 0.0
	elif (X>X0) and (X<X1):
		membresia = (X/(X1-X0))-(X0/(X1-X0))
	elif X >= X1:
		membresia = 1.0
	return membresia
def funTriangular(X,X0,X1,X2):
	membresia = 0.0
	if X <= X0:
		membresia = 0.0
	elif (X > X0) and (X <= X1):
		membresia = (X/(X1-X0))-(X0/(X1-X0))
	elif (X > X1) and (X <= X2):
		membresia = (X/(X2-X1))-(X2/(X2-X1))
	elif X > X2:
		membresia = 1.0
	return membresia
def funTrapezoide(X,X0,X1,X2,X3):
	membresia = 0.0
	if X <= X0:
		membresia = 0.0
	elif (X > X0) and (X <= X1):
		membresia = (X/(X1-X0))-(X0/(X1-X0))
	elif (X > X1) and (X <= X2):
		membresia = 1.0
	elif (X > X2) and (X <= X3):
		membresia = (X/(X3-X2))-(X3/(X3-X2))
	elif X > X3:
		membresia = 0.0
	return membresia
