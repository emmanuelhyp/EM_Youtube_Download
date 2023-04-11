
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
from os import path
from PyQt5.uic import loadUiType
import urllib.request
import pafy
import humanize



ui,_ = loadUiType('main.ui')

class MainApp(QMainWindow , ui ):
    def __init__(self, parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        self.bouton()


    def InitUI(self) :
        self.tabWidget.tabBar().setVisible(False)
        self.applike_ubuntu()
        self.deplasman_box1()
        self.deplasman_box2()
        self.deplasman_box3()
        self.deplasman_box4()



    def bouton(self):
        ##comand tout bouton nan app la
        self.pushButton_10.clicked.connect(self.telechaje)
        self.pushButton_2.clicked.connect(self.locat)

        self.pushButton_5.clicked.connect(self.video_info)
        self.pushButton_9.clicked.connect(self.telechaje_video)
        self.pushButton_3.clicked.connect(self.sauvegad_locat)

        self.pushButton_8.clicked.connect(self.telechaje_playlist)
        self.pushButton_7.clicked.connect(self.sauvegad_locat_playlist)

        self.pushButton.clicked.connect(self.ouvri_acceuil)
        self.pushButton_4.clicked.connect(self.ouvri_telechajman)
        self.pushButton_11.clicked.connect(self.ouvri_youtube)
        self.pushButton_12.clicked.connect(self.ouvri_settings)

        self.pushButton_15.clicked.connect(self.applike_ubuntu)
        self.pushButton_13.clicked.connect(self.applike_darkgray)
        self.pushButton_6.clicked.connect(self.applike_darkorange)
        self.pushButton_14.clicked.connect(self.applike_dark)

    def progression (self, blocknum, blocktaille,totaltaille):
        ##calcule la progression
        read= blocktaille * blocknum

        if totaltaille > 0 :
            download_poucentag = read * 100 / totaltaille
            self.progressBar.setValue(download_poucentag)
            QApplication.processEvents()

    #####################################################################################
    ################## Parti de telechajeman d'un pichier quelconq fichier###############
    def locat(self):
        save_locat=QFileDialog.getSaveFileName(self, caption="Sauvegarder comme" , directory="." , filter="All File(*.*)")
        print(save_locat)
        self.lineEdit_2.setText(str(save_locat[0]))

    def telechaje(self):
        telechaje_url= self.lineEdit.text()
        save_locat = self.lineEdit_2.text()

        if telechaje_url=='' or save_locat=='' :
            QMessageBox.warning(self, "erreur de donnee!!!",'Link oubyen Location an pa rete vid')
        else:
            try:
                urllib.request.urlretrieve(telechaje_url , save_locat , self.progression)
            except Exception:
                QMessageBox.warning(self, "Erreur de telechajeman", 'SVP importer un url valide ou un location valide')

        QMessageBox.information(self,"telechajman Fini" , "telechajman fini avek sikse")

        telechaje_url = self.lineEdit.text()
        save_locat = self.lineEdit_2.text()
        self.progressBar.setValue(0)


    def sauvegad_locat(self):
        ##modifye kote pou enregistre
        pass

#####################################################################################
########################  pati de telechajman de video youtube  #####################

    def sauvegad_locat(self):
        save_locat = QFileDialog.getSaveFileName(self, caption="Sauvegarder comme", directory=".", filter="Video mp4(*.mp4);; All File(*.*)")
        self.lineEdit_4.setText(str(save_locat[0]))

    def video_info(self):
        video_url=self.lineEdit_3.text()

        if video_url=='' :
            QMessageBox.warning(self,'Erreur de donnee','importer un video url valide')
        else:
            video = pafy.new(video_url)
            print(video.title)
            print(video.duration)
            print(video.author)
            print(video.viewcount)

            video_kalite=video.streams
            for stream in video_kalite :
                size=humanize.naturalsize(stream.get_filesize())
                data="{} {} {} {}".format(stream.mediatype, stream.extension, stream.quality , size)

                self.comboBox.addItem(data)



    def telechaje_video(self):
        video_url= self.lineEdit_3.text()
        save_locat= self.lineEdit_4.text()

        if video_url == '' or save_locat=='':
            QMessageBox.warning(self, 'Erreur de donnee', 'importer un video url valide')
        else:
            video = pafy.new(video_url)
            video_stream = video.streams
            kalite_video= self.comboBox.currentIndex()
            telechajman = video_stream[kalite_video].download(filepath=save_locat, callback=self.video_progression)

            QMessageBox.information(self,"telechajman Fini" , "telechajman fini avek sikse")

            telechaje_url = self.lineEdit_3.setText("")
            save_locat = self.lineEdit_4.setText("")
            self.label_5.setText("")
            self.progressBar_2.setValue(0)
            self.comboBox.clear()




    def video_progression(self , total, received, ratio, rate, time):
        read_data = received
        if total > 0 :
            download_percent = read_data *100 / total
            self.progressBar_2.setValue(download_percent)
            temps_restant = round(time/60,2)

            self.label_5.setText(str("{} minit ki rete".format(temps_restant)))
            QApplication.processEvents()




##############################################################################
#####################Pati telechajman playlist################################


    def telechaje_playlist(self):
        playlist_url = self.lineEdit_5.text()
        save_locat = self.lineEdit_6.text()

        if playlist_url == '' or save_locat == '':
            QMessageBox.warning(self , 'Erreur de donnee', 'importer un video url valide')
        else:
            playlist = pafy.get_playlist(playlist_url)
            playlist_video = playlist['items']
            self.lcdNumber_2.display(len(playlist_video))

        os.chdir(save_locat)
        if os.path.exists(str(playlist['title'])) :
            os.chdir(str(playlist['title']))
        else:
            os.mkdir(str(playlist['title']))
            os.chdir(str(playlist['title']))

        video_couran_download = 1
        #quality= self.comboBox_2.currentIndex()

        QApplication.processEvents()
        for video in playlist_video :
            try :

                couran_video = video['pafy']
                couran_video_stream = couran_video.getbest(preftype='mp4')
                self.label_16.setText(str("{} {}".format(couran_video_stream.resolution,couran_video_stream.extension)))
                video_couran_download +=1
                download = couran_video_stream.download(callback=self.telechaman_progression)
                self.lcdNumber.display(video_couran_download)
                QApplication.processEvents()
            except OSError :
                QMessageBox.warning(self , 'Erreur de extraction', 'Nous paka telechaj video sa')

            except TypeError:
                QMessageBox.warning(self , 'Erreur de type', 'Nous paka telechaje typ video sa')

        QMessageBox.information(self,"telechajman Fini" , "telechajman fini avek sikse")

        telechaje_url = self.lineEdit_5.setText("")
        save_locat = self.lineEdit_6.setText("")
        self.label_16.setText("")
        self.progressBar_3.setValue(0)
        self.comboBox.clear()
        self.lcdNumber_2.display(0)
        self.lcdNumber.display(0)






    def telechaman_progression(self , total, received, ratio, rate, time):
        read_data = received
        if total > 0:
            download_percent = read_data * 100 / total
            self.progressBar_3.setValue(download_percent)
            temps_restant = round(time / 60, 2)
            self.label_6.setText(str("{} minit ki rete".format(temps_restant)))
            QApplication.processEvents()

    def sauvegad_locat_playlist(self):
        save_locat_playlist = QFileDialog.getExistingDirectory(self,"chwazi dpsye wap metel")
        self.lineEdit_6.setText(save_locat_playlist)


    ###################################################
    ################ chanje de menu ###################

    def ouvri_acceuil(self):
        self.tabWidget.setCurrentIndex(0)
        self.deplasman_box1()
        self.deplasman_box2()
        self.deplasman_box3()
        self.deplasman_box4()


    def ouvri_telechajman(self):
        self.tabWidget.setCurrentIndex(1)

    def ouvri_youtube(self):
        self.tabWidget.setCurrentIndex(2)

    def ouvri_settings(self):
        self.tabWidget.setCurrentIndex(3)



#####################################################################
#############appp theme###############################
    def applike_darkgray(self):
        style = open('themes/qstyledarkgray.css','r')
        style = style.read()
        self.setStyleSheet(style)


    def applike_dark(self):
        style = open('themes/style_dark.css','r')
        style = style.read()
        self.setStyleSheet(style)

    def applike_ubuntu(self):
        style = open('themes/styleubuntu.css','r')
        style = style.read()
        self.setStyleSheet(style)

    def applike_darkorange(self):
        style = open('themes/darkorange.css','r')
        style = style.read()
        self.setStyleSheet(style)

####################################################################################################
#############################app animation #####################################

    def deplasman_box1(self):
        box_anime1 = QPropertyAnimation(self.groupBox, b"geometry")
        box_anime1.setDuration(2000)
        box_anime1.setStartValue(QRect(0,0,0,0))
        box_anime1.setEndValue(QRect(21,30,261,111))
        box_anime1.start()
        self.box_anime1 = box_anime1

    def deplasman_box3(self):
        box_anime3 = QPropertyAnimation(self.groupBox_3, b"geometry")
        box_anime3.setDuration(2000)
        box_anime3.setStartValue(QRect(0,0,0,0))
        box_anime3.setEndValue(QRect(321,30,261,111))
        box_anime3.start()
        self.box_anime3 = box_anime3

    def deplasman_box2(self):
        box_anime2 = QPropertyAnimation(self.groupBox_2, b"geometry")
        box_anime2.setDuration(2000)
        box_anime2.setStartValue(QRect(0,0,0,0))
        box_anime2.setEndValue(QRect(20,180,261,111))
        box_anime2.start()
        self.box_anime2 = box_anime2

    def deplasman_box4(self):
        box_anime4 = QPropertyAnimation(self.groupBox_4, b"geometry")
        box_anime4.setDuration(2000)
        box_anime4.setStartValue(QRect(0,0,0,0))
        box_anime4.setEndValue(QRect(320,180,261,111))
        box_anime4.start()
        self.box_anime4 = box_anime4






####################################################################################################




def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.setWindowTitle("Man App download")
    window.setWindowIcon(QIcon("icon/icon.ico"))
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
