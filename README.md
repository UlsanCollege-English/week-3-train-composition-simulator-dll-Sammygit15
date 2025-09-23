[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/VHRrzNBX)
# Train Composition Simulator (DLL)

## Story (why this matters)
In a rail yard, operators **attach** cars at the **front** or **back**, quickly
**detach** either end, or remove a **specific car** in the middle to fix an
issue—while keeping the rest of the train intact.

## Technical description (what to build)
In `src/train.py`, implement:

- `attach_front(car_id)`
- `attach_back(car_id)`
- `detach_front()` → car id or `None`
- `detach_back()` → car id or `None`
- `detach(car_id)` → remove first match; fix neighbors and ends; return `True/False`
- `to_list()` → list of car ids

## Hints
1. When the last car is removed, both `head` and `tail` become `None`.
2. For middle removal, patch neighbors **both ways**.
3. Keep `to_list()` simple for quick debugging.

## Run tests locally
```bash
python -m pytest -q

OR

python -m pytest -q tests/test_train.py
```

## Common problems
- Not updating head/tail when removing the first or last car.
- Half-patched links (changed next but not prev, or vice versa).
- Returning the wrong type from detach_* (should be the car id or None).