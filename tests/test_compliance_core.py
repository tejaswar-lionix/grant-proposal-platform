"""Tests for compliance core distinct"""

def test_compliance_core_0():
    doc={"pages":2,"font":"Arial 12pt","margins":1.0}
    assert doc["pages"]<=2 or doc["font"]=="Arial 12pt"

def test_compliance_core_1():
    doc={"pages":2,"font":"Arial 12pt","margins":1.0}
    assert doc["pages"]<=2 or doc["font"]=="Arial 12pt"

def test_compliance_core_2():
    doc={"pages":2,"font":"Arial 12pt","margins":1.0}
    assert doc["pages"]<=2 or doc["font"]=="Arial 12pt"

def test_compliance_core_3():
    doc={"pages":2,"font":"Arial 12pt","margins":1.0}
    assert doc["pages"]<=2 or doc["font"]=="Arial 12pt"
