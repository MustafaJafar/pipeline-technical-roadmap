# Pipeline Development
how to add your custom code


## OpenPype

## Prism 2.0 

- [Prism Code snippets](resources/code_snippets/prism_snippets.py). 

### Extend Prism
In prism you can do 4 main things: 
1) Access the Prism Python API from within your own custom tools. *It doesn't need to be a Prism plugin or hook.*
    ```
    import PrismInit
    core = PrismInit.pcore
    sequences, shots = core.entities.getShots()
    core.popup("Number of shots in current project: {}".format(len(shots)))
    ```

2) Add a Custom python module <br>
    by copying it to: 
    - Project `{project_path}/00_Pipeline/CustomModules/Python`
    - Prism Scripts `{prism_root}/Scripts` ,*Be careful!*

3) Add a Custom Plugin, *Refer to docs to learn more!*<br>
    You can find empty templates to start with:

      - {prism_root}/Plugins/Apps <br>
      - {prism_root}/Plugins/Custom <br>

    Then copy it to:
      - `{prism_data}/plugins`
      - `{user_documents}/prism2/plugins`
      - `{project_path}/00_Pipeline/Plugins/Apps` 

4) Add some actions on certain events **i.e. Hooks, Callbacks**
    - Hooks can be found at `{project_path}/00_Pipeline/Hooks`
    - Callback are used in custom Prism plugins, [Read more](https://prism-pipeline.com/docs/latest/index/development/developingPlugins.html#using-callbacks)

<br>

> Note: <br>
> Your code would be lost when you update Prism to a newer version.<br>
> This applies only to cases where you modify any Prism scripts directly or store scripts in the Prism root folder. If you store your custom code in plugins/hooks or files outside of the Prism root folder, they will not be affected when updating Prism.

