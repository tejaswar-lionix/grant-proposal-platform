"""Tests for compliance edge distinct"""

def test_compliance_edge_0():
    doc={"pages":2,"font":"Arial 12pt","margins":1.0}
    assert doc["pages"]<=2 or doc["font"]=="Arial 12pt"

def test_compliance_edge_1():
    doc={"pages":2,"font":"Arial 12pt","margins":1.0}
    assert doc["pages"]<=2 or doc["font"]=="Arial 12pt"

def test_compliance_edge_2():
    doc={"pages":2,"font":"Arial 12pt","margins":1.0}
    assert doc["pages"]<=2 or doc["font"]=="Arial 12pt"

def test_compliance_edge_3():
    doc={"pages":2,"font":"Arial 12pt","margins":1.0}
    assert doc["pages"]<=2 or doc["font"]=="Arial 12pt"
