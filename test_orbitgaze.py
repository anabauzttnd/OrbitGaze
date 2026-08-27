# test_orbitgaze.py
"""
Tests for OrbitGaze module.
"""

import unittest
from orbitgaze import OrbitGaze

class TestOrbitGaze(unittest.TestCase):
    """Test cases for OrbitGaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OrbitGaze()
        self.assertIsInstance(instance, OrbitGaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OrbitGaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
