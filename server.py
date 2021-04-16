import os
import time
import pandas as pd
import requests
import pyrebase
import pandas as pd
from firebase_admin import credentials, initialize_app, storage , firestore

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Not So System Files\Study\6th sem\SGP Ideas\quick3D\serviceAcc.json'

cred = credentials.Certificate("serviceAcc.json")
app = initialize_app(cred, {'storageBucket': 'quick3d-a9d3d.appspot.com'})
# app = initialize_app(cred)


config={
    "apiKey": "AIzaSyBHUU0WTY8j9QDX-rEx-rNvMrRIzwI9l5E",
    "databaseURL": "",
    "authDomain": "quick3d-a9d3d.firebaseapp.com",
    "projectId": "quick3d-a9d3d",
    "storageBucket": "quick3d-a9d3d.appspot.com",
    "messagingSenderId": "751533499745",
    "appId": "1:751533499745:web:ffbddaabe599db68569120",
    "measurementId": "G-QZRMCR0CLZ",
    "serviceAccount" : "serviceAcc.json"
}

OBJ_DIR = "src/results/pifuhd_final/recon"
IMG_DIR = "src/images"

DOWNLOAD_DIR_PATH = 'src/images'
FIREBASE_IMG_PATH = 'img'
FIREBASE_OBJ_PATH = 'obj'
FIREBASE_PRE_PATH = 'img-preview'
LOCAL_PRE_PATH = "src/results/pifuhd_final/recon/"
LOCAL_OBJ_PATH = "src/results/pifuhd_final/recon/"

def filename_from_link(link):
    img_name=link.split('%2F')[1].split('?')[0]
    return img_name

def get_fb_file_list():
    files = storage_wrapper.list_files()
    img_list = []
    for file in files:
        entry = {}
        link = storage_wrapper.child(file.name).get_url(None)
        print(link)
        img_ext = ['png','jpg','jpeg']
        for ext in img_ext:
            if link.find(ext) != -1  and link.find('img-preview') == -1:
                img_list.append((link,filename_from_link(link)))
                break

    return img_list


def get_local_file_list():
    items = os.listdir(IMG_DIR)
    newlist = []
    for names in items:
        if names.endswith(".png") or names.endswith(".jpg") or names.endswith(".jpeg"):
            newlist.append(names)
            
    return newlist

def Fetch():
    imglist = get_fb_file_list()
    lcllist = get_local_file_list()
    not_processed_files = []
    for ci in imglist:
        if (ci[1] not in lcllist): # check for this also in future -> if (ci[1].split('.')[0]+'.obj' not in df.name)
            #download
            not_processed_files.append(ci[1])
            print('downloading file...')
            r = requests.get(ci[0])
            open(DOWNLOAD_DIR_PATH+'/'+ci[1], 'wb').write(r.content)
            print('downloaded ',DOWNLOAD_DIR_PATH+'/'+ci[1])

    return not_processed_files


def Process():
    #process !takes about 50 sec per image.
    print('Making 3D Models...')
    stream = os.popen('cmd /c "app.bat"')
    output = stream.read()
    print(output)


def UploadAndClean(not_processed_files):
    #deleting processed files
    print("deleting image files as it's processed...")
    df = pd.read_csv('list.csv')
    for imgname in not_processed_files:
        #delete from local dir
        # os.remove(DOWNLOAD_DIR_PATH+'/'+imgname)
        #upload the model
        print("uploading 3D model of ",imgname)
        # #by using pyrbase
        # storage_wrapper.child(FIREBASE_OBJ_PATH +'/'+imgname.split('.')[0] + '.obj').put(LOCAL_OBJ_PATH + imgname.split('.')[0] + '.obj')

        #uploading obj
        blob = bucket.blob(FIREBASE_OBJ_PATH +'/'+imgname.split('.')[0] + '.obj')
        blob.upload_from_filename(LOCAL_OBJ_PATH +'/'+ imgname.split('.')[0] + '.obj')
        blob.make_public()
        link =blob.public_url

        #uploading corresponding img preview
        blob = bucket.blob(FIREBASE_PRE_PATH +'/'+imgname.split('.')[0] + '.png')
        blob.upload_from_filename(LOCAL_PRE_PATH + imgname.split('.')[0] + '.png')
        blob.make_public()
        preview_link =blob.public_url
        print("uploaded.")
        #delete from firebase
        # storage_wrapper.delete(FIREBASE_IMG_PATH+'/'+imgname)
        entry ={}
        entry['link'] = link
        entry['preview_link'] = preview_link
        entry['name'] = imgname.split('.')[0] + '.obj'
        entry['image'] = FIREBASE_IMG_PATH+'/'+imgname
        entry['processed'] = 1
        print(entry)
        doc_ref = db.collection(u'obj')
        doc_ref.add(entry)
        df = df.append(entry, ignore_index = True)
    df.to_csv('list.csv')
    storage_wrapper.child('list.csv').put(r'C:\Not So System Files\Study\6th sem\SGP Ideas\quick3D\list.csv')



def timer():
    t = 30 #number of seconds per each scan
    while t:
        mins, secs = divmod(t, 60)
        timer = 'COOLDOWN {:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print()



    

if __name__ == '__main__':
    db = firestore.Client()
    df = pd.read_csv('list.csv')
    firebase=pyrebase.initialize_app(config)
    bucket = storage.bucket()
    storage_wrapper = firebase.storage()
    
    # while True:
    #     try:
    #         not_processed_files = Fetch()
    #         print("number of unprocessed images : ",len(not_processed_files))
    #         if len(not_processed_files) == 0:
    #             timer()
    #             continue
    #         else:
    #             # Process() #Pose Estimation -> NN -> FInal 3D rendering
    #             UploadAndClean(not_processed_files) # obj upload // GC
    #             timer()
    #     except:
    #         timer()       
    
    
    not_processed_files = Fetch()
    print("number of unprocessed images : ",len(not_processed_files))
    if len(not_processed_files) == 0:
        pass
    else:
        Process() #Pose Estimation -> NN -> FInal 3D rendering
        UploadAndClean(not_processed_files) # obj upload // GC
        pass      