import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
 
class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(410)

    def test_kassan_koko_alussa_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisten_maara_alussa_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukkaiden_maara_alussa_oikein(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    #testataan kateismaksua

    #edulliset
    def test_syo_edullisesti_kateisella_kasvattaa_kassaa(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_kasvattaa_myytyja_lounaita(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_syo_edullisesti_antaa_vaihtorahan(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihtoraha, 10)

    def test_syo_edullisesti_palauttaa_rahat_jos_raha_ei_riita(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(220)
        self.assertEqual(vaihtoraha, 220)

    def test_syo_edullisesti_ei_kasvata_lounaiden_maaraa_jos_ei_rahaa(self):
        self.kassa.syo_edullisesti_kateisella(220)
        self.assertEqual(self.kassa.edulliset, 0)

    #maukkaat
    def test_syo_maukkaasti_kateisella_kasvattaa_kassaa(self):
        self.kassa.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_kasvattaa_myytyja_lounaita(self):
        self.kassa.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_syo_maukkaasti_antaa_vaihtorahan(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(410)
        self.assertEqual(vaihtoraha, 10)

    def test_syo_maukkaasti_palauttaa_rahat_jos_raha_ei_riita(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(220)
        self.assertEqual(vaihtoraha, 220)

    def test_syo_maukkaasti_ei_kasvata_lounaiden_maaraa_jos_ei_rahaa(self):
        self.kassa.syo_maukkaasti_kateisella(220)
        self.assertEqual(self.kassa.edulliset, 0)

    #testataan korttimaksua

    def test_kortille_voi_ladata_positiivisen_summan_rahaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(str(self.kortti), "saldo: 14.1")

    def test_kortille_ei_voi_ladata_negatiivista_summaa_rahaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -400)
        self.assertEqual(str(self.kortti), "saldo: 4.1")

    #edulliset
    def test_syo_edullisesti_kortilla_kasvattaa_myytyja_lounaita(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_syo_edullisesti_kortilla_veloittaa_summan_kortilta_jos_rahaa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 1.7")

    def test_syo_edullisesti_kortilla_palauttaa_onnistuessaan_true(self):
        palautus = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(palautus)

    def test_syo_edullisesti_kortilla_ei_kasvata_myytyja_lounaita_jos_raha_ei_riita(self):
        for i in range(2):
            self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_syo_edullisesti_kortilla_ei_muuta_kortin_saldoa_jos_raha_ei_riita(self):
        for i in range(2):
            self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 1.7")

    def test_syo_edullisesti_kortilla_palauttaa_false_jos_raha_ei_riita(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        palautus = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertFalse(palautus)

    #maukkaat
    def test_syo_maukkaasti_kortilla_kasvattaa_myytyja_lounaita(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_veloittaa_summan_kortilta_jos_rahaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 0.1")

    def test_syo_maukkaasti_kortilla_palauttaa_onnistuessaan_true(self):
        palautus = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(palautus)

    def test_syo_maukkaasti_kortilla_ei_kasvata_myytyja_lounaita_jos_raha_ei_riita(self):
        for i in range(2):
            self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_ei_muuta_kortin_saldoa_jos_raha_ei_riita(self):
        for i in range(2):
            self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 0.1")

    def test_syo_maukkaasti_kortilla_palauttaa_false_jos_raha_ei_riita(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        palautus = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertFalse(palautus)

    def test_kassan_rahamaara_ei_muutu_kortilla_maksaessa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)