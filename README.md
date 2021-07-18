# small-term-weixiang
基于情感分析的智能养老系统
安装教程
=======
1.python安装flask框架
2.linux搭建tensorflow
计算机视觉
=========
古名扬，何文龙
任务
-------
第一周周报：
任务完成情况：
1. 安装 ubuntu 系统 
2. 配置计算机视觉环境 
3. 人脸采集功能的实现 
制作提示声音
人脸识别 调用 face_recognition 库来识别人脸 
人脸采集 调用摄像头拍照采集人脸，并保存 
4.陌生人检测的实现 
调 用 face_recognition 对 图 像 进 行 训 练 ， 并 通 过 
save_embeddings 函数保存训练模型 
通过 load embeddings 函数加载训练模型，并进行陌生人 
检测
6. 使用人工神经网络（ANN）做情感分析 
学习了随机梯度下降算法，了解了一些优化器原理
进行了 hog 特征提取 
尝试了一些优化器 
进行了网络参数调整
7.录入老人，义工图片

8. 房间摄像头的监控 
 实现房间摄像头的监控，即把人脸识别模型（陌生人检测） 
第二周：
1我们使用CNN做了手写数字识别。本任务使用CNN做情感分析。
2.老人摔倒检测-收集数据。
3禁止区域入侵检测
4.义工识别、义工和老人距离的判断、义工交互检测、桌子摄像头的监控
5.opencv画面呈现在html中
6.计算机视觉端代码整合
7.对情感识别进行优化，主要表现为通过调整学习率和轮数来使得情感识别以最短的时间完成最好的效果
8.去除摔倒检测的背景
边缘检测和轮廓
此方法基于两个概念：边缘检测和轮廓。边缘检测，顾名思义，就是试图在图像中找到对比线或边缘。这个关键的第一步是对图像进行预处理，以帮助区分任何物体。有几种边缘检测方法存在，其中，Canny方法是非常受欢迎的，并打包在OpenCV中。
web端
======
陈康，何翀，孙玮
任务
----
1.管理员登录界面
2.后端入侵区域检测界面
3.个人中心界面
4.人像采集界面
5.工作人员界面
6.人像采集界面

