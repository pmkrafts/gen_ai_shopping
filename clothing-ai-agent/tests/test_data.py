from data.store import get_products, search_products


def test_all_products_load():
    products = get_products()
    assert len(products) >= 20


def test_ids_unique():
    products = get_products()
    ids = [p.id for p in products]
    assert len(ids) == len(set(ids))


def test_search_by_color():
    results = search_products(filters={"color": "red"})
    assert all("red" in [c.lower() for c in p.colors] for p in results)


def test_search_by_size():
    results = search_products(filters={"size": "M"})
    assert all("M" in [s.upper() for s in p.sizes] for p in results)


def test_search_by_price_range():
    results = search_products(filters={"min_price": 500, "max_price": 2000})
    assert all(500 <= p.price <= 2000 for p in results)


def test_search_by_tag():
    results = search_products(query="summer")
    assert any("summer" in p.tags for p in results) or len(results) == 0


def test_in_stock_excludes_zero():
    results = search_products(filters={"in_stock": True})
    assert all(p.stock > 0 for p in results)