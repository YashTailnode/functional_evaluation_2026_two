# Debugging Report

## Problem 1 - Incorrect Record Count

### Root Cause

The original implementation split content by `"\n"` and returned the number of
lines. That counted the header as a record and could also count trailing blank
lines. It would also fail for valid CSV fields containing quoted newlines.

### Fix

`count_csv_records` now uses Python's `csv.reader`, ignores blank rows, and
subtracts the header row by default.

### Verification

Unit tests cover the provided example, trailing newlines, blank files, quoted
multiline fields, and files without a header.

### Additional Improvements

The implementation exposes a `has_header` flag for CSV files that do not include
a header.

## Problem 2 - Application Crash

### Root Cause

`json.loads` raises `json.JSONDecodeError` for malformed JSON. The original code
allowed that low-level exception to escape directly, which can crash request
handlers when the caller does not catch it.

### Fix

`parse_json` catches `JSONDecodeError` and raises a custom `JsonParseError` with
line and column information. The original exception is preserved as the cause.

### Verification

Tests cover valid JSON, malformed JSON, useful error details, and exception
chaining.

### Additional Improvements

The custom exception keeps structured `line` and `column` attributes for logging
or API error responses.

## Problem 3 - Memory Leak / Performance Issue

### Root Cause

The original code looped over `records` inside another loop over `records`. For
`n` records, it performed about `n * n` comparisons, so time complexity was
`O(n^2)`. On large inputs this creates serious CPU pressure and also creates
many repeated temporary lists.

### Fix

The optimized version builds a dictionary from `id` to matching records once,
then returns the matching group for each original record.

### Verification

Tests confirm that the output shape and order match the original behavior,
including empty inputs and generator inputs.

### Additional Improvements

Time complexity is reduced to `O(n)`. Space complexity is `O(n)` for the index.
The trade-off is extra memory for the dictionary, but that is much cheaper than
repeated full scans for large files.

## Problem 4 - Hidden Runtime Error

### Root Cause

The formula used division by `discount_percent`:

```python
price - price / discount_percent * 100
```

For `price=1000` and `discount_percent=10`, this evaluates to `-9000` instead
of `900`. When `discount_percent` is `0`, the code divides by zero.

### Fix

The formula is now:

```python
price - (price * discount_percent / 100)
```

The implementation also validates numeric inputs, disallows negative prices,
and accepts only discount percentages from `0` to `100`.

### Verification

Tests cover the provided example, zero discount, full discount, invalid
percentages, negative prices, and non-numeric input.

### Additional Improvements

Input validation makes failures explicit and easier to diagnose.

## Problem 5 - Race Condition / Shared State Bug

### Root Cause

The shared cache can be read and written by multiple requests at the same time.
Two requests for the same uncached user can both miss the cache and call
`fetch_user`. The JavaScript example also checks truthiness, so cached falsy
values such as `null` or `0` would be fetched repeatedly.

### Fix

`ThreadSafeUserCache` uses a per-user lock. Only one thread fetches a missing
user at a time, while requests for different users can still proceed in
parallel. It checks key presence with `in`, so falsy cached values are valid.

### Verification

Tests cover normal caching, caching of a falsy value, and concurrent requests
for the same user.

### Additional Improvements

For production, a cache should usually add expiry, maximum size, metrics, and
clear behavior for fetch failures.

## Problem 6 - Broken Unit Test

### Root Cause

The implementation returned `a - b`, but the test only checked truthiness:

```python
assert add(5, 2)
```

Since `3` is truthy in Python, the test passed even though the result was wrong.

### Fix

`add` now returns `a + b`. Tests assert exact expected values instead of only
checking whether the result is truthy.

### Verification

Tests cover positive numbers, negative numbers, mixed signs, and zero.

### Additional Improvements

The improved tests would fail for subtraction, multiplication, or other
incorrect implementations that still return truthy values.

