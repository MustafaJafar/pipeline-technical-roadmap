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
go to: https://zou.cg-wire.com/

<br>

My setup : <br>
pipline-pype machine runs `kitsu` for `openpype` projects <br>
pipline-prism machine runs `kitsu` for `prism` projects <br>

---

### OpenPype Installation : 
Firstly, Setup MongoDB on pipeline-pype machine as follows: [How to Install MongoDB 6 on Ubuntu 22.04](https://www.youtube.com/watch?v=rdCk3YzW5os)


For user Machines : <br>
- Download win installer from the latset release [OpenPype releases](https://github.com/ynput/OpenPype/releases)
- Add Monogo URL in OpenPype settings 

<br>

Connect `Kitsu` to `OpenPype` : 
- Activate `Kitsu` module in Admin Settings and add `kitsu`'s URL

> This step is done once as it will be save in the databas.


---

