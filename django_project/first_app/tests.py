from django.test import TestCase


# Create your tests here.
class ExampleTestCase(TestCase):

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    def test_example(self):
        self.assertEqual(True, True)
