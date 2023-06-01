# Pipeline configuration

Settings and configuration in `Prism 2.0` and `OpenPype`
I'm just showing the settings that concern me for now.

### Settings Categories
Open Pype :
  - Studio Settings 
    - System
    - Projects
  - Local Settings 
  
Prism 2.0 : 
  - Project Settings 
  - User Settings 
  
## OpenPype 
- System Settings
  - General 
    - Studio Name 
    - Admin Password
  - Openpype deployment Control
  - Studio Environment Variables
  - Modules
  - Integrations
  - Tools

- Project Settings 
  - File Roots and Templates 
      > You can define default paths (e.g. **Work**, **Render** and **Publish**) <br>
      > You can define custom paths per task type: 
      > 1. add other template: `project_anatomy/templates`
      > 2. add task type: `project_anatomy/tasks`
      > 3. assign template for a task type: **e.g.** `project_settings/global/tools/Workfiles`
  - Attributes
    - Frame Rate
    - Resolution
    - Applications to show in launcher

  - Application Settings
    - Maya : Reference Loader
  
  - Project Folder Structure `project_settings/global/project_folder_structure`
  - Project Specific Environment variables `project_settings/global/project_environments`
  
- Local Settings 
  - Mongo URL
  - Override DCC path 
  - User Specific Environment variables [Disabled by default]

## Prism 2.0
- Project Settings 
  - General 
    - Use Master version
    - Frame Rate
    - Resolution
  - Departments -formerly "Category"- / Tasks 
  - Project Folder Structure 
  - Project Specific Environment variables
  - Project Managment 
    > Kitsu : It only syncs one project, and it only syncs the assigned tasks also. 

- User Settings 
  - DCC Apps paths 
  - Enable/Disable Plugins 
  - User Specific Environment variables

---

## Conclusion 

In my opinion : 

    Prism focuses on user
    OpenPype focuses on studio

Openpype 
  - allows remote collaboration via site sync 
  - can Utilize multi storage servers via templates
  - has centralized Settings/Configurations 
  - is easily scalable
  - requires some practicing for artists, admins and developers 
  - can support more users 

Prism : 
  - is very artist friendly
  - is easier to build a custom pipeline on top of it
  - is easier to operate and maintain 
  - you can create a library project that's folder is shared among remote collaborators via a third party tool (e.g. dropbox).

### For more Info

You can check: 

- Ynput links 
  - https://community.ynput.io/
  - https://openpype.io/
  - https://ayon.ynput.io/

- Prism Links
  - https://prism-pipeline.readthedocs.io/en/latest/

Also, you can have a direct connection with the creators via discord:
  - [Prism discord server](https://discord.gg/6CXhJV5nyJ) 
  - [Ynput discode server](https://discord.gg/ynput)