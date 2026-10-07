import decimal,unittest
import unitunau as u
class UnitTests(unittest.TestCase):
    def test_m_km(self):self.assertEqual(decimal.Decimal(u.convert('1000','m','km')),1)
    def test_cm_mm(self):self.assertEqual(decimal.Decimal(u.convert('2.5','cm','mm')),25)
    def test_kg_g(self):self.assertEqual(decimal.Decimal(u.convert('1','kg','g')),1000)
    def test_mg_kg(self):self.assertEqual(decimal.Decimal(u.convert('1','mg','kg')),decimal.Decimal('0.000001'))
    def test_c_f(self):self.assertEqual(decimal.Decimal(u.convert('0','C','F')),32)
    def test_f_c(self):self.assertEqual(decimal.Decimal(u.convert('212','F','C')),100)
    def test_c_k(self):self.assertEqual(decimal.Decimal(u.convert('0','C','K')),decimal.Decimal('273.15'))
    def test_zero_k(self):self.assertEqual(decimal.Decimal(u.convert('0','K','C')),decimal.Decimal('-273.15'))
    def test_below_zero(self):
        with self.assertRaises(ValueError):u.convert('-1','K','C')
    def test_negative_mass(self):
        with self.assertRaises(ValueError):u.convert('-1','kg','g')
    def test_mixed(self):
        with self.assertRaises(ValueError):u.convert('1','m','g')
    def test_bad_unit(self):
        with self.assertRaises(ValueError):u.convert('1','oz','g')
    def test_bad_numbers(self):
        for v in ('NaN','Infinity','1e3','١','1.','.'+'1'*30):
            with self.assertRaises(ValueError):u.number(v)
    def test_bounds(self):
        with self.assertRaises(ValueError):u.number('1'*16)
    def test_same(self):self.assertEqual(decimal.Decimal(u.convert('2.5','m','m')),decimal.Decimal('2.5'))
    def test_context_unchanged(self):old=decimal.getcontext().prec;u.convert('1','F','C');self.assertEqual(decimal.getcontext().prec,old)
if __name__=='__main__':unittest.main()
