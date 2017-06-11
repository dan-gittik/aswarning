# As Warning

A context manager that turns exceptions to warnings.

```python
>>> from aswarning import as_warning

>>> with as_warning():
...  raise ValueError('foo')
... 
aswarning.py:16: Warning: 
Traceback (most recent call last):
  File "aswarning.py", line 14, in as_warning
    yield
  File "<stdin>", line 2, in <module>
    ValueError: foo

>>> class MyWarning(Warning):
...     pass
>>> with as_warning('something went wrong', MyWarning):
...     raise ValueError('foo')
...
aswarning.py:16: MyWarning: something went wrong
Traceback (most recent call last):
  File "aswarning.py", line 14, in as_warning
    yield
  File "<stdin>", line 2, in <module>
    ValueError: foo
```
