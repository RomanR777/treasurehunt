# TEST TASK TREASURE HUNT
## STATUS: WORK IN PROGRESS
### INSTALATION
virtualenv -p `which python3.6` venv

source venv/bin/activate

pip install -r requirements.txt

### LINT
flake8

### TEST
python -m pytest --cov=core tests