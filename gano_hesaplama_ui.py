from PyQt5 import QtCore, QtWidgets


class DersWidget(QtWidgets.QWidget):
    """Her ders için vize/final/kredi giriş alanlarını tutan küçük bir widget"""

    def __init__(self, index):
        super().__init__()
        self.index = index

        layout = QtWidgets.QHBoxLayout()

        self.vize = QtWidgets.QLineEdit()
        self.vize.setPlaceholderText("Vize")

        self.final = QtWidgets.QLineEdit()
        self.final.setPlaceholderText("Final")

        self.kredi = QtWidgets.QLineEdit()
        self.kredi.setPlaceholderText("Kredi")

        # Vize yüzdesi seçimi
        self.combo = QtWidgets.QComboBox()
        self.combo.addItems(["40%", "30%", "20%"])

        layout.addWidget(QtWidgets.QLabel(f"Ders {index+1}:"))
        layout.addWidget(self.vize)
        layout.addWidget(self.final)
        layout.addWidget(self.kredi)
        layout.addWidget(self.combo)

        self.setLayout(layout)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)

        # ---- DERS SAYISI SEÇİMİ ----
        self.spinDersSayisi = QtWidgets.QSpinBox()
        self.spinDersSayisi.setMinimum(1)
        self.spinDersSayisi.setMaximum(15)
        self.spinDersSayisi.setValue(3)

        self.btnOlustur = QtWidgets.QPushButton("Ders Alanlarını Oluştur")
        self.btnOlustur.clicked.connect(self.dersleri_olustur)

        self.verticalLayout.addWidget(QtWidgets.QLabel("Ders Sayısı Seç:"))
        self.verticalLayout.addWidget(self.spinDersSayisi)
        self.verticalLayout.addWidget(self.btnOlustur)

        # Ders alanları burada oluşacak
        self.dersContainer = QtWidgets.QVBoxLayout()
        self.verticalLayout.addLayout(self.dersContainer)

        # Hesapla butonu
        self.btnHesapla = QtWidgets.QPushButton("GENEL ORTALAMAYI HESAPLA")
        self.btnHesapla.clicked.connect(self.hesapla)
        self.verticalLayout.addWidget(self.btnHesapla)

        # Sonuç label
        self.labelSonuc = QtWidgets.QLabel("")
        self.verticalLayout.addWidget(self.labelSonuc)

        # İlk yüklemede ders alanlarını oluştur
        self.dersleri_olustur()

    # -----------------------------------------------------------------------
    def dersleri_olustur(self):
        """Ders sayısına göre giriş alanlarını oluşturur"""
        # Önce eski widgetları sil
        while self.dersContainer.count():
            item = self.dersContainer.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.dersler = []
        ders_sayisi = self.spinDersSayisi.value()

        for i in range(ders_sayisi):
            dersWidget = DersWidget(i)
            self.dersContainer.addWidget(dersWidget)
            self.dersler.append(dersWidget)

    # -----------------------------------------------------------------------
    def hesapla(self):
        toplam_not = 0
        toplam_kredi = 0

        for d in self.dersler:
            try:
                vize = float(d.vize.text())
                final = float(d.final.text())
                kredi = float(d.kredi.text())
                yuzde_vize = int(d.combo.currentText().replace("%", ""))
                yuzde_final = 100 - yuzde_vize

                ders_notu = vize * (yuzde_vize / 100) + final * (yuzde_final / 100)

                toplam_not += ders_notu * kredi
                toplam_kredi += kredi

            except:
                self.labelSonuc.setText("Hata: Lütfen tüm derslere geçerli değer girin!")
                return

        if toplam_kredi == 0:
            self.labelSonuc.setText("Hata: Kredi 0 olamaz!")
            return

        gano = toplam_not / toplam_kredi
        self.labelSonuc.setText(f"GENEL ORTALAMA (GANO): {gano:.2f}")

# -----------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
