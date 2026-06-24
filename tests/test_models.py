import pytest
from models.product import Product


def test_valid_product():
    p = Product(
        id="PROD999",
        title="Test Shirt",
        price=999,
        sizes=["M"],
        colors=["blue"],
        description="A test shirt.",
        tags=["casual"],
        category="shirt",
        gender="men",
        stock=10,
    )
    assert p.id == "PROD999"


def test_invalid_id():
    with pytest.raises(ValueError):
        Product(
            id="BADID",
            title="Test",
            price=100,
            sizes=["M"],
            colors=["blue"],
            description="x",
            tags=["casual"],
            category="shirt",
            gender="men",
            stock=1,
        )


def test_negative_price():
    with pytest.raises(ValueError):
        Product(
            id="PROD998",
            title="Test",
            price=-10,
            sizes=["M"],
            colors=["blue"],
            description="x",
            tags=["casual"],
            category="shirt",
            gender="men",
            stock=1,
        )


def test_negative_stock():
    with pytest.raises(ValueError):
        Product(
            id="PROD997",
            title="Test",
            price=100,
            sizes=["M"],
            colors=["blue"],
            description="x",
            tags=["casual"],
            category="shirt",
            gender="men",
            stock=-1,
        )
