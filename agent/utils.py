from typing import Callable, TypeVar

T = TypeVar("T")


def retry(
    func: Callable[[], T],
    max_retries: int = 2,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> T:
    """Call func up to max_retries + 1 times on failure.

    Args:
        func: Callable taking no arguments.
        max_retries: Number of retries after the first failure.
        exceptions: Tuple of exceptions to catch and retry.

    Returns:
        The result of func.

    Raises:
        The last exception if all retries fail.
    """
    last_exception: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            return func()
        except exceptions as e:
            last_exception = e
            if attempt < max_retries:
                continue
    raise last_exception
