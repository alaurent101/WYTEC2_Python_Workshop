## Workshop requirements

There are 2 ways to carry on with the workshop:

1. Using **Anaconda** (on your computer, install required)\
    We will use Spyder (desktop, most advanced) and JupyterLab (notebooks, most user friendly)
2. Using a **Binder** (online)\
   You can run and modify code during the workshop, but changes are not saved. The **Binder** is that same as the **Workshop notebook** but you can run the code within.

## If option 1: Install/Download BEFORE the workshop (you probably already did this)

Do the following BEFORE the beginning of the workshop (ideally the day before). This takes about 40 minutes, at reasonably good internet speed.

1. Install **Anaconda**, which is a free "bundle" of Python and many modules, libraries and other programs commonly used in scientific research. Please install **Anaconda** from here: https://www.anaconda.com/download

2. Once **Anaconda** finishes installing, open the **Anaconda Navigator**. Sometimes this is automatically opened after the installation finishes. If not, search in the Windows Taskbar (in Mac, search in the Launchpad) for "Anaconda Navigator".
3. Once Anaconda Navigator is open, take a look at the available applications, find the application named “**Spyder**” (option 1a) and “**JupyterLab**”. If it is already installed, there will be a “Launch” button… if it is NOT installed, there will be a “Install” button. Make sure **Spyder** and **JupyterLab** are installed (by clicking on the ”Install” button)… but you may NOT want to “launch” it just yet. Wait until you finish installing the packages shown below.
4. Open the **Anaconda Prompt** (Windows) or **Terminal** (Mac). Easiest way is by searching in the Windows Taskbar the term "Anaconda Prompt" (Windows) or search in the Launchpad for "Terminal" (Mac). Then follow the next ste to install 3 modules (i.e. netcdf4, cartopy and cmocean):

* Install `netcdf4`, by copy-pasting in the **Anaconda Prompt (or Terminal)**: 
<div class='terminalBlock'>conda install -c anaconda netcdf4</div>

   * Click [Enter]
   * If it asks you "are you sure?", type "y" and click [Enter] again.<br><br>
   
* Install `cartopy`, by copy-pasting in the **Anaconda Prompt (or Terminal)**:
<div class='terminalBlock'>conda install -c conda-forge cartopy</div>

   * Click [Enter]
   * If it asks you "are you sure?", type "y" and click [Enter] again.<br><br>
   
* Install `cmocean`, by copy-pasting in the **Anaconda Prompt (or Terminal)**:
<div class='terminalBlock'>conda install -c conda-forge cmocean</div>

   * Click [Enter]
   * If it asks you "are you sure?", type "y" and click [Enter] again.

5. Get the workshop files from **GitHub**. Download the workshop repository from here: https://github.com/alaurent101/WYTEC2_Python_Workshop/archive/refs/heads/main.zip

   Unzip the file anywhere on your computer and rename the folder **WYTEC2_Python_Workshop**. This will be the base location for the workshop.

## If option 2:

The **Binder** is available here: [![Binder](images/badge_logo.svg)](https://mybinder.org/v2/gh/alaurent101/WYTEC2_Python_Workshop/HEAD?urlpath=%2Fdoc%2Ftree%2FWYTEC2_PythonTutorial.ipynb)

It should take less that a minute to build the **Binder** and you'll be ready to go. It will look similar to the **Workshop notebook**

## Workshop mechanics (how to work through this workshop)

For this workshop you will need 3 programs (sometimes 4):

1. **Workshop notebook**: It is this [web-page](https://nbviewer.org/github/alaurent101/WYTEC2_Python_Workshop/blob/main/WYTEC2_PythonTutorial.ipynb), which has the instructions on what to do in the lab. If you are reading "this" you already found Workshop manual.
2. **Spyder**: This is the desktop program that you will use to write and run Python code. We'll talk more about **Spyder** below.
3. **JupyterLab**: This is the notebook program that you will also use to write and run Python code. We'll talk more about **JupyterLab** below.
4. **Terminal**: Every once in a while you will need to install additional Python modules. This is done in the **Terminal**. More on this below.

In the first part of the workshop, you will be required to read along the **Workshop notebook** and copy-paste code from the **Workshop notebook** into **Spyder** to run it. This will create output in the form of numbers, graphs, maps, etc. So you will be jumping back and forth between the **Workshop notebook** and **Spyder** throughout the first part of the Workshop. If you chose the **Binder** option you can run the code directly from there.\
In the second part of the workshop, we will work directly on the **Workshop notebook** with **JupyterLab**. If you chose the **Binder** it would look the same (online version).\
