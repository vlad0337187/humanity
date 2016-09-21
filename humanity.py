#! /usr/bin/env python3
''' 
('RU') Данный модуль заменяет стандартные типы данных последовательностей (списки, кортежи, строки) аналогичными типами данных,
в которых индексация идет не с нуля а с единицы. Пример: a = humlist(1,2,3); print(a[2]) выведет 2.

Содержит типы данных: 
	humlist (аналог списков), humtuple (аналог кортежей), humstr (аналог строк)
Содержит функции:
	humrange (аналог range)

Подключение модуля: 
1) Добавим в sys.path расположение каталога (папки) с данным модулем. 
	Пример 1 (простой):
		import sys
		sys.path.append('/home/user/modules')
	Пример 2 (с относительными путями): 
		import os, sys, inspect
		# realpath() will make your script run, even if you symlink it :)
		cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
		if cmd_folder not in sys.path:
		sys.path.insert(0, cmd_folder)
	Пример 3 (с относительными путями):
		# use this if you want to include modules from a subfolder
		cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
		if cmd_subfolder not in sys.path:
		sys.path.insert(0, cmd_subfolder)
  Можно не добавлять если данный модуль находится в домашнем каталоге (папке). В некоторых ОС домашний каталог это тот, в котором
  расположен файл с выполняемой программой.
2) Импортируем его: from humanity import *
  или: import humanity


('EN') This module replaces the standard sequence data types (lists, tuples, strings) similar types of data,
in which indexation is not from zero but from one. Example: a = humlist(1,2,3); print(a[2]) will print 2.

Contains data types: 
	humlist (similar to lists), humtuple (similar to tuples), humstr (analogue lines)
Contains functions:
	humrange (analogue range)

Importing module: 
1) Add to sys.path to a directory (folder) with this module. 
	Example 1 (simple):
		import sys
		sys.path.append('/home/user/modules')
	Example 2 (with relative paths): 
		import os, sys, inspect
		# realpath() will make your script run, even if you symlink it :)
		cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
		if cmd_folder not in sys.path:
		sys.path.insert(0, cmd_folder)
	Example 3 (with relative paths):
		# use this if you want to include modules from a subfolder
		cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
		if cmd_subfolder not in sys.path:
		sys.path.insert(0, cmd_subfolder)
		You can not add if the module is in the home directory (folder). In some operating systems the home directory is the one in which
		is a file with the executable program.
2) Import: import from humanity *
or: import humanity

Version: 2.3
'''




def changeIndexes(keys):
	'''('RU') Функция используется в: __getitem__, __setitem__, __delitem__.
	Она смещает в последовательностях номер первого элемента с [0] на [1].
	если в функц. передается один аргумент, он int и пишется в keys
	если пытаешься брать срез, keys присваивается объект среза вида: slice(1, None, None)'''
	''' В других методах не используется, так как там нету объектов среза: slice(1, None, None), там можно просто отнять 1 от индекса или добавить
	
	version: 1.1
	'''
	if isinstance(keys, slice):
		keys = str(keys) # isinstance(n,int) не помогает
		keys = keys.replace('slice(', '').replace(')', '')
		keys = keys.split(', ')
		if keys[0] != 'None':
			keys[0] = int(keys[0]) - 1
		elif keys[0] == 'None':
			keys[0] = None
		if keys[1] != 'None':
			keys[1] = int(keys[1])
		elif keys[1] == 'None':
			keys[1] = None
		if keys[2] != 'None':# это шаг
			keys[2] = int(keys[2])
		elif keys[2] == 'None':
			keys[2] = None
		keys = slice(keys[0], keys[1], keys[2]) # потому что должна быть последовательность с одним элементом
	elif isinstance(keys, int): #если нет 'slice(', значит целое число
		if keys > 0:
			keys = keys - 1
		elif keys == 0:
			raise IndexError('There is no element under index 0')
		elif keys < 0:
			pass	
	return keys




def getitem():
	pass
	
	


