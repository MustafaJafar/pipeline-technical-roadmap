"""
Auto Name Conventions Renamer for Maya.
"""

from collections import (defaultdict  , OrderedDict )
import maya.mel as mel
import maya.cmds as cmds
    
objs_dic = defaultdict( list )
name_convs = OrderedDict( [ ("mesh" , "_GEO")  ,
                ("nurbsCurve"  , "_CRV") ,
                ("nurbsSurface" , "_NRB") ,
                ("locator"   , "_LOC") , 
                ("transform" , "_GRP") ])

for obj in cmds.ls(type = "transform" , l = 1):
    child = cmds.listRelatives(obj , children = 1 , f =1)
    if (child) :
        typ = cmds.nodeType(child[0])
        if not obj.endswith(name_convs.get(typ, "")): objs_dic[typ].append(obj)

    else : 
        if not obj.endswith(name_convs.get(typ, "")): objs_dic[cmds.nodeType(obj)].append(obj)


    
for typ , suffix in name_convs.items() :
    objs = objs_dic.get(typ ,[])
    if (objs) :
        #print(objs)
        cmds.select(cl=True)
        cmds.select(objs)
        mel.eval(f'searchReplaceNames "$" "{suffix}" "selected";')        
        
    