# SR based GFPGAN

## 目的
简化使用

## 环境

参考我的环境
requirements_sr310.txt  \

不需要一致！！ 首先 torch torchvision版本 自己对应 \
其次，运行时如果出现报错，可以参考报错package 的 版本号

## ckp

下载后把里面的pth 文件 放到 experiments/pretrained_models 下
> 链接：https://pan.baidu.com/s/1vF39DJ2n1JY24HJzUpVwhQ \
> 提取码：y5r7

下载后把里面的pth 文件 放到 gfpgan/weights 下
> 链接：https://pan.baidu.com/s/1lsX1rkJV9_d54_-N7d8s7g \
> 提取码：h9ci

如果没有上面的文件夹，记得自己创建一下哈

## 操作
1. bash demo_test.sh 查看 环境，ckp 是否都满足条件
2. python demo_gfpgan.py 运行 简化版的 sr 代码
3. python flask_gfpgan.py -c 0 -p 8088 运行 sr api 在 8088 端口
4. python flask_gfpgan_query.py -p 8088 测试 api 是否可用