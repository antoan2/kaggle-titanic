# Requirements
- docker
- docker-compose
- kaggle-api installed

# Setup
```
# Get the datas
mkdir data
kaggle competitions download -c titanic
```
## With docker
```
docker-compose build
```

## With virutalenv
```
virtualenv --pyton=python3.6 venv
source venv/bin/activate
pip install -r ./learning-tool/src/requirements.txt
```

# Usage
You can run the main script or an ipython command.

## With docker
```
docker-compose run --rm learning-tool python main.py
docker-compose run --rm learning-tool ipython
```

## With virutalenv
```
source venv/bin/activate
python main.py
ipython
```

# TODO
- Explain notebooks access in Readme
- Write notebooks to analyse the data
- Test more models
- Model fine tuning
