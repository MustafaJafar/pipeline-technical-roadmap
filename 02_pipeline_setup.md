# Pipeline setup

In my experiment, I'm going to test 

- `openpype` and `prism` for pipeline management 
- `kitsu` for production management


At this point I had setup : 
- Virtually connected virtual machines
- Storage that is sharable across network
 
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
pipline machine 1 runs `kitsu` for `openpype` projects <br>
pipline machine 2 runs `kitsu` for `prism` projects <br>