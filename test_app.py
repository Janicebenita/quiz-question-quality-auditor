import unittest
from app import audit_question
class Tests(unittest.TestCase):
    def test_duplicate_and_bad_answer(self):
        issues=audit_question({"prompt":"A reasonable question?","options":["A","A","B"],"answer":"C"})["issues"];self.assertIn("duplicate-options",issues);self.assertIn("answer-not-in-options",issues)
    def test_valid_structure_passes(self): self.assertEqual(audit_question({"prompt":"Which item matches the documented rule?","options":["A","B","C"],"answer":"A"})["status"],"pass")
if __name__=="__main__":unittest.main()
