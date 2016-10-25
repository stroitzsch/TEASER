# -*- coding: utf-8 -*-

from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.gui.controller.controller import Controller
import teaser.logic.utilities as utilitis

import uuid

def check(line):
	string = ""
	suffix = ""
	for i in line:
		if(i == "("):
			suffix += i  
		elif (i == "U"):
			suffix += i
			if suffix == "(U":
				break
		else:
			string += i
	return string

class createXml:
	def start(self):
		#root = et.Element("TypeBuildingElements")
		#root.set("version" , "0.4")	
		#rootMaterial = et.Element("MaterialTemplates")
		#rootMaterial.set("version" , "0.4")	
		# count maxlines
		f = open("test.txt", "r")
		num_lines = sum(1 for line in f)
		f.close 
		
		
		f = open("test.txt", "r")
		# line startDocument
		f.readline()
		building_age_group = str(f.readline())
		index = 24
		while(True):
			# type_of_wall
			name_wall = str(f.readline())
			if name_wall.startswith("Roof"):
				wall0 = Rooftop()
				wall1 = Rooftop()
				wall2 = Rooftop()
			
			if name_wall.startswith("Wall"):
				wall0 = OuterWall()
				wall1 = OuterWall()
				wall2 = OuterWall()				
				
			if name_wall.startswith("Floor"):
				wall0 = Floor()
				wall1 = Floor()
				wall2 = Floor()				
				
			if name_wall.startswith("Window"):
				wall0 = Window()
				wall1 = Window()
				wall2 = Window()				
				
			if name_wall.startswith("Door"):
				wall0 = OuterWall()
				wall1 = OuterWall()
				wall2 = OuterWall()
			
			
			dummyValue = 99
			
			layer = Layer()
			layer.id = 1
			layer.thickness = dummyValue
			mat = Material(layer)

			wall0.surface_area = dummyValue
			wall0.construction_type = "tabula_standard" 
			wall0.building_age_group = [1860,1918]
			wall0.u_value = dummyValue
			wall0.add_layer(layer, 0)
			
			wall1.surface_area = dummyValue
			wall1.construction_type = "tabula_refurbished" 
			wall1.building_age_group = [1860,1918]
			wall1.u_value = dummyValue
			wall1.add_layer(layer, 0)
			
			wall2.surface_area = dummyValue
			wall2.construction_type = "tabula_advanced_refurbished" 
			wall2.building_age_group = [1860,1918]
			wall2.u_value = dummyValue
			wall2.add_layer(layer, 0)

			# surface area
			f.readline()
			wall0.surface_area = f.readline()
			wall1.surface_area = f.readline()
			wall2.surface_area = f.readline()
		
			# type of construction/refurbishment measure
			f.readline()
			f.readline()
			f.readline()
		
			# material englisch
			wall0.material = check(f.readline())
			# material deutsch
			f.readline()
			# material englisch
			wall1.material = check(f.readline())
			# material deutsch
			f.readline()
			# material englisch
			wall2.material = check(f.readline())
			# material deutsch
			f.readline()
		
			# picture (muell beim kopieren)
			f.readline()
			f.readline()
			f.readline()
			f.readline()
			
			# u_value
			f.readline()
			# leerzeile
			f.readline()
			wall0.u_value = f.readline()
			wall1.u_value = f.readline()
			wall2.u_value = f.readline()
			
			
			path = utilitis.get_full_path("Data\Input\InputData\TabulaGermany.xml")
			prefix_path, suffix_path = utilitis.split_path(path)
			wall0.save_type_element(prefix_path, suffix_path)
			wall1.save_type_element(prefix_path, suffix_path)
			wall2.save_type_element(prefix_path, suffix_path)

			index += 22
			if(index > num_lines):
				break
