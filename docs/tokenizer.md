# Tokenizer

We want only want to tokenize variables, method and class names.

Rather than trying to make something, that works for all languages, I think it would be better to make a class, and anytime you want to add another language, add a new method for that language.
Something like [code_tokenize](https://pypi.org/project/code-tokenize/), but more tailored for our needs.

General idea of the outcome of the tokenizer:

```python
def func():
    varA = 1

def func():
    varB = 2
```

These two functions are identical except for naming. The tokenizer should _nomralize_ the names.

```python
def func():
    var_1 = 1

def func():
    var_1 = 2
```

## Supported Languages

- Python

For the project, we'll perhaps focus first on Python?

## Other Materials

Check out these materials for referneces to other projects. They have preprocessing and encoding methods.

- [https://huggingface.co/Lazyhope/python-clone-detection](https://huggingface.co/Lazyhope/python-clone-detection)
- [https://github.com/RepoAnalysis/PythonCloneDetection](https://github.com/RepoAnalysis/PythonCloneDetection)
