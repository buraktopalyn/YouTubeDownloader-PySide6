# İMPORTLAR
from PySide6.QtCore import Qt
from PySide6 import QtGui
from PySide6 import *
from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QFileDialog
from pathlib import Path
from pytube import YouTube
from datetime import datetime
import requests
from moviepy.editor import *
import csv
import sys
import cv2
import locale
# Qt Designer arayüzü import etme
from ui_mainFrame import *  

# Konum Ayarı
locale.setlocale(locale.LC_ALL, "")



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint) # pencere başlığını kaldır
        self.setAttribute(Qt.WA_TranslucentBackground); # şeffaf pencere
        self.setWindowIcon(QIcon("icons/icons8_video_playlist_48px.png"))  # logo
        self.setWindowTitle("Downlaoder")
        self.setFont(QFont("fonts/Bulletproof", 14))
        QtGui.QFontDatabase.addApplicationFont("fonts/Bulletproof.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts/Comfortaa-Bold.ttf")
        self.setStyleSheet("font-family: Comfortaa;")
        self.ui.title.setStyleSheet("font-family: Bulletproof;")

        self.videoFunctions()
        self.musicFunctions()
        self.transformFunctions()
        self.historyFunctions()
        self.settingsFunctions()
        

        # pencereyi hareket ettirme
        def moveWindow(e):
            if self.isMaximized() == False: # pencere tam ekran değilse
                if e.buttons() == Qt.LeftButton: # sol butona tıklama olduğunda
                    # hareket ettirme
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        # hareket ettirmek için frame e fonksiyon atama
        self.ui.movewindow.mouseMoveEvent = moveWindow

        ### __INIT__ SONU ###


    ### GEÇMİŞ

    def historyFunctions(self):
        self.ui.clearh.clicked.connect(lambda: self.delHistory())

    def delHistory(self):
        with open("history.csv", "w") as f:
            self.ui.clearh.setEnabled(False)
            self.ui.past.setText("Geçmiş temizlendi.")
            self.ui.clearh.setText("Temizle")
            self.ui.abouth.setText("Uygulama Geçmişi")


    ### AYARLAR

    def settingsFunctions(self):
        self.ui.tur.clicked.connect(lambda: self.setTur())
        self.ui.eng.clicked.connect(lambda: self.setEng())

        self.ui.white.clicked.connect(lambda: self.setWhite())
        self.ui.blue.clicked.connect(lambda: self.setBlue())
        self.ui.red.clicked.connect(lambda: self.setRed())
        self.ui.green.clicked.connect(lambda: self.setGreen())

    def setTur(self):
        self.ui.tur.setEnabled(False)
        self.ui.eng.setChecked(False)
        self.ui.eng.setEnabled(True)

    def setEng(self):
        self.ui.eng.setEnabled(False)
        self.ui.tur.setChecked(False)
        self.ui.tur.setEnabled(True)

    def setWhite(self):
        self.ui.white.setEnabled(False)
        self.ui.blue.setChecked(False)
        self.ui.blue.setEnabled(True)
        self.ui.red.setChecked(False)
        self.ui.red.setEnabled(True)
        self.ui.green.setChecked(False)
        self.ui.green.setEnabled(True)

    def setBlue(self):
        self.ui.blue.setEnabled(False)
        self.ui.white.setChecked(False)
        self.ui.white.setEnabled(True)
        self.ui.red.setChecked(False)
        self.ui.red.setEnabled(True)
        self.ui.green.setChecked(False)
        self.ui.green.setEnabled(True)

    def setRed(self):
        self.ui.red.setEnabled(False)
        self.ui.white.setChecked(False)
        self.ui.white.setEnabled(True)
        self.ui.blue.setChecked(False)
        self.ui.blue.setEnabled(True)
        self.ui.green.setChecked(False)
        self.ui.green.setEnabled(True)

    def setGreen(self):
        self.ui.green.setEnabled(False)
        self.ui.white.setChecked(False)
        self.ui.white.setEnabled(True)
        self.ui.blue.setChecked(False)
        self.ui.blue.setEnabled(True)
        self.ui.red.setChecked(False)
        self.ui.red.setEnabled(True)


    ### DÖNÜŞTÜR

    def transformFunctions(self):
        self.ui.selectvideo.clicked.connect(lambda: self.selectVideo())
        self.ui.selectmusic.clicked.connect(lambda: self.selectMusic())
        self.ui.downloadbtn_3.clicked.connect(lambda: self.transformVideo())
        self.musicpath = str(Path.home() / "Downloads")

    def selectVideo(self):
        dialog = QFileDialog()
        self.videopath = dialog.getOpenFileName(self, "Video Seçin")
        if self.videopath[0] == "":
            self.ui.selectvideo.setText("Video Seçilmedi")
        elif self.videopath[0][-3:] != "mp4":
            self.ui.selectvideo.setText("Sadece Video Seçebilirsiniz")
        else:
            try: 
                btntxt = self.videopath[0].split("/")
                self.ui.selectvideo.setText(btntxt[-1])
                self.ui.selectvideo.setChecked(True)
                self.ui.selectmusic.setEnabled(True)
                videosize = os.path.getsize(self.videopath[0])
                self.ui.sizebtn_3.setText(f"{videosize/(1024*1024):.1f} MB")
                self.videoname = btntxt[-1].replace(" ", "_")
                self.ui.bartxt_3.setText("Dönüştürmeye Hazır")
                #video fotoğrafı al
                cap = cv2.VideoCapture(self.videopath[0])
                num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                middle_frame_idx = num_frames // 2
                cap.set(cv2.CAP_PROP_POS_FRAMES, middle_frame_idx)
                ret, frame = cap.read()
                cv2.imwrite('images/smallth.jpg', frame)
                self.ui.videophoto.setStyleSheet(u"""#videophoto { 
                    border-image: url(images/smallth.jpg);
                    border: 2px solid #282828;
                    border-radius: 5px;
                    background-color: #181818;
                    }""")
                self.ui.downloadbtn_3.setEnabled(True)
                self.musicname = self.videoname[:-4]+".mp3"
            except:
                self.ui.bartxt_3.setStyleSheet("color: red;")
                self.ui.bartxt_3.setText("Bir Hata Oluştu")

    def selectMusic(self):
        dialog = QFileDialog()
        self.musicpath = dialog.getExistingDirectory(self, 'Ses Kaydetme Yeri Seçin')
        if self.musicpath == "":
            self.musicpath = str(Path.home() / "Downloads")
            self.ui.btnpath_2.setText("/Downloads")
        else:
            btntxt = self.musicpath.split("/")
            self.ui.selectmusic.setText(f"/{btntxt[-1]}")
            self.ui.selectmusic.setChecked(True)
            self.ui.downloadbtn_3.setEnabled(True)

    def transformVideo(self):
        self.ui.main.setEnabled(False)
        try: 
            startdown = datetime.now()
            video = VideoFileClip(self.videopath[0])
            savepath = self.musicpath+"\\"+self.musicname
            audio = video.audio
            audio.write_audiofile(savepath)

            enddown = datetime.now()
            process = str((enddown-startdown).seconds)

            self.progressanimation = QPropertyAnimation(self.ui.progressBar_3, b"value")
            self.progressanimation.setDuration(2000)
            self.progressanimation.setStartValue(0)
            self.progressanimation.setEndValue(100)
            self.progressanimation.setEasingCurve(QtCore.QEasingCurve.OutInQuint)
            self.progressanimation.start()

            trdate = datetime.now().strftime("%c")

            with open("history.csv", "a", encoding="utf-8") as wf:
                writeon = csv.writer(wf, delimiter=",", quotechar=',', quoting=csv.QUOTE_MINIMAL)
                writeon.writerow(['transform', self.ui.sizebtn_3.text(), self.videoname, trdate])

            self.ui.bartxt_3.setStyleSheet("color: #ccc;")
            self.ui.bartxt_3.setText(f"Dönüştürüldü ({process} sn)")
        except:
            self.ui.bartxt_3.setStyleSheet("color: red;")
            self.ui.bartxt_3.setText("Bir Hata Oluştu")
        self.ui.main.setEnabled(True)


    ### MÜZİK

    def musicFunctions(self):
        # muzik bul
        self.ui.searchbtn_2.clicked.connect(lambda: self.findMusic(self.ui.searchtxt_2.text()))
        self.mpath = str(Path.home() / "Downloads")
        self.ui.btnpath_2.clicked.connect(lambda: self.setmPath())
        self.ui.downloadbtn_2.clicked.connect(lambda: self.downloadMusic())

    def findMusic(self, link):
        self.ui.main.setEnabled(False)
        flag = True
        # Create a YouTube object with the given URL
        try: 
            self.music = YouTube(link)
        except:
            flag = False
            self.ui.bartxt_2.setText("Lütfen YouTube Linki Giriniz")

        if flag:
            thumbnail = self.music.thumbnail_url
            response = requests.get(thumbnail)

            with open('images/thumbnail_2.jpg', 'wb') as f:
                f.write(response.content)

            self.mtitle = self.music.title
            duration = self.music.length  # saniye türünden video uzunluğu
            self.sesdosyasi = duration / 64  # MB türünden dosya boyutu

            self.ui.thumbfr_2.setStyleSheet(u"#thumbfr_2 { border-image: url(images/thumbnail_2.jpg);} ")

            self.audio = self.music.streams.get_audio_only()  # en yüksek kalitede indirir

            self.ui.videotitle_2.setText(f"{self.mtitle}")

            sesdk = int(duration / 60)
            sessan = duration % 60
            if sessan < 10:
                sessan = f"0{sessan}"
            elif sessan == 0:    
                sessan = "00"

            muziksuresi = f"{sesdk}:{sessan}"
            self.ui.duration_2.setText(muziksuresi)

            self.ui.sizebtn_2.setText(f"{self.sesdosyasi:.1f} MB")

            self.ui.btnpath_2.setEnabled(True)
            self.ui.downloadbtn_2.setEnabled(True)

            self.ui.downloadbtn_2.setText("İndir")
            self.ui.bartxt_2.setStyleSheet("color: #ccc;")
            self.ui.bartxt_2.setText("İndirmeye Hazır")

            self.ui.searchtxt_2.clear()
        self.ui.main.setEnabled(True)

    def downloadMusic(self):
        self.ui.main.setEnabled(False)
        self.ui.bartxt_2.setText("İndiriliyor")
        self.ui.progressBar.setValue(0)
        startdown = datetime.now()

        self.audio.download(output_path=self.mpath)

        try:
            # Ses dosyasını MP3 formatına dönüştürme
            music_title = self.music.title.replace(" ", "_")
            mp3_file = music_title + ".mp3"
            print(self.mpath+"\\"+self.audio.default_filename)
            videoclip = AudioFileClip(self.mpath+"\\"+self.audio.default_filename)
            videoclip.write_audiofile(self.mpath+"\\"+mp3_file)

            # İndirilen ses dosyasının silinmesi
            os.remove(self.mpath+"\\"+self.audio.default_filename)
            
            enddown = datetime.now()
            process = str((enddown-startdown).seconds)

            self.progressanimation = QPropertyAnimation(self.ui.progressBar_2, b"value")
            self.progressanimation.setDuration(2000)
            self.progressanimation.setStartValue(0)
            self.progressanimation.setEndValue(100)
            self.progressanimation.setEasingCurve(QtCore.QEasingCurve.OutInQuint)
            self.progressanimation.start()

            musicdate = datetime.now().strftime("%c")

            with open("history.csv", "a", encoding="utf-8") as wf:
                writeon = csv.writer(wf, delimiter=",", quotechar=',', quoting=csv.QUOTE_MINIMAL)
                writeon.writerow(['sound', self.ui.sizebtn_2.text(), mp3_file, musicdate])

            self.ui.bartxt_2.setText(f"İndirildi ({process} sn)")

        except:
            self.ui.bartxt_2.setStyleSheet("color: red;")
            self.ui.bartxt_2.setText("Bir Hata Oluştu")
        self.ui.main.setEnabled(True)

    def setmPath(self):
        dialog = QFileDialog()
        self.mpath = dialog.getExistingDirectory(self, 'Ses Kaydetme Yeri Seçin')
        if self.mpath == "":
            self.mpath = str(Path.home() / "Downloads")
            self.ui.btnpath_2.setText("/Downloads")
        else:
            btntxt = self.mpath.split("/")
            self.ui.btnpath_2.setText(f"/{btntxt[-1]}")
            self.ui.btnpath_2.setChecked(True)


    ### VİDEO

    def videoFunctions(self):
        # pencere butonları
        self.ui.close.clicked.connect(lambda: sys.exit())
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())
        # sayfa butonları
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.videobtn.setEnabled(False)
        self.ui.videobtn.setChecked(True) 
        self.ui.videobtn.clicked.connect(lambda: self.videoPage())
        self.ui.musicbtn.clicked.connect(lambda: self.musicPage())
        self.ui.transformbtn.clicked.connect(lambda: self.transformPage())
        self.ui.historybtn.clicked.connect(lambda: self.historyPage())
        self.ui.aboutbtn.clicked.connect(lambda: self.aboutPage())
        self.ui.settingsbtn.clicked.connect(lambda: self.settingsPage())
        # kalite butonları
        self.ui.btn720p.setEnabled(False)
        self.ui.btn720p.setChecked(True) 
        self.ui.btn720p.clicked.connect(lambda: self.p720())
        self.ui.btn360p.clicked.connect(lambda: self.p360())
        # dosya konumu butonu
        self.ui.btnpath.setText("/Downloads")
        self.path = str(Path.home() / "Downloads")
        self.ui.btnpath.clicked.connect(lambda: self.setPath())
        # arama butonu
        self.ui.searchbtn.clicked.connect(lambda: self.findVideo(self.ui.searchtxt.text()))
        # kalite butonları
        self.ui.btn720p.clicked.connect(lambda: self.get720p())
        self.ui.btn360p.clicked.connect(lambda: self.get360p())
        # videoyu indir
        
        self.ui.downloadbtn.clicked.connect(self.downloadVideo)

    def get720p(self):
        self.stream = self.streams.get_highest_resolution()
        self.filesize = self.stream.filesize
        self.filesize = float(self.filesize / (1024*1024))
        self.ui.sizebtn.setText(f"{self.filesize:.1f} MB")

    def get360p(self):
        self.stream = self.streams.get_lowest_resolution()
        self.filesize = self.stream.filesize
        self.filesize = float(self.filesize / (1024*1024))
        self.ui.sizebtn.setText(f"{self.filesize:.1f} MB")
          
    def findVideo(self, link):
        self.ui.main.setEnabled(False)
        flag = True
        # Create a YouTube object with the given URL
        try: 
            self.video = YouTube(link)
        except:
            flag = False
            self.ui.bartxt.setText("Lütfen YouTube Linki Giriniz")

        if flag:
            thumbnail = self.video.thumbnail_url
            response = requests.get(thumbnail)

            with open('images/thumbnail.jpg', 'wb') as f:
                f.write(response.content)

            self.title = self.video.title
            duration = self.video.length

            self.ui.thumbfr.setStyleSheet(u"#thumbfr { border-image: url(images/thumbnail.jpg);} ")

            # Get the available video streams
            self.streams = self.video.streams.filter(progressive=True)

            self.ui.videotitle.setText(f"{self.title}")

            sesdk = int(duration / 60)
            sessan = duration % 60
            if sessan < 10:
                sessan = f"0{sessan}"
            elif sessan == 0:    
                sessan = "00"
            videosuresi = f"{sesdk}:{sessan}"
            self.ui.duration.setText(videosuresi)

            self.resolist = list()
            for self.stream in self.streams:
                if self.stream.resolution != "144p":
                    self.resolist.append(self.stream.resolution)
            
            if len(self.resolist) == 1:
                self.ui.btn360p.setText(self.resolist[-1])
                self.ui.btn360p.setChecked(True)
                self.ui.btn720p.setChecked(False)
            else: 
                self.ui.btn360p.setText(self.resolist[-2])
                self.ui.btn720p.setText(self.resolist[-1])
                self.ui.btn360p.setEnabled(True)

            self.stream = self.streams.get_highest_resolution()
            self.filesize = self.stream.filesize
            self.filesize = float(self.filesize / (1024*1024))

            self.ui.sizebtn.setText(f"{self.filesize:.1f} MB")

            self.ui.btnpath.setEnabled(True)
            self.ui.downloadbtn.setEnabled(True)

            self.ui.downloadbtn.setText("İndir")
            self.ui.bartxt.setStyleSheet("color: #ccc;")
            self.ui.bartxt.setText("İndirmeye Hazır")

            self.ui.searchtxt.clear()
        self.ui.main.setEnabled(True)

    def downloadVideo(self):
        self.ui.main.setEnabled(False)
        self.ui.progressBar.setValue(0)
        startdown = datetime.now()
        self.stream.download(output_path=self.path)
        enddown = datetime.now()
        process = str((enddown-startdown).seconds)

        self.progressanimation = QPropertyAnimation(self.ui.progressBar, b"value")
        self.progressanimation.setDuration(2000)
        self.progressanimation.setStartValue(0)
        self.progressanimation.setEndValue(100)
        self.progressanimation.setEasingCurve(QtCore.QEasingCurve.OutInQuint)
        self.progressanimation.start()

        videodate = datetime.now().strftime("%c")

        with open("history.csv", "a", encoding="utf-8") as wf:
            writeon = csv.writer(wf, delimiter=",", quotechar=',', quoting=csv.QUOTE_MINIMAL)
            writeon.writerow(['video', self.ui.sizebtn.text(), self.title, videodate])

        self.ui.bartxt.setText(f"İndirildi ({process} sn)")
        self.ui.main.setEnabled(True)

    def setPath(self):
        dialog = QFileDialog()
        self.path = dialog.getExistingDirectory(self, 'Video Kaydetme Yeri Seçin')
        if self.path == "":
            self.path = str(Path.home() / "Downloads")
            self.ui.btnpath.setText("/Downloads")
        else:
            btntxt = self.path.split("/")
            self.ui.btnpath.setText(f"/{btntxt[-1]}")
            self.ui.btnpath.setChecked(True)

    def p720(self):
        self.ui.btn720p.setEnabled(False)
        self.ui.btn360p.setChecked(False)
        self.ui.btn360p.setEnabled(True)

    def p360(self):
        self.ui.btn360p.setEnabled(False)
        self.ui.btn720p.setChecked(False)
        self.ui.btn720p.setEnabled(True)

    def videoPage(self):
        self.ui.videobtn.setEnabled(False)
        self.ui.musicbtn.setChecked(False)
        self.ui.musicbtn.setEnabled(True)
        self.ui.transformbtn.setChecked(False)
        self.ui.transformbtn.setEnabled(True)
        self.ui.historybtn.setChecked(False)
        self.ui.historybtn.setEnabled(True)
        self.ui.aboutbtn.setChecked(False)
        self.ui.aboutbtn.setEnabled(True)
        self.ui.settingsbtn.setChecked(False)
        self.ui.settingsbtn.setEnabled(True)
        self.ui.stackedWidget.setCurrentIndex(0)

    def musicPage(self):
        self.ui.musicbtn.setEnabled(False)
        self.ui.videobtn.setChecked(False)
        self.ui.videobtn.setEnabled(True)
        self.ui.transformbtn.setChecked(False)
        self.ui.transformbtn.setEnabled(True)
        self.ui.historybtn.setChecked(False)
        self.ui.historybtn.setEnabled(True)
        self.ui.aboutbtn.setChecked(False)
        self.ui.aboutbtn.setEnabled(True)
        self.ui.settingsbtn.setChecked(False)
        self.ui.settingsbtn.setEnabled(True)
        self.ui.stackedWidget.setCurrentIndex(1)

    def transformPage(self):
        self.ui.transformbtn.setEnabled(False)
        self.ui.videobtn.setChecked(False)
        self.ui.videobtn.setEnabled(True)
        self.ui.musicbtn.setChecked(False)
        self.ui.musicbtn.setEnabled(True)
        self.ui.historybtn.setChecked(False)
        self.ui.historybtn.setEnabled(True)
        self.ui.aboutbtn.setChecked(False)
        self.ui.aboutbtn.setEnabled(True)
        self.ui.settingsbtn.setChecked(False)
        self.ui.settingsbtn.setEnabled(True)
        self.ui.stackedWidget.setCurrentIndex(2)

    def historyPage(self):
        self.ui.historybtn.setEnabled(False)
        self.ui.videobtn.setChecked(False)
        self.ui.videobtn.setEnabled(True)
        self.ui.musicbtn.setChecked(False)
        self.ui.musicbtn.setEnabled(True)
        self.ui.transformbtn.setChecked(False)
        self.ui.transformbtn.setEnabled(True)
        self.ui.aboutbtn.setChecked(False)
        self.ui.aboutbtn.setEnabled(True)
        self.ui.settingsbtn.setChecked(False)
        self.ui.settingsbtn.setEnabled(True)
        self.ui.stackedWidget.setCurrentIndex(3)

        flag = True
        with open("history.csv", "r", encoding="utf-8") as f:
            content = csv.reader(f, delimiter=",")
            cumle = ""
            itemlist = list()
            for dest in content:
                if len(dest) == 0:
                    flag = False
                if len(dest) != 0:
                    itemlist.append(dest) 
            itemlist.reverse()

            if flag == True:
                self.ui.clearh.setEnabled(False)
                self.ui.past.setText("Henüz işlem yapılmadı.")
            else:
                itemMB = 0
                itemadet = 0
                for deste in itemlist:
                    self.ui.past.clear()
                    self.ui.clearh.setEnabled(True)
                    if deste[0] == "video":
                        icon = "▶"
                    elif deste[0] == "sound":
                        icon = "𝄞"
                    elif deste[0] == "transform":
                        icon = "∞"
                    cumle += f"{icon} / {deste[2][:15]}.. / {deste[1]} / {deste[3][:-3]}\n\n"
                    itemMB += float(deste[1][:-3])
                    itemadet += 1
                itemc = "Temizle ("+str(itemMB)+" MB)"
                self.ui.clearh.setText(itemc)
                self.ui.past.setText(cumle)
                self.ui.abouth.setText(f"Uygulama Geçmişi ({itemadet})")

    def aboutPage(self):
        self.ui.aboutbtn.setEnabled(False)
        self.ui.videobtn.setChecked(False)
        self.ui.videobtn.setEnabled(True)
        self.ui.musicbtn.setChecked(False)
        self.ui.musicbtn.setEnabled(True)
        self.ui.transformbtn.setChecked(False)
        self.ui.transformbtn.setEnabled(True)
        self.ui.historybtn.setChecked(False)
        self.ui.historybtn.setEnabled(True)
        self.ui.settingsbtn.setChecked(False)
        self.ui.settingsbtn.setEnabled(True)
        self.ui.stackedWidget.setCurrentIndex(4)

    def settingsPage(self):
        self.ui.settingsbtn.setEnabled(False)
        self.ui.videobtn.setChecked(False)
        self.ui.videobtn.setEnabled(True)
        self.ui.musicbtn.setChecked(False)
        self.ui.musicbtn.setEnabled(True)
        self.ui.transformbtn.setChecked(False)
        self.ui.transformbtn.setEnabled(True)
        self.ui.historybtn.setChecked(False)
        self.ui.historybtn.setEnabled(True)
        self.ui.aboutbtn.setChecked(False)
        self.ui.aboutbtn.setEnabled(True)
        self.ui.stackedWidget.setCurrentIndex(5)


    # pencereye mouse fonksiyonu ekleme
    def mousePressEvent(self, event):
        # pencerenin güncel konumunu alma
        self.clickPosition = event.globalPos()



# UYGULMAYI ÇALIŞTIRMA
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
