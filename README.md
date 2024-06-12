# computer-vision-course
# Sources & udemy course
<b>Udemy course:</b> https://www.udemy.com/share/10143y3@GmhgL2nFG3QDxH4DGeblXwsz6uiLPxBsfSLtQVXG8rsIo30x1YTrkmNiyJJGdCgVwA==/


## Environment setup
### Anaconda
#### Python Path
Add the conda to your python path:
```
export PATH="/home/peter/anaconda3/bin/:$PATH"
```

#### Open Anaconda terminal bash
```
source ~/anaconda3/bin/activate
```

#### Create the conda enviroment of the course
```
conda env create -f cvcourse_linux.yml
```

#### Activate and deactivate the created conda environment
```
# To activate this environment, use                                             
#     $ conda activate python-cvcourse                                          
# To deactivate an active environment, use                                                   
#     $ conda deactivate   
```

### Google Colab
Google colab already has the environment set up to all the needs of the udemy course.
Packages needed:
* matplotlib
* cv2
* Image
* numpy
#### Create a google colab file
Go to your google drive account and click on the three stripes on the top left. Then click "more". You should see now Google Colab as a creatable file.

This will create you a python notebook that is stored in your google drive. You can sync it also with your GitHub Account and give it access to your google drive data.
