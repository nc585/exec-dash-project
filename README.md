# Executive Dashboard Project

A repository for the "Executive Dashboard" project in Professor Rossetti's OPIM 244 class at Georgetown University. 

Original project description: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/projects/exec-dash.md

# Prerequisites 

Anaconda 3.7
Python 3.7
Pip

# Installation

First, fork this: https://github.com/nc585/exec-dash-project

Next, clone or download that repository onto your computer and navigate there from the command line.

```sh
cd exec-dash-project
```

Then, create and activate a new virtual environment using your Anaconda Prompt. You can call this environment "dashboard-env" and install the following within the virtual environment:

```sh
pip install -r requirements.txt
```

# Usage

Analyze monthly sales data to generate a chart for business insight.

```sh
python -m app.monthly_sales
```

# Testing

The first time you are using this project, install the `pytest` package within the virtual environment. In this case, the environment is "dashboard-env".

```sh
pip install pytest
```

Run tests:

```sh
pytest --disable-pytest-warnings # this will prevent warnings by matplotlib during testing
```





