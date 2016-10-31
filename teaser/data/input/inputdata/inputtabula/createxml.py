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
from teaser.data.dataclass import DataClass

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
	"""Creates a new xml file named tabula with given Building data in 
	a txt document"""

	def create(self):
		"""Opens a file(txt). Read the given file line for line and creates 
		the xml."""
	
		f = open("test1.txt", "r")
		num_lines = sum(1 for line in f)
		f.close 
		
		f = open("test1.txt", "r")
		
		#first line (startDocument)
		f.readline()
		#building_age_group
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
		
			# material english
			wall0.material = check(f.readline())
			# material german
			f.readline()
			# material english
			wall1.material = check(f.readline())
			# material german
			f.readline()
			# material english
			wall2.material = check(f.readline())
			# material german
			f.readline()
		
			# picture (garbage)
			f.readline()
			f.readline()
			f.readline()
			f.readline()
			
			# u_value
			f.readline()
			# emptyline
			f.readline()
			wall0.u_value = f.readline()
			wall1.u_value = f.readline()
			wall2.u_value = f.readline()
			
			path = utilitis.get_full_path("Data\Input\InputData\TabulaGermany.xml")
			dc = DataClass
			dc.path_tb = path
			dc.load_tb_binding(dc)
			wall0.save_type_element(dc)
			wall1.save_type_element(dc)
			wall2.save_type_element(dc)

			index += 22
			if(index > num_lines):
				break
