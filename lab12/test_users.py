import pytest
def identity(person):return person.id if hasattr(person,'id') else person['id']
@pytest.mark.parametrize('age',[1,100])
@pytest.mark.parametrize('name',['AA','АААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА'])
def test_edges(registry,age,name):assert registry.add(name,age,'edge@example.com') is not None
@pytest.mark.parametrize('name,age,email',[
    ('X',25,'x@example.com'),('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',25,'x@example.com'),
    ('Valid Name',0,'x@example.com'),('Valid Name',101,'x@example.com'),
    ('Valid Name',True,'x@example.com'),('Name123',25,'x@example.com'),
    ('Valid Name',25,'invalid')])
def test_rejection(registry,name,age,email):
    with pytest.raises(ValueError):registry.add(name,age,email)
    assert registry.all()==[]
def test_operations(registry):
    person=registry.add('Valid Name',25,'valid@example.com');key=identity(person)
    assert registry.get(key)==person and registry.find('VALID@EXAMPLE.COM')==person
    assert registry.delete(key) and registry.get(key) is None
    assert not registry.delete(key)
def test_duplicate(seeded):
    with pytest.raises(ValueError,match='duplicate'):seeded.add('Another Person',30,'ANNA@EXAMPLE.COM')
    assert len(seeded.all())==2
def test_missing(seeded):assert seeded.get(999) is None and seeded.find('missing@example.com') is None
def test_generated(registry,datasets):
    for row in datasets:
        person=registry.add(**row)
        assert registry.get(identity(person))==person
    assert len(registry.all())==75
