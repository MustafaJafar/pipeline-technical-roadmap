# DCC apps and APIs

Any app that we use to create a digital art / content `e.g. 3d models`  is called a Digital Content Creation app `DCC app`

---
## Use DCCs as an Artist

This is important for two reasons: <br>

- How code affects a DCC 
- Understand the big picture of a typical VFX pipeline 

You should learn the DCC first in order to be able to understand the effect of your code on it.
>In other words, you need to learn how to use Maya before digging in and creating Maya Scripts and tools! 

So, Give your self time to learn to use the DCC as an artist first<br><br>

Also, I recommend making a project like this to understand the big picture of a typical VFX pipeline so that you can learn: 
  - what is the role of each department 
  - what is the input and output of each DCC
  - how to use each DCC 
  - what each artist do in their daily life at work
<br>

In this project I used DCCs like **Nuke**, **3d Equalizer**, **Houdini**, **Da Vinci Resolve** <br>
More Details: 
1) Set **aces color space** & do basic color corrention in **Nuke**
2) Camera tracking in **3d Equalizer** 
3) 3D scene setup & match lighting in **Houdini** 
4) Create 3d effects in **Houdini** & render in **RenderMan**
5) Composite in **Nuke**
6) Edit sound in **Audacity**
7) Color Grade in **Da Vinci Resolve**

[![Apollo Lunar from garage VFX](https://img.youtube.com/vi/sgYxC825VJU/0.jpg)](https://www.youtube.com/watch?v=sgYxC825VJU)

---

## Use DCCs as a developer

Artists can interact with programs using **UI** "User Interface"

Developers can interact with programs using **API** "Application Programming Interface" which defines how to interact with a certain program via coding. 

Example:<br>
You can write a python code that interacts with Maya via Maya API. <br>
In other words, you can write a python code to do some thing (e.g. create new objects) in Maya Scene. 

<br>

I found these websites and courses useful <br>
Also, Don't forget DCC API documentation! 

Maya API : 
- [Maya Mel Reference](https://help.autodesk.com/cloudhelp/2022/ENU/Maya-Tech-Docs/Commands/)
- [Maya Python Reference](https://help.autodesk.com/cloudhelp/2022/ENU/Maya-Tech-Docs/CommandsPython/)
- [zurbrigg website](https://zurbrigg.com/)
- [Master Rigging & Python Scripting in Maya](https://www.thegnomonworkshop.com/tutorials/master-rigging-python-scripting-in-maya)

<br>

Houdini API : 
- [Houdini Vex Reference](https://www.sidefx.com/docs/houdini/vex/lang.html)
- [Houdini Python Reference](https://www.sidefx.com/docs/houdini/hom/hou/index.html)
- [Procedural Cities with Houdini and Python](https://www.pluralsight.com/courses/houdini-python-procedural-cities)
- [Introduction to Houdini VEX and Python](https://www.fxphd.com/details/578/)
- [Advanced VEX & Python for Houdini TDs](https://www.fxphd.com/details/580/)

<br>

After Effects API : 
- [After Effects Scripting Guide](https://ae-scripting.docsforadobe.dev/)
- [@NTProductions](https://www.youtube.com/@NTProductions)

<br>


Nuke API : 
- [Foundry Python Devguide](https://learn.foundry.com/nuke/developers/latest/pythondevguide/)