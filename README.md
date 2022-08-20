# JSON Web Token Creator for Google Cloud IoT

## Usage
```bash
# Clone the repository.
~$ git clone git@github.com:electricalgorithm/JWT-Creator.git
~$ cd JWT-Creator
# Create a virtual environment to install dependencies.
~$ virtualenv .
~$ source bin/activate
# Install dependencies.
(JWT-Creator) ~$ pip install -r requirements.txt
# Run the program.
(JWT-Creator) ~$ python JWT_Creator.py -i [project_name] -p [private_key_location] -a [algorithm_name] -t [minutes_to_live]
```

## Help
```
usage: JWT_Creator.py [-h] -i PROJECT_ID [PROJECT_ID ...] -p PRIVATE_KEY [PRIVATE_KEY ...] 
        -a ALGORITHM [ALGORITHM ...] [-t MINUTES [MINUTES ...]] [-s SAVE [SAVE ...]]

This application gives you the JWT token you need.

options:
  -h, --help            show this help message and exit
  -i PROJECT_ID [PROJECT_ID ...], --project_id PROJECT_ID [PROJECT_ID ...]
                        Provide your project id as a string.
  -p PRIVATE_KEY [PRIVATE_KEY ...], --private_key PRIVATE_KEY [PRIVATE_KEY ...]
                        Provide the private key file.
  -a ALGORITHM [ALGORITHM ...], --algorithm ALGORITHM [ALGORITHM ...]
                        Provide the algorithm name as a string.
  -t MINUTES [MINUTES ...], --minutes MINUTES [MINUTES ...]
                        Provide duration in terms of minutes.
  -s SAVE [SAVE ...], --save SAVE [SAVE ...]
                        Save the token into a TXT file.
```