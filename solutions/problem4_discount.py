from numbers import Real


def get_discount(price: Real, discount_percent: Real) -> float:
    if (
        isinstance(price, bool)
        or isinstance(discount_percent, bool)
        or not isinstance(price, Real)
        or not isinstance(discount_percent, Real)
    ):
        raise TypeError("price and discount_percent must be numbers")

    if price < 0:
        raise ValueError("price cannot be negative")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")

    return float(price - (price * discount_percent / 100))
