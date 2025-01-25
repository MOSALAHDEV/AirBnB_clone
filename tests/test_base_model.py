import unittest
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Test creation of BaseModel class """
    def test_base_model(self):
        """ Test creation of BaseModel class """
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertEqual(type(bm.created_at), datetime)
        self.assertEqual(type(bm.updated_at), datetime)
        self.assertEqual(type(bm.to_dict()), dict)
    def test_save(self):
        """ Test save method """
        bm = BaseModel()
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)
        self.assertEqual(type(bm.created_at), datetime)
    
    def test_to_dict(self):
        """ Test to_dict method """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(type(bm_dict['created_at']), str)
        self.assertEqual(type(bm_dict['updated_at']), str)
        self.assertEqual(type(bm_dict), dict)
    
    def test_init_args_kwargs(self):
        """ Test init method with args and kwargs """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        bm2 = BaseModel(**bm_dict)
        self.assertEqual(bm2.id, bm.id)
        self.assertEqual(bm2.created_at, bm.created_at)
        self.assertEqual(bm2.updated_at, bm.updated_at)
        self.assertEqual(bm2.to_dict(), bm_dict)

        def test_str(self):
            """ Test __str__ method """
            bm = BaseModel()
            bm_str = str(bm)
            self.assertEqual(bm_str, f"[{bm.__class__.__name__}] ({bm.id}) {bm.__dict__}")
    if __name__ == '__main__':
        unittest.main()
