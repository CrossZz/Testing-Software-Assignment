import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Demophantom(unittest.TestCase): 
      def setUp(self):
         self.driver = webdriver.Chrome(executable_path=".././driver/chromedriver.exe")
         self.timeout = 60
         self.driver.get('https://vn-z.vn')

         # Đăng nhập 

         link_SignIn = self.driver.find_element(By.CSS_SELECTOR, "a[href='/login/']")
         link_SignIn.click() 

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.NAME,'login'))
         )

         txt_email = self.driver.find_element(By.NAME,'login')
         txt_email.send_keys("minhhoang0411")

         txt_passwd = self.driver.find_element(By.NAME,'password')
         txt_passwd.send_keys("20062000")

         btn_login = self.driver.find_element(By.CLASS_NAME, 'button--icon--login')
         btn_login.click()

      def test1_text_comment(self):

         self.driver.get('https://vn-z.vn/threads/god-of-war-4-pc-xac-nhan-ho-tro-man-hinh-sieu-rong-4k-cong-nghe-dlss-va-fsr-v-v.44176/')

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".fr-element.fr-view p"))
         )

         txt_cmt=self.driver.find_element(By.CSS_SELECTOR,".fr-element.fr-view p")
         txt_cmt.send_keys("Game hay")

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         time.sleep(2)
         

         cmt=self.driver.find_element(By.CSS_SELECTOR,"article[data-author='minhhoang0411']:last-child article .bbWrapper")
         assert cmt.text == "Game hay"
      
      def test2_emoji_comment(self):

         self.driver.get('https://vn-z.vn/threads/mien-cuoc-data-khi-do-speedtest-vn-toc-do-internet.44174/')

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".fr-element.fr-view p"))
         )

         icon = self.driver.find_element(By.ID,"xfSmilie-1")
         icon.click()

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CLASS_NAME,"js-emoji"))
         )
         smile=self.driver.find_element(By.CSS_SELECTOR,"a[data-shortname=':)']")
         smile.click()

         txt_cmt=self.driver.find_element(By.CSS_SELECTOR,".fr-element.fr-view p")
         txt_cmt.send_keys("Thông tin khá bổ ích")

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         time.sleep(2)
         
         cmt=self.driver.find_element(By.CSS_SELECTOR,"article[data-author='minhhoang0411']:last-child article .bbWrapper")
         #kiểm tra xem có emoji chưa   
         check=True
         try:   
            checkEmoji=cmt.find_element(By.CSS_SELECTOR,"img[data-shortname=':)']")
         except:
            check=False

         assert cmt.text=="Thông tin khá bổ ích" and check==True

      def test3_null_comment(self):

         self.driver.get('https://vn-z.vn/threads/mot-so-ung-dung-windows-11-bi-hong-do-chung-chi-het-han.44160/')

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".fr-element.fr-view p"))
         )

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".overlay-content .blockMessage"))
         )
        
         # Store the alert text in a variable
         alert=self.driver.find_element(By.CSS_SELECTOR,".overlay-content .blockMessage")
         assert alert.text=="Xin mời nhập vào đúng nội dung."
      
      def test4_image_comment(self):

         self.driver.get('https://vn-z.vn/threads/mot-so-ung-dung-windows-11-bi-hong-do-chung-chi-het-han.44160/')

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".fr-element.fr-view p"))
         )
         btn_insert=self.driver.find_element(By.ID,'insertImage-1')
         btn_insert.click()

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.ID,'imageByURL-1'))
         )

         btn_url=self.driver.find_element(By.ID,'imageByURL-1')
         btn_url.click()

         input_url=self.driver.find_element(By.ID,'fr-image-by-url-layer-text-1')
         input_url.send_keys("https://lafactoriaweb.com/wp-content/uploads/2020/09/Meme_la_gi_03-600x375.jpg")

         btn_chen=self.driver.find_element(By.CSS_SELECTOR,"button[data-cmd='imageInsertByURL']")
         btn_chen.click()
         
         time.sleep(1)

         txt_cmt=self.driver.find_element(By.CSS_SELECTOR,".fr-element.fr-view p")
         txt_cmt.send_keys("Bài viết hay đó")

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         time.sleep(2)
         
         cmt=self.driver.find_element(By.CSS_SELECTOR,"article[data-author='minhhoang0411']:last-child article .bbWrapper")
         check=True
         try:
            checkImage=cmt.find_element(By.CSS_SELECTOR,"img[src='https://lafactoriaweb.com/wp-content/uploads/2020/09/Meme_la_gi_03-600x375.jpg']")
         except:
            check=False
         assert cmt.text=="Bài viết hay đó" and check==True
      
      def test5_text_answer(self):

         self.driver.get('https://vn-z.vn/threads/god-of-war-4-pc-xac-nhan-ho-tro-man-hinh-sieu-rong-4k-cong-nghe-dlss-va-fsr-v-v.44176/')

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".fr-element.fr-view p"))
         )

         reply=self.driver.find_element(By.CSS_SELECTOR,"a[title='Trả lời, trích dẫn bài viết này']")
         reply.click()

         txt_cmt=self.driver.find_element(By.CSS_SELECTOR,".fr-element.fr-view p")
         txt_cmt.send_keys("Game hay")

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         time.sleep(2)
         

         cmt=self.driver.find_element(By.CSS_SELECTOR,"article[data-author='minhhoang0411']:last-child article .bbWrapper")
         assert cmt.text == "Game hay"

      def test6_emoji_answer(self):

         self.driver.get('https://vn-z.vn/threads/mien-cuoc-data-khi-do-speedtest-vn-toc-do-internet.44174/')

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".fr-element.fr-view p"))
         )
         reply=self.driver.find_element(By.CSS_SELECTOR,"a[title='Trả lời, trích dẫn bài viết này']")
         reply.click()

         icon = self.driver.find_element(By.ID,"xfSmilie-1")
         icon.click()

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CLASS_NAME,"js-emoji"))
         )
         smile=self.driver.find_element(By.CSS_SELECTOR,"a[data-shortname=':)']")
         smile.click()

         txt_cmt=self.driver.find_element(By.CSS_SELECTOR,".fr-element.fr-view p")
         txt_cmt.send_keys("Bài viết khá bổ ích")

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         time.sleep(2)
         
         cmt=self.driver.find_element(By.CSS_SELECTOR,"article[data-author='minhhoang0411']:last-child article .bbWrapper")
         #kiểm tra xem có emoji chưa
         check=True
         try:   
            checkEmoji=cmt.find_element(By.CSS_SELECTOR,"img[data-shortname=':)']")
         except:
            check=False

         assert cmt.text=="Bài viết khá bổ ích" and check==True

      def test7_null_answer(self):

         self.driver.get('https://vn-z.vn/threads/vivobook-13-slate-oled-t3300-may-tinh-may-tinh-bang-tv-oled-tat-ca-trong-mot.44130/')

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".fr-element.fr-view p"))
         )
         reply=self.driver.find_element(By.CSS_SELECTOR,"a[title='Trả lời, trích dẫn bài viết này']")
         reply.click()

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".overlay-content .blockMessage"))
         )
        
         # Store the alert text in a variable
         alert=self.driver.find_element(By.CSS_SELECTOR,".overlay-content .blockMessage")
         assert alert.text=="Xin mời nhập vào đúng nội dung."
      
      def test8_image_answer(self):

         self.driver.get('https://vn-z.vn/threads/mot-so-ung-dung-windows-11-bi-hong-do-chung-chi-het-han.44160/')

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".fr-element.fr-view p"))
         )

         reply=self.driver.find_element(By.CSS_SELECTOR,"a[title='Trả lời, trích dẫn bài viết này']")
         reply.click()

         btn_insert=self.driver.find_element(By.ID,'insertImage-1')
         btn_insert.click()

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.ID,'imageByURL-1'))
         )

         btn_url=self.driver.find_element(By.ID,'imageByURL-1')
         btn_url.click()

         input_url=self.driver.find_element(By.ID,'fr-image-by-url-layer-text-1')
         input_url.send_keys("https://lafactoriaweb.com/wp-content/uploads/2020/09/Meme_la_gi_03-600x375.jpg")

         btn_chen=self.driver.find_element(By.CSS_SELECTOR,"button[data-cmd='imageInsertByURL']")
         btn_chen.click()
         
         time.sleep(1)

         txt_cmt=self.driver.find_element(By.CSS_SELECTOR,".fr-element.fr-view p")
         txt_cmt.send_keys("Bài viết hay")

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         time.sleep(2)
         
         cmt=self.driver.find_element(By.CSS_SELECTOR,"article[data-author='minhhoang0411']:last-child article .bbWrapper")
         check=True
         try:
            checkImage=cmt.find_element(By.CSS_SELECTOR,"img[src='https://lafactoriaweb.com/wp-content/uploads/2020/09/Meme_la_gi_03-600x375.jpg']")
         except:
            check=False
         assert cmt.text=="Bài viết hay" and check==True
      
      def test9_nonfunc(self):
         self.driver.get('https://vn-z.vn/threads/alder-lake-s-intel-core-12th-ban-ra-giup-amd-giam-gia.44196/')

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".fr-element.fr-view p"))
         )

         txt_cmt=self.driver.find_element(By.CSS_SELECTOR,".fr-element.fr-view p")
         txt_cmt.send_keys("Bài viết bổ ích ghê")

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         self.driver.get('https://vn-z.vn/threads/alder-lake-s-intel-core-12th-ban-ra-giup-amd-giam-gia.44196/')

         txt_cmt=self.driver.find_element(By.CSS_SELECTOR,".fr-element.fr-view p")
         txt_cmt.send_keys("Bài viết bổ ích ghê")

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".overlay-content .blockMessage"))
         )
        
         # Store the alert text in a variable
         alert=self.driver.find_element(By.CSS_SELECTOR,".overlay-content .blockMessage").text
         assert alert[0:22]=="You must wait at least"
      
      def test10_nonfunc(self):

         self.driver.get('https://vn-z.vn/threads/samsung-dang-bi-kien-vi-da-ban-samsung-chromebook-plus-2-trong-1-vi-loi-ban-le-khien-man-hinh-bi-vo.44204/')

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".fr-element.fr-view p"))
         )

         txt_cmt=self.driver.find_element(By.CSS_SELECTOR,".fr-element.fr-view p")
         txt_cmt.send_keys("2 ông lớn đánh nhau")

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         self.driver.get('https://vn-z.vn/threads/alder-lake-s-intel-core-12th-ban-ra-giup-amd-giam-gia.44196/')

         reply=self.driver.find_element(By.CSS_SELECTOR,"a[title='Trả lời, trích dẫn bài viết này']")
         reply.click()

         txt_cmt=self.driver.find_element(By.CSS_SELECTOR,".fr-element.fr-view p")
         txt_cmt.send_keys("2 ông lớn đánh nhau")

         btn_reply = self.driver.find_element(By.CLASS_NAME, 'button--icon--reply')
         btn_reply.click()

         WebDriverWait(self.driver,self.timeout).until(

            EC.presence_of_element_located((By.CSS_SELECTOR,".overlay-content .blockMessage"))
         )
        
         # Store the alert text in a variable
         alert=self.driver.find_element(By.CSS_SELECTOR,".overlay-content .blockMessage").text
         assert alert[0:22]=="You must wait at least"

      def tearDown(self):
         self.driver.quit()

if __name__ == '__main__':
   unittest.main()