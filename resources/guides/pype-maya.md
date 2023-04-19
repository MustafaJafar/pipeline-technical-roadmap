# Working with OpenPype in Maya

This file is a quick summary of [Openpype Maya](https://openpype.io/docs/artist_hosts_maya/)

## Openpype basic functionality :
- Publish 
- Load 
- Render

### Publish process 

1) Prepare your work for publishing 
2) Create family and set subset
   > Families are used to categorize data, [read more](https://openpype.io/docs/artist_publish)
3) Publish 
4) Deal with errors and re-publish

### Loading tools

- Load 
- Manage
- Library

## In this guide : How to Publish and load

- model 
- material
- rig
- animation
- assembly 
- point cache
- mayascene
- review

### Publish Model Guide

1) Preparation : 
   - Group your objects 
   - Follow Naming Conventions
  
        ```
        Suffices must be:
            - mesh:
                _GEO (regular geometry)
                _GES (geometry to be smoothed at render)
                _GEP (proxy geometry; usually not to be rendered)
                _OSD (open subdiv smooth at rendertime)
            - nurbsCurve: _CRV
            - nurbsSurface: _NRB
            - locator: _LOC
            - null/group: _GRP
            - animation contreller : _CTR
        Suffices can also be overridden by project settings.
        ```

2) Create family and set subset
   1) Select your group
   2) Go to **OpenPype → Create...**
   3) Select **Model** and **Subset**
        
        ![Select **Model** and **Subset**](../images/pype-maya-01.jpg)

3) Publish 
   1) Go **OpenPype → Publish....**
   2) Set **status** and click **play button**
    
        ![Select **Model** and **Subset**](../images/pype-maya-02.jpg)

   3) Deal with errors and re-publish

   
### Publish Model Example