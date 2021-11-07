#!/usr/bin/python

'''打电话识别，数据格式转换。'''

import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def phone_converter(input_path, output_path):
    '''转换格式主函数'''
    for _, _, filenames in os.walk():
        for filename in filenames:
            if(filename.endswith('xml')):
                tree = ET.parse(filename)  # <class 'xml.etree.ElementTree.ElementTree'>
                root = tree.getroot()           # 获取根节点 <Element 'data' at 0x02BF6A80>
                label = root.find('object/name').text
                print(label)
                break
        break

if __name__ == '__main__':
    input_path = '/home/data/334'
    output_path = '/home/data/334'