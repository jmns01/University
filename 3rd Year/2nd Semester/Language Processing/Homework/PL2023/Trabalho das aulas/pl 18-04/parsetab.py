
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CLOSEPAREN NULL NUM OPENPARENABin : NULLABin : Raiz OPENPAREN ABin ABin CLOSEPARENRaiz : NUM'
    
_lr_action_items = {'NULL':([0,2,5,6,8,],[2,-1,2,2,-2,]),'NUM':([0,2,5,6,8,],[4,-1,4,4,-2,]),'$end':([1,2,8,],[0,-1,-2,]),'CLOSEPAREN':([2,7,8,],[-1,8,-2,]),'OPENPAREN':([3,4,],[5,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ABin':([0,5,6,],[1,6,7,]),'Raiz':([0,5,6,],[3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ABin","S'",1,None,None,None),
  ('ABin -> NULL','ABin',1,'p_abin_vazia','abin_yacc.py',6),
  ('ABin -> Raiz OPENPAREN ABin ABin CLOSEPAREN','ABin',5,'p_abin','abin_yacc.py',11),
  ('Raiz -> NUM','Raiz',1,'p_raiz','abin_yacc.py',16),
]
