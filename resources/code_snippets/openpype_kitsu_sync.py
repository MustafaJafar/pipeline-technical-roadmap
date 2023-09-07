'''
This code is to sync kitsu projects with openpype
It's no londer needed as the terminal commands are updated 

// sync all projects then run listen
openpype_console module kitsu sync-service -l me@domain.ext -p my_password

// sync specific projects then run listen
openpype_console module kitsu sync-service -l me@domain.ext -p my_password -prj project_name01 -prj  project_name02

// start listen only for all projects
openpype_console module kitsu sync-service -l me@domain.ext -p my_password -lo

---

Furtherly, Terminal Commands may not be used in the futuer as The sync feature may be added to the options in the UI, 
    So an admin can select from a list what projects they want to sync.
'''

#---Get All projects-----
def get_all_projects_1() : 
    import gazu
    names = [item.get("name" , "") for item in gazu.project.all_projects()]
    return names

def get_all_projects_2() : 
    import gazu
    get_name = lambda x : x.get("name" , "")
    names =  list(map(get_name , gazu.project.all_projects()))
    return names


print(f"all projects: {get_all_projects_2()}\n")

#-----------------------------------------
import os 

login = os.environ["KITSU_LOGIN"]
password = os.environ["KITSU_PWD"]

all_projects = get_all_projects_1() # you can use it to list all the projects in kitsu

ignore_projects = []  # a list of projects you want to skip  
filter_projects = () # a tuple of projects you want to sync 

print(f"login: {login}\npassword: {password}\n")
print(f"ignore_projects: {ignore_projects}\n")
print(f"ignore_projects: {filter_projects}\n")

#---Sync Projects-----
from openpype.modules.kitsu.utils.update_op_with_zou import sync_all_projects
# this means sync all projects except ignore_projects 
sync_all_projects(login , password , ignore_projects = ignore_projects  )

# this means sync filter_projects only
sync_all_projects(login , password , filter_projects = filter_projects )
