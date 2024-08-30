import unittest
import test_12_3

tournement_TS = unittest.TestSuite()
tournement_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
tournement_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournement_TS)