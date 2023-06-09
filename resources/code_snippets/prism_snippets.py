import os 

# Access prism python API 
import PrismInit
core = PrismInit.pcore

# Example on using prism python API
# you can access it from within your own custom tools. It doesn't need to be a Prism plugin or hook.
sequences, shots = core.entities.getShots()
core.popup("Number of shots in current project: {}".format(len(shots)))


# Base Directories 
core.prismRoot
core.prismLibs
core.projectPath
core.getPrismDataDir()
core.getUserPrefDir()

ffmpegPath = os.path.join(core.prismLibs, "Tools", "FFmpeg", "bin", "ffmpeg.exe"  )

# Get current asset data 
fn = core.getCurrentFileName()
data = core.getScenefileData(fn)



# Get User name 
username = core.username.title()



# Get plugin name
App = core.appPlugin.pluginName

# Access Statmanger 
sm = core.getStateManager()
importStates = [state for state in sm.states if state.ui.className == "ImportFile"]
for state in importStates : 
    print( sm.getFilePaths(state))

# Automated Import in StateManager, this works in prism 1.0 
prismImport = sm.tw_import
item_path = "" 
existed_import_items = [prismImport.topLevelItem(i).ui.e_file.text() for i in range(prismImport.topLevelItemCount())] 
if (item_path not in existed_import_items) :
    imported_item = sm.createState("ImportFile" , importPath = item_path)
    # imported_item.ui.updateUi() # update ui after item was imported

existed_tasks = [prismImport.topLevelItem(i).ui.taskName for i in range(prismImport.topLevelItemCount())]
if ("_ShotCam" not in existed_tasks ):
    sm.shotCam()

prismImport.topLevelItem(0).ui.updateUi() #get the first item and use it to update ui 



# Automated Export in StateManager, example to craete playblast in maya
item_name = "preview"
execute_flag = True 
prismExport = sm.tw_export
existed_export_items = [prismExport.topLevelItem(i) for i in range(prismExport.topLevelItemCount()) if item_name in prismExport.topLevelItem(i).ui.l_taskName.text()]
if (not existed_export_items):
    item = sm.createState("Playblast")
    item.ui.l_taskName.setText(item_name)
else : 
    item = existed_export_items[0]
    
item.ui.cb_rangeType.setCurrentIndex(0) # set frame range to "scene"
item.ui.cb_formats.setCurrentIndex(2)   # set output fromat to ".mp4 (with audio)"
if (execute_flag): 
    item.ui.executeState(sm) #cause warning if quicktime video is not installed.

    playblast_path =  item.ui.l_pathLast.text() 



# Tips for prism hooks 
# Access Core object in hooks
def main (*args, **kwargs) :  
    core = kwargs["core"] 
    App = core.appPlugin.pluginName
    if App == "Maya" :
        core.popup("This is Maya!")

# Add your checks in hooks which is easier than using the prePublish callback in a custom Prism plugin to run your checks.
def myCheck(stateManager):
    if stateManager.core.appPlugin.pluginName != "Maya":
        return True

    import maya.cmds as cmds
    obj = cmds.ls("myRequiredObject")
    return bool(obj)

def main(*args, **kwargs):
    print(args, kwargs)
    stateManager = args[0]
    if not myCheck(stateManager):
        stateManager.core.popup("Checks not passed.")
        return {"cancel": True}
    

# Get Assets list 
assets = core.entities.getAssets()

# Get Shots List 
shots = core.entities.getShots()

# Get latest version path 
fname = core.getCurrentFileName()
entity = core.getScenefileData(fname)

# entity = assets[0] # You can do something like this! 
products = list(core.products.getProductNamesFromEntity(entity).keys())
filepath = core.products.getLatestVersionpathFromProduct(products[0] , entity=entity)

