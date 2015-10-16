from nose.tools import *
from ex48.ex48 import *

def test_sentence():
    s = Sentence(('noun', 'prince'), ('verb', 'go'), ('noun','cinema'))
    assert_equal(s.subject, 'prince')
    assert_equal(s.verb, 'go')
    assert_equal(s.obj, 'cinema')

def test_peek():
    assert_equal(peek(['I', 'like', 'chocolate']), 'I')
    assert_equal(peek([]), None)

def test_match():
    assert_equal(match([('noun', 'bear'), ('verb', 'eats'), ('noun', 'honey')], 'noun'), ('noun', 'bear'))
    assert_equal(match([('verb', 'eats'), ('noun', 'honey')], 'noun'), None)

def test_skip():
    l = [('stop', 'the'), ('noun', 'bear'), ('verb', 'eats'), ('noun', 'honey')]
    skip(l, 'stop')
    assert_equal(l , [('noun', 'bear'), ('verb', 'eats'), ('noun', 'honey')])

def test_parse_verb():
    v = parse_verb([('stop', 'the'), ('verb', 'eats'), ('noun', 'honey')])
    print('***')
    assert_equal(v, ('verb', 'eats'))

    assert_raises(ParserError, parse_verb, [('noun', 'bear'), ('noun', 'honey')])


def test_parse_obj():
    o = parse_obj([('stop', 'the'), ('noun', 'honey')])
    assert_equal(o, ('noun', 'honey'))

    o = parse_obj([('stop', 'the'), ('direction', 'north')])
    assert_equal(o, ('direction', 'north'))

    assert_raises(ParserError, parse_obj, [('verb', 'eats')])

def test_parse_subject():
    s = parse_subject([('verb', 'eats'), ('noun', 'honey')], ('noun', 'bear'))
    assert_equal(s, Sentence(('noun', 'bear'), ('verb', 'eats'), ('noun', 'honey')))

def test_parse_sentence():
    wl = [('noun', 'bear'), ('verb', 'eats'), ('noun', 'honey')]
    s = parse_sentence(wl)
    assert_equal(s, Sentence('bear', 'eats', 'honey'))
    wl = [('verb', 'eats'), ('noun', 'honey')]
    s = parse_sentence(wl)
    assert_equal(s, Sentence('Player', 'eats', 'honey'))
    wl = [('other', 'azerty')]
    assert_raises(ParseError, parse_sentence, wl)

