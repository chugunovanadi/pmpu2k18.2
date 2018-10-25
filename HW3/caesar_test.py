from unittest import TestCase, main
from HW3.caesar_logic import encrypt, decrypt


class Tester(TestCase):
    def test_true_encrypt_1(self):
        self.assertEqual(encrypt(3, 'Hello world'), 'Khoor zruog')

    def test_true_encrypt_2(self):
        self.assertEqual(encrypt(-5, 'Moyu konus v vannoy'), 'Hjtp fjipn q qviijt')

    def test_true_encrypt_3(self):
        self.assertEqual(encrypt(25, 'Vylivayu vino v rakovinu'), 'Uxkhuzxt uhmn u qzjnuhmt')

    def test_true_encrypt_4(self):
        self.assertEqual(encrypt(0, 'With Halloween'), 'With Halloween')

    def test_true_encrypt_5(self):
        self.assertEqual(encrypt(6, '(,,,)=(^.^)=(,,,)'), '(,,,)=(^.^)=(,,,)')

    def test_true_encrypt_6(self):
        self.assertEqual(encrypt(7, 'PoStAvtE zachet AVTOMATOM'), 'WvZaHcaL ghjola HCAVTHAVT')

    def test_true_encrypt_7(self):
        self.assertEqual(encrypt(5, 'WYXZZZZZwyxzzzzz'), 'BDCEEEEEbdceeeee')

    def test_true_decrypt_1(self):
        self.assertEqual(decrypt(3, 'Khoor zruog'), 'Hello world')

    def test_true_decrypt_2(self):
        self.assertEqual(decrypt(-5, 'Hjtp fjipn q qviijt'), 'Moyu konus v vannoy')

    def test_true_decrypt_3(self):
        self.assertEqual(decrypt(25, 'Uxkhuzxt uhmn u qzjnuhmt'), 'Vylivayu vino v rakovinu')

    def test_true_decrypt_4(self):
        self.assertEqual(decrypt(0, 'With Halloween'), 'With Halloween')

    def test_true_decrypt_5(self):
        self.assertEqual(decrypt(6, '(,,,)=(^.^)=(,,,)'), '(,,,)=(^.^)=(,,,)')

    def test_true_decrypt_6(self):
        self.assertEqual(decrypt(7, 'WvZaHcaL ghjola HCAVTHAVT'), 'PoStAvtE zachet AVTOMATOM')

    def test_true_decrypt_7(self):
        self.assertEqual(decrypt(5, 'BDCEEEEEbdceeeeeee'), 'WYXZZZZZwyxzzzzzzz')


main()
