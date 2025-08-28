# 📘 Understanding `defaultdict` in Python

## What is `defaultdict`?

`defaultdict` is a subclass of Python’s built-in `dict` that **automatically initializes keys** with a default value the first time they’re accessed.

If you try to access a key that doesn’t exist, instead of throwing a `KeyError`, it automatically creates that key with a `default value` that you define.

---

## ✅ Regular `dict` Behavior

```python
my_dict = {}
my_dict['user1'] += 1  # ❌ KeyError: 'user1'
```

## ✅ `default dict` Behavior

```python
from collections import defaultdict

my_dict = defaultdict(int)
my_dict['user1'] += 1  # ✅ No error — user1 is initialized to 0
```