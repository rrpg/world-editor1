# -*- coding: utf-8 -*-
import os

rootPath = os.path.dirname(__file__) + '/..'
externalPath = rootPath + '/externals'
exportPath = os.path.expanduser('~') + '/.rrpg/maps'
databasePath = externalPath + '/engine/database'
databaseStructure = databasePath + '/structure.sql'

defaultMap =  exportPath + '/default.db'

map_default_width = 400
map_default_height = 400
map_minimum_width = 10
map_minimum_height = 10
map_maximum_width = 10000
map_maximum_height = 10000

tempDir = rootPath + '/tmp'
localesDir = rootPath + '/locales'

generator = {}
generator['map'] = {
	'path': externalPath + '/map-generator',
	'generator': externalPath + '/map-generator/map -t -f %s -w %d -h %d'
}

db = exportPath + '/%s.db'

colors = {}
colors['selected-cell'] = [None, (0, 0, 0)]
colors['start-cell'] = [(0, 0, 0), (0, 0, 0)]
colors['places'] = [(127, 127, 127), (127, 127, 127)]
colors['npc'] = [(127, 127, 127), (127, 127, 127)]

scaleFactor = 30.0
zoomDelta = .25
