# -*- coding: utf8 -*-

"""
Module to work with world maps (Generation, edition, save...)
"""
import subprocess
import os
import config
import sqlite3
import sys


class map:
	@staticmethod
	def generate(name, width, height):
		command = config.generator['map']['generator'] % (
			config.generator['map']['destination-dir'] + '/' + name,
			width,
			height
		)
		if not os.path.exists(config.generator['map']['destination-dir']):
			os.makedirs(config.generator['map']['destination-dir'])
		subprocess.call(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	@staticmethod
	def export(name):
		fileName = config.db % (name)
		# Delete the file if it already exist
		if os.path.isfile(fileName):
			os.remove(fileName)

		# Open connection
		db = sqlite3.connect(fileName)

		# Import an external check class from the generator
		sys.path.insert(0, config.generator['map']['path'])
		import checks

		c = db.cursor()

		f = open(config.databaseStructure, 'r')
		sql = f.read()
		c.executescript(sql)
		f.close()

		# Create main region
		# @TODO replace World by a custom world name
		query = "INSERT INTO region (region_name) VALUES ('World')"
		c.execute(query)

		# Create area types
		query = "INSERT INTO area_type (name) VALUES "
		areaTypes = checks.getGroundTypes()
		valuesInsert = list()
		valuesInsert.append("('dungeon')")
		values = list()
		for t in areaTypes:
			valuesInsert.append("(?)")
			values.append(t)
		query = query + ', '.join(valuesInsert)
		c.execute(query, values)

		# Get area types IDs
		query = "SELECT id_area_type, name FROM area_type"
		c.execute(query)
		result = c.fetchall()
		areaTypes = list()
		for r in result:
			areaTypes.append({'id_area_type': r[0], 'name': r[1]})

		# Insert areas
		db.close()
