# This is a sample Python script.
# _*_ coding:utf-8 _*_

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import requests
import os
from lxml import etree

def download_pypi():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    homepage_url = 'https://pypi.tuna.tsinghua.edu.cn/simple/'

    li_list = open(file_name, "r", encoding="UTF-8")

    for li in li_list:
        package_dir = li.split('/')[-2]
        
        # 根据实际存储路径修改即可，以下实例为Windows
        prefix_dir = 'E:\\pypi_source\\aa'
        # Linux如下'/home/heywhale/pypi_source'
        # prefix_dir = '/home/heywhale/pypi_source'
        if not os.path.exists(package_dir):
            os.mkdir(package_dir)

        sub_url = li.strip()

        sub_url_response = requests.get(url=sub_url, headers=headers)
        sub_url_response.encoding = sub_url_response.apparent_encoding
        sub_url_content = sub_url_response.text
        sub_url_tree = etree.HTML(sub_url_content)

        try:
            aa_list = sub_url_tree.xpath('//a')
            #print(len(aa_list))
            for aa in aa_list:
                download_homepage = 'https://pypi.tuna.tsinghua.edu.cn/'
                package_tmp_url = aa.xpath('./@href')[0]
                package_tmp_name = aa.xpath('./text()')[0]
                #print(package_tmp_name)
                package_url = download_homepage + package_tmp_url[6:]
                #print(package_url)

                package_response = requests.get(url=package_url, headers=headers)
                package_content = package_response.content
                
                # 以下是Windows示例
                package_path = prefix_dir + '\\' + package_dir + '\\' + package_tmp_name
                # 以下是Linux示例
                # package_path = prefix_dir + '/' + package_dir + '/' + package_tmp_name
                with open(package_path, 'wb') as imp:
                    imp.write(package_content)
                    #print(package_tmp_name + ' download success!')
        except:
            print(package_dir)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #file_name = sys.argv[1]
    #download_pypi()
    print('Download success!')
    print('dev')
