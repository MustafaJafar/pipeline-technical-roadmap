# Pipeline setup

In my experiment, I'm going to test 

- `openpype` and `prism` for pipeline management 
- `kitsu` for production management


At this point I had setup : 
- Virtually connected virtual machines
- Storage that is sharable across virtual network
 
    ```
    \\storage\repo
    \\storage\configs

    \\storage\3d
    \\storage\fx
    \\storage\comp
    ```


---

### Setup Kitsu : 
It needs someone who's familiar with linux. <br>
[Deploy kitsu for production guide](resources/guides/kitsu-deploy.md)

<br>

My setup : <br>
`pipline-pype machine` runs `kitsu` for `openpype` projects <br>
`pipline-prism machine` runs `kitsu` for `prism` projects <br>

---

### OpenPype Installation : 
Firstly, Install MongoDB, I choose to install it on `pipline-pype machine` <br>
[Install MongoDB 6 Community guide](resources/guides/mongodb-ubuntu.md)


For user Machines : <br>
- Download win installer from the latset release [OpenPype releases](https://github.com/ynput/OpenPype/releases)
- Add Monogo URL in OpenPype settings 

<br>

Connect `Kitsu` to `OpenPype` : 
- Activate `Kitsu` module in Admin Settings and add `kitsu`'s URL

> This step is done once as it will be saved in the databas.


---

