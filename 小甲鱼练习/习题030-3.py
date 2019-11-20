#  编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件
# （要求查找mp4 rmvb, avi的格式即可）
#  并把创建一个文件（vedioList.txt）存放所有找到的文件的路径


import os


def search_video(video_dir):
    os.chdir(video_dir)
    for item in os.listdir(os.curdir):
        if os.path.splitext(item)[1] in video:
            video_list.append(os.getcwd() + os.sep + item)
        if os.path.isdir(item):
            search_video(item)
            os.chdir(os.pardir)

    with open(video_txt, 'w')as f:
        for i in video_list:
            f.writelines(i + '\n\n')


video = ['.avi', '.rmvb', '.wmv', '.mp4', '.flv', '.f4v']
video_list = []
video_dir = input('输入查找的初始目录：')
video_txt = video_dir + '/video.txt'

search_video(video_dir)

print('视频文件位置信息已保存到%s' % video_txt)
