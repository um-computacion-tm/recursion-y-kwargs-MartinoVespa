import unittest

from kwargs import buscar_datos

class testkwargs(unittest.TestCase):
    
    def setUp(self):
        
        self.database = {

        "persona1": {
            "primer_nombre": "Pablo",
            "segundo_nombre": "Diego",
            "primer_apellido": "Ruiz",
            "segundo_apellido": "Picasso"
        },

        "persona2" : {
            "primer_nombre": "Martino",
            "segundo_nombre": "Agustin",
            "primer_apellido": "Vespa",
            "segundo_apellido": "Stacchiola"  
     }

        }

def test_datos_encontrados(self):

    resultado = buscar_datos("Pablo", "Martino", database=self.database)
    self.assertEqual(resultado, ["Pablo", "Martino"])

def test_datos_no_encontrados(self):

    resultado = buscar_datos("Avellaneda", "Luserfforn", database=self.database)

    self.assertEqual(resultado, [])

def test_datos_mezclados(self):

    resultado = buscar_datos("Pablo", "Lusserfforn", "Martino", database=self.database)

    self.assertEqual(resultado, ["Pablo", "Martino"])

unittest.main()
