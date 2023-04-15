# Pipeline setup

In my experiment, I'm going to test 

- `openpype` and `prism 2.0` for pipeline management 
- `kitsu` for production management

> I chose `openpype` and `prism 2.0` as both supports **Kitsu** as well as **USD**

<br>

At this point I have : 
- 2 virtual pipeline machines
- 1 virtual storage machine that shares paths like these on network
 
    ```
    \\storage\repo
    \\storage\configs

    \\storage\3d
    \\storage\fx
    \\storage\comp
    ```


---

## Setup Kitsu : 
It needs someone who's familiar with linux. <br>
[Deploy kitsu for production guide](resources/guides/kitsu-deploy.md)

<br>

My setup : <br>
`pipline-pype` machine that runs `kitsu` and `MongoDB` for `openpype` projects <br>
`pipline-prism` machine that runs `kitsu` for `prism 2.0` projects <br>

---

## OpenPype Installation : 
Firstly, Install **MongoDB Server**, I choose to install it on `pipline-pype` machine <br>
[Install MongoDB 6 Community guide](resources/guides/mongodb-ubuntu.md)


For user Machines : <br>
- Download win installer from the latset release [OpenPype releases](https://github.com/ynput/OpenPype/releases)
- Add Monogo URL in OpenPype settings 

<br>

Connect `openPype` to `kitsu` : 
- Activate `kitsu` module in Admin Settings and add `kitsu`'s URL
- Note that `openpype` sync with all `kitsu` projects and assets that complies to `openpype` naming rules  

> This step is done once as it will be saved in `openpype`'s  database.

>Naming convention:<br>
>At this moment names of assets, tasks, subsets or representations can contain only letters, numbers and underscore.
---

## Prism 2.0 Installation : 
Firstly, Get `prism 2.0` license <br>
Email to: contact@prism-pipeline.com

For user Machines : <br>
Install as follows [Prism Getting Started](https://prism-pipeline.com/docs/latest/index/getting_started.html)

>P.S.<br>
>This beta version of Prism Pipeline 2.0 is intended for testing purposes only.<br>It is not recommended to use it for commercial projects, but possible on your own risk.

<br>

Connect `Prism 2.0` to `Kitsu` : 

- From

        Options > Project Management > Setup 

Connect `prism 2.0` to `kitsu` : 
- Note that `prism 2.0` sync with the specified `kitsu` project

&emsp;for more info: [Prism Kitsu setup](https://prism-pipeline.com/docs/latest/index/plugins/Kitsu.html)


> You can Use the same `kitsu` server with both `openpype` as well as `prism 2.0`  <br>
> As `openpype` will sync with all projects that complies to its naming convention <br>
> And `prism 2.0` can sync with the rest <br>


---