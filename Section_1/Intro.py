# Virtual env. creation, Requirment.txt file use 

# Virtual env. creation:
# 
# Go terminal and open comand prompt.
# Now let's create virtual environment. (It is best practice to create for every project diffrent environment)
# code: conda create -p venv python==3.10       (Here venv is environment name)
# 
# Where is comand prompt is there basically this venv name virtual environment created.
# Now for activate that environment:
# code: conda activate venv/    (Here "venv/" means that folder location)
# 
# Now for the deactivate the environment
# code: conda deactivate

# Requirment.txt file use:
# which are the library are we want to use in our project that with exact name of library mention in requirment.txt file.
# Now after writing for installation of all that library
# 
# First of all transfer cmd to that folder where your venv was.
# Then we need to activate it for that 
# code write in cmd: conda activate venv/
# 
# now transfer cmd to that folder where you need.
# now further installation of any packages or requirment file:
# code: pip install -r requirements.txt 

# Now for entire course we use two type of file .pynb and .py
# for run .pynb file in vs code in your venv must install this two package.
# code: pip install ipykernel
# for run .pynb file u need to select kernel venv from search bar.



