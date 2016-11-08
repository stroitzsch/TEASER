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
from teaser import project


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


def checkMat(wall, materialName):
    dummyString = "dummy"
    dictLayer = {"brickwork": [1, "brickwork"],
                 "tilted roof with clay/straw filling between rafters":
                 [2, "tilted roof with clay", "straw filling between rafters"],
                 "insulate cavity between rafters heighten rafters and clear interspace if necessary), total insulation thickness 12 cm":
                 [3, "insulate cavity between rafters",
                     "clear interspace if necessary", "thickness"],
                 "insulate cavity between rafters + insulation layer, total insulation thickness 30 cm":
                 [3, "insulate cavity between rafters",
                     "clear interspace if necessary", "thickness", 30],
                 "add 8 cm of insulation on inner surface air-tight cladding, water pipes must not be conducted in outer brickwork)":
                 [3, "insulation", "inner surface ", "bricjwork" "thickness"],
                 "if external insulation is possible: add 24 cm of insulation, creation of historical facade appearance e.g. wooden shingles, plaster, strip tiles, ...)":
                 [1, dummyString],
                 "vault ceiling": [1, "vault ceiling"],
                 "add 8 cm of insulation below / alternatively: on top of ceiling in case of floor renovation)":
                 [1, dummyString],
                 "add 12 cm insulation below in case of sufficient cellar height) / alternatively: on top of ceiling in case of floor renovation) or combination of both":
                 [1, dummyString],
                 "wooden window with dual-pane glazing":
                 [1, dummyString],
                 "windows with double glazing, argon filled, low-E, historical impression divisions)":
                 [1, dummyString],
                 "windows with triple glazing, argon filled, low-E, insulated frame, historical impression divisions)":
                 [1, dummyString],
                 "wooden door":
                 [1, dummyString],
                 "entry door with insulation layer ":
                 [1, dummyString],
                 "mount new door with insulation layer ":
                 [1, dummyString],
                 "wooden beam ceiling":
                 [1, dummyString],
                 "add 12 cm insulation above + flooring if necessary)":
                 [1, dummyString],
                 "add 30 cm insulation above + flooring if necessary)":
                 [1, dummyString],
                 "brickwork, two layers":
                 [2, dummyString],
                 "add 12 cm of insulation + plaster external insulated render system), alternative: curtain wall e.g. cellulose between timbers)":
                 [1, dummyString],
                 "add 24 cm of insulation + plaster external insulated render system), alternative: curtain wall":
                 [1, dummyString],
                 "concrete ceiling with steel beams and wooden flooring":
                 [1, dummyString],
                 "add 8 cm of insulation below / alternatively: on top of ceiling in case of floor renovation)":
                 [1, dummyString],
                 "add 12 cm insulation below in case of sufficient cellar height) / alternatively: on top of ceiling in case of floor renovation) or combination of both":
                 [1, dummyString],
                 "wooden door":
                 [1, dummyString],
                 "entry door with insulation layer":
                 [1, dummyString],
                 "mount new door with insulation layer ":
                 [1, dummyString],
                 "plastic frame window with dual-pane glazing":
                 [1, dummyString],
                 "windows with double glazing, argon filled, low-E":
                 [1, dummyString],
                 "windows with triple glazing, argon filled, low-E, insulated frame":
                 [1, dummyString],
                 "brickwork, two layers":
                 [1, dummyString],
                 "concrete ceiling":
                 [1, dummyString],
                 "masonry of hollow blocks or honeycomb bricks":
                 [1, dummyString],
                 "cavity blocks ceiling":
                 [1, dummyString],
                 "concrete ceiling with 1 cm insulation":
                 [1, dummyString],
                 "concrete ceiling with 5 cm insulation":
                 [1, dummyString],
                 "12 cm insulation on ceiling + roofing":
                 [1, dummyString],
                 "30 cm insulation on ceiling + roofing":
                 [1, dummyString],
                 "concrete panels":
                 [1, dummyString],
                 "add 12 cm of insulation + plaster external insulated render system), alternative: curtain wall e.g. cellulose between timbers)":
                 [1, dummyString],
                 "add 24 cm of insulation + plaster external insulated render system), alternative: curtain wall":
                 [1, dummyString],
                 "concrete ceiling with 2 cm insulation":
                 [1, dummyString],
                 "add 8 cm of insulation below / alternatively: on top of ceiling in case of floor renovation)":
                 [1, dummyString],
                 "add 12 cm insulation below in case of sufficient cellar height) / alternatively: on top of ceiling in case of floor renovation) or combination of both":
                 [1, dummyString],
                 "metal door":
                 [1, dummyString],
                 "":
                 [1, dummyString],
                 "":
                 [1, dummyString],
                 "":
                 [1, dummyString],
                 "":
                 [1, dummyString],
                 "":
                 [1, dummyString],
                 "":
                 [1, dummyString],
                 "":
                 [1, dummyString],
                 "":
                 [1, dummyString],
                 "":
                 [1, dummyString],
                 "":
                 [1, dummyString],
                 "":
                 [1, dummyString]
                                
                 
                 }

    try:
        dcMat = DataClass
        pathMat = utilitis.get_full_path(
            "Data\Input\InputData\MaterialTemplates2.xml")
        dcMat.path_mat = pathMat
        dcMat.load_mat_binding(dcMat)

        materialNameList = dictLayer[materialName]
        numberOfLayer = materialNameList[0]
        layer = Layer()
        layer.id = 1
        layer.thickness = 65
        mat = Material(layer)
        # print(materialNameList[1])
        mat.name = materialNameList[1]
        wall.add_layer(layer, 0)
        mat.save_material_template(dcMat)

        if numberOfLayer >= 2:
            layer = Layer()
            layer.id = 2
            layer.thickness = 65
            mat2 = Material(layer)
            # print(materialNameList[2])
            mat2.name = materialNameList[2]
            wall.add_layer(layer, 1)
            mat2.save_material_template(dcMat)

        elif numberOfLayer == 3:
            layer = Layer()
            layer.id = 3
            layer.thickness = 65
            mat3 = Material(layer)
            # print(materialNameList[3])
            mat3.name = materialNameList[2]
            wall.add_layer(layer, 2)
            mat3.save_material_template(dcMat)

    except:
        print(materialName)


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

        # first line (startDocument)
        f.readline()
        # building_age_group
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

            wall0.surface_area = dummyValue
            wall0.construction_type = "tabula_standard"
            wall0.building_age_group = [1860, 1918]
            wall0.u_value = dummyValue

            wall1.surface_area = dummyValue
            wall1.construction_type = "tabula_refurbished"
            wall1.building_age_group = [1860, 1918]
            wall1.u_value = dummyValue

            wall2.surface_area = dummyValue
            wall2.construction_type = "tabula_advanced_refurbished"
            wall2.building_age_group = [1860, 1918]
            wall2.u_value = dummyValue

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
            material0 = str(check(f.readline()))
            material0 = material0.replace("\n", "")
            checkMat(wall0, material0)
            # material german
            f.readline()
            # material english
            material1 = str(check(f.readline()))
            material1 = material1.replace("\n", "")
            checkMat(wall1, material1)
            # material german
            f.readline()
            # material english
            material2 = str(check(f.readline()))
            material2 = material2.replace("\n", "")
            checkMat(wall2, material2)
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

            path = utilitis.get_full_path(
                "Data\Input\InputData\TabulaGermany.xml")
            dc = DataClass
            dc.path_tb = path
            dc.load_tb_binding(dc)
            wall0.save_type_element(dc)
            wall1.save_type_element(dc)
            wall2.save_type_element(dc)

            index += 22
            if(index > num_lines):
                break
