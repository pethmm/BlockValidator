# test_blockvalidator.py
"""
Tests for BlockValidator module.
"""

import unittest
from blockvalidator import BlockValidator

class TestBlockValidator(unittest.TestCase):
    """Test cases for BlockValidator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockValidator()
        self.assertIsInstance(instance, BlockValidator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockValidator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
