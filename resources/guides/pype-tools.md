# OpenPype Tools

A set of powershell scripts that automates certain processes for `openpype` development, [read more](https://openpype.io/docs/dev_build/).

Tools are used for:

1) Run from source
2) Build OpenPype
3) Create ZIP 



---
## Before running tools

My routine before running any tools : 
1) Open power shell 
2) Run `cd openpype_local_repo_path`
3) Run `Set-ExecutionPolicy -ExecutionPolicy unrestricted`

### Run from source 

1) Run `.\tools\create_env.ps1`
2) Run `.\tools\fetch_thirdparty_libs.ps1`
3) Run `.\tools\run_tray.ps1`

### Build OpenPype
1) Run `.\tools\create_env.ps1` 
2) Run `.\tools\fetch_thirdparty_libs.ps1`
3) Run `.\tools\build.ps1` 
4) [Optional] Run `.\tools\build_win_installer.ps1`

### Create ZIP 
1) Run `.\tools\create_env.ps1` 
2) Run `.\tools\create_zip.ps1 --path "OpenPype_CodeBase_Path\deployment"` 


---

## Troubleshooting 

I faced these errors and these solutions worked for me.

1) UNC Paths

        Expecting value: line 1 column 1 (char 0)
        !!! Poetry command failed.

    [Solution ✅] Apparently, Power shell script was unhappy because of my network path. I copied source code to local folder and it worked.

2) No git repository
   
        fatal: not a git repository (or any of the parent directories): .git

    [Solution 1 ✅] Run `git init` <br>
    [Solution 2 ✅] Clone repo with git instead of copying and pasting
        
        git clone --recurse-submodules https://github.com/pypeclub/OpenPype.git

3) poetry failed 
 
        Program 'poetry.exe' failed to run

    [Solution ✅] 
     1) Delete **.poetry** **.venv** folders 
     2) Run `.\tools\create_env.ps1`

<br>

4) Cannot find Inno 
    
        !!! Cannot find Inno Setup command
        !!! You can download it at https://jrsoftware.org/

    If you read docs properly, you won't face this error, [find it here](https://openpype.io/docs/dev_build/#build_win_installer)<br>
    [Solution ✅] 
    1) Download Inno Setup [direct link](https://jrsoftware.org/download.php/is.exe)
    2) Add installation path to PATH
   
            C:\Program Files (x86)\Inno Setup 6