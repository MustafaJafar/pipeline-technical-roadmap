# Pipeline Development
how to add your custom code


## OpenPype

## Prism 2.0 

- [Prism Code snippets](resources/code_snippets/prism_snippets.py). 

### Custom Modules / Plugins
In prism you can do 2 main things: 
1) Add a Custom python module <br>
    by copying it to: 
    - Project `{project_path}/00_Pipeline/CustomModules/Python`
    - Prism Scripts `{prism_root}/Scripts` ,*Be careful!*

2) Add a Custom Plugin, *Refer to docs to learn more!*<br>
    You can find empty templates to start with:

      - {prism_root}/Plugins/Apps <br>
      - {prism_root}/Plugins/Custom <br>

    Then copy it to:
      - `{prism_data}/plugins`
      - `{user_documents}/prism2/plugins`
      - `{project_path}/00_Pipeline/Plugins/Apps` 


<br>

> According to [prism docs](https://prism-pipeline.readthedocs.io/en/latest/index/feature_reference/#overview) <br>
> Your code would be lost when you update Prism to a newer version.

