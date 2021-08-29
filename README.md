## Note
将工作路径cd到 panda_project/code/mmdetection-master后再运行，
否则相对路径会报错！


## Installation
运行环境：python=3.7.10 torch=1.7.1 torchvision=0.8.2 opencv=4.5.1 MMCV=1.2.7 mmdetection=2.10.0+     cuda-10.2


## Crop
cd到 panda_project/code/PANDA-Toolkit-gaiic-panda 工作路径后，运行Task1_utils.py，程序自动对训练集图片进行裁图。
裁剪的图片保存到  panda_project/user_data/split_person_train/image_train
对应的标签保存到  panda_project/user_data/split_person_train/image_annos


## Train
cd到 panda_project/code/mmdetection-master 工作路径后
分别运行
python cascade_rcnn50_dcn_train/visible_dir/cascade_rcnn_r50_fpn_dconv_c3-c5_1x_coco.py   训练visible类
python cascade_rcnn50_dcn_train/full_dir/cascade_rcnn_r50_fpn_dconv_c3-c5_1x_coco.py      训练full类
python cascade_rcnn50_dcn_train/head_dir/cascade_rcnn_r50_fpn_dconv_c3-c5_1x_coco.py      训练head类
python cascade_rcnn50_dcn_train/vehicle_dir/cascade_rcnn_r50_fpn_dconv_c3-c5_1x_coco.py   训练vehicle类


## Test
cd到 panda_project/code/mmdetection-master 工作路径后，运行run.sh（默认是0号卡，如需改动直接修改run.sh文件中的 CUDA_VISIBLE_DEVICES= ）
运行结果自动保存到../../prediction_result/
run.sh自动运行test.py文件
IMAGE_ROOT = '../../tcdata/Test/'     #训练集图片路径
FASTER_RCNN_CONFIG = './cascade_rcnn50_dcn_test/cascade_rcnn_r50_fpn_dconv_c3-c5_1x_coco.py'  # 配置文件路径
CKPT_PATH = './checkpoints/cascade_rcnn50_dcn_giou_pth'  # 模型路径
RESULT_PATH = '../../prediction_result/'  # 保存结果路径

运行的配置文件为 ./cascade_rcnn50_dcn_test/cascade_rcnn_r50_fpn_dconv_c3-c5_1x_coco.py
加载的训练好的四个类别的模型位于 ./checkpoints/cascade_rcnn50_dcn_giou_pth


## Acknowlegement
This repo obtained from [MMdet](https://github.com/open-mmlab/mmdetection) and [Pand-Toolkit]https://github.com/GigaVision/PANDA-Toolkit
