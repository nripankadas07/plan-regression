import unittest
from plan_regression import compare
class Tests(unittest.TestCase):
 def test_ratio_and_delta(self):
  a={'Node Type':'Seq Scan','Total Cost':100};b={**a,'Total Cost':130};self.assertEqual(len(compare(a,b)['regressions']),1);self.assertFalse(compare(a,b,minimum_delta=40)['regressions'])
 def test_changed_operator_not_mispaired(self):
  x=compare({'Node Type':'Seq Scan','Total Cost':1},{'Node Type':'Index Scan','Total Cost':999});self.assertTrue(x['structural_changes']);self.assertFalse(x['regressions'])
 def test_child_and_zero_baseline(self):
  x=compare({'Node Type':'Sort','Plans':[{'Node Type':'Seq Scan','Plan Rows':0}]},{'Node Type':'Sort','Plans':[{'Node Type':'Seq Scan','Plan Rows':10}]});self.assertEqual(x['regressions'][0]['path'],'root/0');self.assertIsNone(x['regressions'][0]['ratio'])
 def test_nonfinite_rejected(self):
  with self.assertRaises(ValueError):compare({'Node Type':'Scan','Total Cost':float('nan')},{'Node Type':'Scan'})
 def test_no_runtime_claim_from_cost(self):
  x=compare({'Node Type':'Scan','Total Cost':10},{'Node Type':'Scan','Total Cost':20});self.assertEqual(x['regressions'][0]['metric'],'Total Cost')
