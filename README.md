# Conda demo

## 1. Install Conda

Already installed globally on my system. If you don't have Conda installed, you can download it from [here](https://docs.conda.io/en/latest/miniconda.html).

## 2. Create a new Conda environment

```bash
conda create --name multi-lang-demo python=3.8 nodejs=18.18.2 --yes
```

This command creates a new environment named `multi-lang-demo`, installing Python 3.8 and Node.js into it.

## 3. Activate the Conda environment

```bash
echo "\033[31mBefore activation, the current versions are Node[$(node --version 2>/dev/null || echo "None")] and Python[$(python --version)]\033[0m"
conda activate multi-lang-demo
echo "\033[32mAfter activation, the current versions are Node[$(node --version)] and Python[$(python --version)]\033[0m"
```

## 4. Python package management

Install a Python package to demonstrate managing Python dependencies:

```bash
conda install flask
```

Here's a simple Flask app to show the installed package worked.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Flask!'

if __name__ == '__main__':
    print("Running Flask app...")
    app.run()
```

## 5. Node.js package management

```bash
npm install express@4.18.3
```
Here's a simple Express app to show the installed package worked.

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World from Express!');
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
```

## 6. Run the applications

In different terminals, run the following commands to start the applications:
```bash
conda activate multi-lang-demo
python app.py 
```
```bash
conda activate multi-lang-demo
node server.js
```

## 7. Benefits

- **Unified Environment Management**: One environment for both Python and Node.js dependencies.
- **Simple and efficient**: Simplifies the workflow and reduces the complexity of managing multiple language environments.
- **Reproducible**: All developers work with the same environment setup and no "it works on my machine" problems.

## 8. Clean-up

```bash
conda deactivate
conda remove --name multi-lang-demo --all --yes
rm -rf node_modules
```

## 9 Speedy setup

Given the `environment.yml` file:
```yml
name: multi-lang-demo
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.8
  - nodejs=18.18.2
  - flask
  - pip
  - pip:
    - flask
```
And the `package.json` file:
```json
{
  "dependencies": {
    "express": "^4.18.3"
  }
}
```
You can run the following commands to set up the environment and run the applications:
```bash
conda env create -f environment.yml
conda activate multi-lang-demo
npm install
python app.py & node server.js & wait
```