class humlist(list):
	'''Class, that is the same to list type, but with normal indexes.
	version: 2
	'''

	# Технические методы:
	
	def __init__(self, *something):
		'''('EN') humlist(1,2) will create [1, 2], humlist([1,2]) will create [1, 2], humlist((1,2), (2,3)) will create [(1, 2), (2, 3)] 
		('RU') Подобные есть и в humtuple и в humstr, только называется __new__.'''
		try: something[1]; something[0] # если два и более аргумента - else:
		except IndexError: # если нет двух и более:
			try: something[0] # если только один аргумент - else:
			except IndexError: # если ни одного аргумента
				list.__init__(self, something)
			else: # если только один аргумент
				something = something[0]
				list.__init__(self, something)
		else: # если два и более аргумента
			list.__init__(self, something) # возвращать ничего не нужно (для базового класса так)
			
	def __getitem__(self, keys):
		'''('EN') x.__getitem__(y) <==> x[y]. If A = [1,2,3], than A[1] will give 1'''
		keys = changeIndexes(keys)
		return list.__getitem__(self, keys)
		
	def __setitem__(self, keys, value):
		'''('EN') Set self[key] to value. If A = [1,2,3], than A[1] = 5 will change A so: [5,2,3]'''
		keys = changeIndexes(keys)
		list.__setitem__(self, keys, value)#второй аргумент просит итерируемый объект вида: (slice(1,2,1), ) или (1, )
		
	def __delitem__(self, keys):
		'''('EN') Delete self[key]. If A = [1,2,3], than A[1] = 5 will change A so: [5,2,3]''' 
		keys = changeIndexes(keys)
		list.__delitem__(self, keys)
		
	# Нетехнические методы:
	
	def insert(self, position, value):
		position = changeIndexes(position)
		list.insert(self, position, value)
		
	def index(self, value, *positions):
		try: # если есть лишние позиции, распакуем их все в оригинальный метод, чтобы получить оригинальную ошибку
			positions[0]; positions[1]; positions[2]
		except IndexError: pass
		else: return list.index(self, value, *positions)
		
		try: # если есть и стартовая, и конечная позиция
			positions[0]; positions[1]
		except IndexError: pass
		else: 
			start = positions[0] - 1
			end = positions[1]
			return list.index(self, value, start, end) + 1
			
		try: # если есть только стартовая позиция - переходим к else
			positions[0]
		except IndexError: # если позиции не были переданы вообще:
			return list.index(self, value) + 1
		else: # если есть только стартовая позиция
			start = positions[0] - 1
			return list.index(self, value, start) + 1
		# копия метода есть в классах humtuple, humstr
		
	def get(self, position):
		'''Returns value of element on position. If such element is absent - returns None.
		'''
		try:
			value = self.__getitem__(self, position)
		except IndexError:
			value = None
		return None




class humtuple(tuple):
	'''Class, that is the same to tuple type, but with normal indexes.
	version: 2
	'''
	
	# Технические методы:
	
	#def __init__(self, something):
		#У кортежей нет этого метода. Вместо него - __new__. Если добавить __init__ - будут работать оба.
		
	def __new__(self, *something): #только init не канает. Походу он вообще тут не работает.
		'''('EN') Analog to __init__ method in humlist class
		('RU') Но они не одинаковы - у каждого свои нюансы.'''
		try: something[1]; something[0] # если два и более аргумента - else:
		except IndexError: # если нет двух и более:
			try: something[0] # если только один аргумент - else:
			except IndexError: # если ни одного аргумента
				return tuple.__new__(self, something)
			else: # если только один аргумент
				something = something[0]
				return tuple.__new__(self, something)
		else: # если два и более аргумента
			return tuple.__new__(self, something) # возвращать ничего не нужно (для базового класса так)
			
	def __getitem__(self, keys):
		'''('EN') Analog to similar method in humlist class'''
		keys = changeIndexes(keys)
		return tuple.__getitem__(self, keys)
		
	def __setitem__(self, keys, value):
		'''('EN') Analog to similar method in humlist class'''
		keys = changeIndexes(keys)
		return tuple.__setitem__(self, keys, value)#второй аргумент просит итерируемый объект вида: (slice(1,2,1), ) или (1, )
		
	def __delitem__(self, keys):
		'''('EN') Analog to similar method in humlist class'''
		keys = changeIndexes(keys)
		return tuple.__delitem__(self, keys)
		
	# Нетехнические методы:
	
	def index(self, value, *positions):
		try: # если есть лишние позиции, распакуем их все в оригинальный метод, чтобы получить оригинальную ошибку
			positions[0]; positions[1]; positions[2]
		except IndexError: pass
		else: return tuple.index(self, value, *positions)
		
		try: # если есть и стартовая, и конечная позиция
			positions[0]; positions[1]
		except IndexError: pass
		else: 
			start = positions[0] - 1
			end = positions[1]
			return tuple.index(self, value, start, end) + 1
			
		try: # если есть только стартовая позиция - переходим к else
			positions[0]
		except IndexError: # если позиции не были переданы вообще:
			return tuple.index(self, value) + 1
		else: # если есть только стартовая позиция
			start = positions[0] - 1
			return tuple.index(self, value, start) + 1
		# копия метода есть в классах humlist, humstr
		
	def get(self, position):
		'''Returns value of element on position. If such element is absent - returns None.
		'''
		try:
			value = self.__getitem__(self, position)
		except IndexError:
			value = None
		return None




