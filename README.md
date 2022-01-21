
Deephist GUI 
### DeepMed - Graphical User Interface
Here we share the user interface of DeepMed (Direct End-to-End Pipeline for Medical Imaging), which allows users to run the DeepMed through the application instead of running them via Python experiment script. The GUI is intended to easier use of the DeepMed pipeline and currently available to use basic functionalities of DeepMed. 


## 0. Requirements
* CUDA-enabled NVIDIA GPU 
* Python version >= 3.8
* Pip
* git

## Installation (Windows)
* Download the source code
* run the installer.bat file inside the folder (double-click or run in command prompt)


## How to use the GUI:

### Training 
* Choose a folder where the training should be saved.
* Choose to train on a certain percentage of the dataset or to apply a k-fold crossvalidation.
* To add a cohort, selecting the slide table, clini table and the path where the tiles are stored, then click on add to list.
  (Changing the cohort names in the list cohort list might help to distinguish the cohorts,however doesn't have any effect on the training).
* Pick the desired targets to train on (possible as soon as the cohorts are added).
* Advanced settings offers further settings for the training.
* Click run once to start the training.
* Settings will be saved in a log file which can be found in the "logfiles_gui" folder.


### Deployment
* Choose a folder with a saved training & a project directory to safe the deployment.
* Pick the desired models that should be deployed.
* Choose the cohorts that should be used for deployment and add to list ( same procedure as in training).
* Choose the desired evaluators and wether they should be grouped or not.
* Advanced settings again offers settings for the deployment.
* Click on run once to start the deployment.

### Visualization
* Choose a deployed project path.
* Click on the desired file
    * Images will be visualized in the Image tabs
    * Tables will be visualized in the Image tabs
    * The log tab contains the deployment log
    * the Tiles tab is without function yet 
