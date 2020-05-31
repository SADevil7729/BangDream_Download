import os
import urllib
import urllib.request
import codecs
import re
import time


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def download(url,file):
    try:
        if os.path.isfile('./Save/Phone/'+file):
            return 1#Existed
        else:
            #print(file)
            urllib.request.urlretrieve(url, './Save/Phone/'+file)
            
            return 0#Success
    except:
        print(index)
        print(url)
        print('Fail!!')
        return 2

if __name__ == '__main__':
    


    fp = open('AssetBundleInfo', "r" , encoding = 'ISO-8859-15')
    lines = fp.readlines()
    fp.close()
    url=[]
    file=[]
    count=0
    for i in range(len(lines)):
        temp=''
        temp=lines[i].strip()
        seiki = r'^(?!.*'+'4.2.0.200'+r').*$'
        temp=re.sub(seiki,'',temp)
        temp=re.sub(r'^\n|\r','',temp)
        temp=re.sub(r'@.*?\n','\n',temp)
        temp=re.sub(r'@.*?\Z','\n',temp)
        temp=re.sub(r'^[^a-z]?(.+)\x12.*?\n','https://d2ktlshvcuasnf.cloudfront.net/Release/4.2.0.200_Hz7FdV39Tg/Android'+r'/\1',temp)

            
        temp2=lines[i].strip()
        temp2=re.sub(seiki,'',temp2)
        temp2=re.sub(r'^\n|\r','',temp2)
        temp2=re.sub(r'.*@','@',temp2)
        temp2=re.sub(r'@(.{64}).*','\g<1>',temp2)
        temp2=re.sub(r'\Z','',temp2)
        temp2=re.sub(r'.*@.*','',temp2)
        #print(temp)
        if temp != '' and temp2 != '':
            url.append(temp)
            file.append(temp2)
            count=count+1
    #download('https://d2ktlshvcuasnf.cloudfront.net/Release/4.2.0.100_Hz7FdV39Tg/Android/AssetBundleInfo')
    #download('https://d2ktlshvcuasnf.cloudfront.net/Release/4.2.0.100_Hz7FdV39Tg/Android/sound/voice/scenario/bandstory107')
    if os.path.exists('./Save/Phone'):
        pass
    else:
        os.makedirs('./Save/Phone', exist_ok=True)

    #print(url[0])
    Success=0
    Existed=0
    Fail=0
    Temp_Output=0
    for i in range(1,count):
        result=download(url[i],file[i])
        if result==0 :
            Success = Success+1
            #time.sleep( 0.05 )
        elif result==1:
            Existed = Existed +1
        else:
            Fail = Fail+1
            time.sleep( 5 )
        if i + Success*5 >= Temp_Output *100:
            Temp_Output=Temp_Output+1
            print(i)
            print(url[i])
            print(file[i])
            print('Index',i,' S',Success,' Existed',Existed,' Fail',Fail)
            
    print('Finish!!')


    

