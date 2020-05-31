import os
import urllib
import urllib.request
import codecs
import re
import time


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def download(url):
    try:
        full_name = url.split('//')[-1]
        filename = full_name.split('/')[-1]
        dirname = "/".join(full_name.split('/')[:-1])
        #print('./Save/'+full_name)
        if os.path.exists(dirname):
            pass
        else:
            os.makedirs('./Save/'+dirname, exist_ok=True)
        if os.path.isfile('./Save/'+full_name):
            return 1#Existed
        else:
            urllib.request.urlretrieve(url, './Save/'+full_name)
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
    for i in range(len(lines)):
        temp=''
        temp=lines[i].strip()
        seiki = r'^(?!.*'+'4.2.0.100'+r').*$'
        temp=re.sub(seiki,'',temp)
        temp=re.sub(r'^\n|\r','',temp)
        temp=re.sub(r'@.*?\n','\n',temp)
        temp=re.sub(r'@.*?\Z','\n',temp)
        temp=re.sub(r'^[^a-z]?(.+)\x12.*?\n','https://d2ktlshvcuasnf.cloudfront.net/Release/4.2.0.100_Hz7FdV39Tg/Android'+r'/\1',temp)
        if temp != '':
            url.append(temp)

        
        """
        temp=temp.replace('','')
        temp=temp.replace('','',1)###
        temp=temp.replace('','')
        temp=temp.replace('','')
        temp=temp.replace('%','')
        temp=temp.replace(',','')
        temp=temp.replace('','')
        if(temp != ''):
            temp_space = temp.find('')
            temp = temp[0:temp_space]
            temp_at =temp.find('@')
            temp_at_fin = temp.find('')
            temp_8 =temp.find('8')
            if(temp_at!=-1):
                #print (temp[temp_at+1:temp_at_fin])
                #print("#")
                1
            #if
            else:
                #print (temp)
                temp_url ='https://d2ktlshvcuasnf.cloudfront.net/Release/4.2.0.100_Hz7FdV39Tg/Android/' + temp 
                #print(temp_url)
                url.append(temp_url)
        """
    #download('https://d2ktlshvcuasnf.cloudfront.net/Release/4.2.0.100_Hz7FdV39Tg/Android/AssetBundleInfo')
    #download('https://d2ktlshvcuasnf.cloudfront.net/Release/4.2.0.100_Hz7FdV39Tg/Android/sound/voice/scenario/bandstory107')

    index=0
    Success=0
    Existed=0
    Fail=0
    for i in url:
        index=index+1
        if index % 100 ==1:
            print('Index',index,' S',Success,' Existed',Existed,' Fail',Fail)
        result=download(i)
        if result==0 :
            Success = Success+1
            time.sleep( 0.5 )
        elif result==1:
            Existed = Existed +1
        else:
            Fail = Fail+1
            time.sleep( 5 )
        
    print('Finish!!')

        



    

