
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BINARY BOOLEAN CHAVETAABERTO CHAVETAFECHO DATE DATETIME END EQUALS EXPONENTE FLOAT HEXADECIMAL INFINITO INT KEY MULTILINESTRING NAN OCTAL OFFSETDATETIME PARENTESERETOABERTO PARENTESERETOFECHO PONTO STRING TIME VIRGULAcodigo : codigo : codigo ENDcodigo : codigo blococonteudo : String\n                | TIME\n                | DATE\n                | OFFSETDATETIME\n                | DATETIME\n                | BOOLEAN\n                | BINARY\n                | OCTAL\n                | HEXADECIMAL\n                | INT\n                | FLOAT\n                | EXPONENTE\n                | INFINITO\n                | NAN\n                | lista\n                | inline_tableString : STRING\n              | MULTILINESTRINGlista : PARENTESERETOABERTO elems PARENTESERETOFECHO\n             | PARENTESERETOABERTO PARENTESERETOFECHOelems : elems VIRGULA conteudo\n           | conteudocodigo : codigo PARENTESERETOABERTO chaves PARENTESERETOFECHO bloco\n              | codigo PARENTESERETOABERTO chaves PARENTESERETOFECHOchaves : KEY PONTO KEY\n              | KEYbloco : bloco KEY EQUALS conteudo\n             | KEY EQUALS conteudoinline_table :  CHAVETAABERTO insideTable CHAVETAFECHOinsideTable : insideTable VIRGULA bloco\n                   | bloco'
    
