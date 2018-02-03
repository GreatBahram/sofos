"""Module test_dategr"""
import unittest
import sys
from PyQt5.QtTest import QTest
import PyQt5.QtCore as Qc
import PyQt5.QtGui as Qg
import PyQt5.QtWidgets as Qw
from sofos import qt

app = Qw.QApplication(sys.argv)


class Tests(unittest.TestCase):

    def setUp(self):
        self.chkbox = qt.TCheckbox()
        self.date = qt.TDate()

    def test_TCheckbox_01(self):
        self.assertEqual(self.chkbox.get(), 0)

    def test_TCheckbox_02(self):
        self.chkbox.set(1)
        self.assertEqual(self.chkbox.get(), 2)

    def test_TDate_01(self):
        self.date.set('2017-01-13')
        self.assertEqual(self.date.get(), '2017-01-13')