class humstr(str):
	'''Class, that is the same to string type, but with normal indexes.
	version: 2
	'''
	
	# Технические методы:
	
	#def __init__(self, something):
		#У кортежей нет этого метода. Вместо него - __new__. Если добавить __init__ - будут работать оба.
	
	def __new__(self, *something): #только init не канает. Походу он вообще тут не работает.
		'''('EN') Analog to __init__ method in humlist class
		('RU') Но они не одинаковы - у каждого свои нюансы.'''
		try: something[1]; something[0] # если два и более аргумента - else:
		except IndexError: # если нет двух и более:
			try: something[0] # если только один аргумент - else:
			except IndexError: # если ни одного аргумента
				return str.__new__(self)
			else: # если только один аргумент
				something = something[0]
				return str.__new__(self, something)
		else: # если два и более аргумента
			return str.__new__(self, something) # возвращать ничего не нужно (для базового класса так)
	
	def __getitem__(self, keys):
		'''('EN') Analog to similar method in humlist class'''
		keys = changeIndexes(keys)
		return str.__getitem__(self, keys)
	
	def __setitem__(self, keys, value):
		'''('EN') Analog to similar method in humlist class'''
		keys = changeIndexes(keys)
		return str.__setitem__(self, keys, value)#второй аргумент просит итерируемый объект вида: (slice(1,2,1), ) или (1, )
	
	def __delitem__(self, keys):
		'''('EN') Analog to similar method in humlist class'''
		keys = changeIndexes(keys)
		return str.__delitem__(self, keys)
	
	# Нетехнические методы:
	
	def find(self, value):
		return str.find(self, value) + 1
	# def rfind и так возвращает правильное значение
	
	def index(self, value, *positions):
		try: # если есть лишние позиции, распакуем их все в оригинальный метод, чтобы получить оригинальную ошибку
			positions[0]; positions[1]; positions[2]
		except IndexError: pass
		else: return str.index(self, value, *positions)
		
		try: # если есть и стартовая, и конечная позиция
			positions[0]; positions[1]
		except IndexError: pass
		else: 
			start = positions[0] - 1
			end = positions[1]
			return str.index(self, value, start, end) + 1
		
		try: # если есть только стартовая позиция - переходим к else
			positions[0]
		except IndexError: # если позиции не были переданы вообще:
			return str.index(self, value) + 1
		else: # если есть только стартовая позиция
			start = positions[0] - 1
			return str.index(self, value, start) + 1
		# копия метода есть в классах humlist, humtuple
	
	def rindex(self, value, *positions):
		try: # если есть лишние позиции, распакуем их все в оригинальный метод, чтобы получить оригинальную ошибку
			positions[0]; positions[1]; positions[2]
		except IndexError: pass
		else: return str.rindex(self, value, *positions)
		
		try: # если есть и стартовая, и конечная позиция
			positions[0]; positions[1]
		except IndexError: pass
		else: 
			start = positions[0] - 1
			end = positions[1]
			return str.rindex(self, value, start, end) + 1
		
		try: # если есть только стартовая позиция - переходим к else
			positions[0]
		except IndexError: # если позиции не были переданы вообще:
			return str.rindex(self, value) + 1
		else: # если есть только стартовая позиция
			start = positions[0] - 1
			return str.rindex(self, value, start) + 1
		# метод основан на методе index, копии которого есть в классах humlist, humtuple, humstr
		
	def get(self, position):
		'''Returns value of element on position. If such element is absent - returns None.
		'''
		try:
			value = self.__getitem__(self, position)
		except IndexError:
			value = None
		return None




def humrange(*n):
	'''Function, that is the same to range() function, but with normal indexes.
	list(humrange(3)) == [1,2,3]; list(humrange(2, 3)) == [2,3]; list(humrange(10, 8, -1)) == [10, 9, 8]
	version: 1
	'''
	try: n[3] # если больше трех аргументов
	except IndexError: pass
	else: return range(*n)
	
	try: n[2] # если три аргумента
	except IndexError: pass
	else: 
		if n[0] < n[1]:
			return range(n[0], n[1] + 1, n[2]) # + и - дают включительность
		elif n[0] > n[1]:
			return range(n[0], n[1] - 1, n[2])
		#elif n[0] == n[1] and n[2] == -1:
		#	return range(n[0], n[1] - 2, n[2])
	
	try: n[1] # если два аргумента
	except IndexError: pass
	else: return range(n[0], n[1] + 1)
	
	try: n[0] # если один аргумент - else
	except IndexError: range() # если ничего не передано
	else: return range(1, n[0] + 1) # если один аргумент