_lr_action_items = {'END':([0,1,2,3,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,38,42,44,],[-1,2,-2,-3,-27,-31,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-30,-26,-23,-22,-32,]),'PARENTESERETOABERTO':([0,1,2,3,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,38,42,43,44,],[-1,4,-2,-3,32,32,-27,-31,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,32,-30,-26,-23,-22,32,-32,]),'KEY':([0,1,2,3,4,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,38,41,42,44,45,47,],[-1,5,-2,6,8,5,36,-31,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,5,-30,6,-23,6,-22,-32,5,6,]),'$end':([0,1,2,3,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,38,42,44,],[-1,0,-2,-3,-27,-31,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-30,-26,-23,-22,-32,]),'EQUALS':([5,6,],[9,10,]),'PARENTESERETOFECHO':([7,8,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,36,37,38,39,42,44,46,],[11,-29,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,38,-28,42,-23,-25,-22,-32,-24,]),'PONTO':([8,],[12,]),'TIME':([9,10,32,43,],[15,15,15,15,]),'DATE':([9,10,32,43,],[16,16,16,16,]),'OFFSETDATETIME':([9,10,32,43,],[17,17,17,17,]),'DATETIME':([9,10,32,43,],[18,18,18,18,]),'BOOLEAN':([9,10,32,43,],[19,19,19,19,]),'BINARY':([9,10,32,43,],[20,20,20,20,]),'OCTAL':([9,10,32,43,],[21,21,21,21,]),'HEXADECIMAL':([9,10,32,43,],[22,22,22,22,]),'INT':([9,10,32,43,],[23,23,23,23,]),'FLOAT':([9,10,32,43,],[24,24,24,24,]),'EXPONENTE':([9,10,32,43,],[25,25,25,25,]),'INFINITO':([9,10,32,43,],[26,26,26,26,]),'NAN':([9,10,32,43,],[27,27,27,27,]),'STRING':([9,10,32,43,],[30,30,30,30,]),'MULTILINESTRING':([9,10,32,43,],[31,31,31,31,]),'CHAVETAABERTO':([9,10,32,43,],[33,33,33,33,]),'CHAVETAFECHO':([13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,38,40,41,42,44,47,],[-31,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-30,-23,44,-34,-22,-32,-33,]),'VIRGULA':([13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,37,38,39,40,41,42,44,46,47,],[-31,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-30,43,-23,-25,45,-34,-22,-32,-24,-33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,],[1,]),'bloco':([1,11,33,45,],[3,35,41,47,]),'chaves':([4,],[7,]),'conteudo':([9,10,32,43,],[13,34,39,46,]),'String':([9,10,32,43,],[14,14,14,14,]),'lista':([9,10,32,43,],[28,28,28,28,]),'inline_table':([9,10,32,43,],[29,29,29,29,]),'elems':([32,],[37,]),'insideTable':([33,],[40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> <empty>','codigo',0,'p_codigo_empty','yacc.py',10),
  ('codigo -> codigo END','codigo',2,'p_codigo_ending','yacc.py',15),
  ('codigo -> codigo bloco','codigo',2,'p_codigo_start','yacc.py',20),
  ('conteudo -> String','conteudo',1,'p_conteudo','yacc.py',26),
  ('conteudo -> TIME','conteudo',1,'p_conteudo','yacc.py',27),
  ('conteudo -> DATE','conteudo',1,'p_conteudo','yacc.py',28),
  ('conteudo -> OFFSETDATETIME','conteudo',1,'p_conteudo','yacc.py',29),
  ('conteudo -> DATETIME','conteudo',1,'p_conteudo','yacc.py',30),
  ('conteudo -> BOOLEAN','conteudo',1,'p_conteudo','yacc.py',31),
  ('conteudo -> BINARY','conteudo',1,'p_conteudo','yacc.py',32),
  ('conteudo -> OCTAL','conteudo',1,'p_conteudo','yacc.py',33),
  ('conteudo -> HEXADECIMAL','conteudo',1,'p_conteudo','yacc.py',34),
  ('conteudo -> INT','conteudo',1,'p_conteudo','yacc.py',35),
  ('conteudo -> FLOAT','conteudo',1,'p_conteudo','yacc.py',36),
  ('conteudo -> EXPONENTE','conteudo',1,'p_conteudo','yacc.py',37),
  ('conteudo -> INFINITO','conteudo',1,'p_conteudo','yacc.py',38),
  ('conteudo -> NAN','conteudo',1,'p_conteudo','yacc.py',39),
  ('conteudo -> lista','conteudo',1,'p_conteudo','yacc.py',40),
  ('conteudo -> inline_table','conteudo',1,'p_conteudo','yacc.py',41),
  ('String -> STRING','String',1,'p_String','yacc.py',46),
  ('String -> MULTILINESTRING','String',1,'p_String','yacc.py',47),
  ('lista -> PARENTESERETOABERTO elems PARENTESERETOFECHO','lista',3,'p_lista','yacc.py',51),
  ('lista -> PARENTESERETOABERTO PARENTESERETOFECHO','lista',2,'p_lista','yacc.py',52),
  ('elems -> elems VIRGULA conteudo','elems',3,'p_elems','yacc.py',60),
  ('elems -> conteudo','elems',1,'p_elems','yacc.py',61),
  ('codigo -> codigo PARENTESERETOABERTO chaves PARENTESERETOFECHO bloco','codigo',5,'p_codigo_newobject','yacc.py',71),
  ('codigo -> codigo PARENTESERETOABERTO chaves PARENTESERETOFECHO','codigo',4,'p_codigo_newobject','yacc.py',72),
  ('chaves -> KEY PONTO KEY','chaves',3,'p_chaves','yacc.py',87),
  ('chaves -> KEY','chaves',1,'p_chaves','yacc.py',88),
  ('bloco -> bloco KEY EQUALS conteudo','bloco',4,'p_bloco_conteudo','yacc.py',97),
  ('bloco -> KEY EQUALS conteudo','bloco',3,'p_bloco_conteudo','yacc.py',98),
  ('inline_table -> CHAVETAABERTO insideTable CHAVETAFECHO','inline_table',3,'p_inline_table','yacc.py',110),
  ('insideTable -> insideTable VIRGULA bloco','insideTable',3,'p_insideTable','yacc.py',114),
  ('insideTable -> bloco','insideTable',1,'p_insideTable','yacc.py',115),
]
