Deephist GUI 
GUI for an easier use of the deepmed pipeline 

## 0. Requirements
*
*
*


## 1. How to install: 

* pip install -r requirements.txt
* install torch vision/etc

## 2. How to use the GUI:

### 2.a Training 
* choose a folder where the training should be saved.
* choose to train on a certain percentage of the dataset or to apply a k-fold crossvalidation
* to add a cohort, selecting the slide table, clini table and the path where the tiles are stored, then click on add to list. 
  (Changign the cohort names in the list cohort list might help to distinguish the cohorts,however doesn't have any effect on the training)
* as soon as the cohorts are added, one can pick the desired targets to train on. 
* advanced settings offers further settings for the training
* click on run once to start the training.
* settings will be safed in a log file which can be found in logfiles_gui


### 2.b Deployment
* choose a folder with a saved training & a project directory to safe the deployment
* pick the desired models that should be deployed 
* choose the cohorts that should be used for deployment and add to list ( same procedure as in training) 
* choose the desired evaluators and wether they should be grouped or not
* advanced settings again offers settings for the deployment
* click on run once to start the deployment.

### 2.c Visualization
* choose a deployed project path
* choose one of the used targets and the desired evaluator 
* In the subtabs one can find the top/botton tiles, plots of the chosen evaluator, and the logfile of the deployment


 
