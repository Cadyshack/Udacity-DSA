# Route Planner Project

The purpose of this project is to implement the A* Algorithm to find the shortest path between two intersections in a graph.

**NOTE:** The code written by myself is all contained inside the **student_code.py** file. Essentially consists of three functions that perform the A* algorithm returning a list of nodes that consist of the shortest path between two nodes.


## Project Dependencies:

- python >= 3.14
- plotly >= 6.4.0
- networkx >= 3.5
- chart-studio >= 1.1.0
- nbformat >= 5.10.4
- ipykernel >= 7.1.0


## Initial Setup

Because this project had various dependencies such as plotly and code was given to us as a starting point in order to focus on solving the algorithm problem, I decided to use the [uv package manager](https://docs.astral.sh/uv/) in order to share this project.

### Step 1

Install uv by following the instillation instruction found [here](https://docs.astral.sh/uv/getting-started/installation/)

### Step 2

Once uv is installed, navigate to the project folder and in the terminal write the following command to launch the Jupyter Notebook.

```console
uv run --with jupyter jupyter lab
```

More detailed instructions on how to run jupyter notebooks with uv can be found at [https://docs.astral.sh/uv/guides/integration/jupyter/](https://docs.astral.sh/uv/guides/integration/jupyter/)
