def get_sr_model(upscale=4):
    import os
    from gfpgan import GFPGANer
    from basicsr.archs.rrdbnet_arch import RRDBNet
    from realesrgan import RealESRGANer

    model_name = 'GFPGANv1.3'
    arch = 'clean'
    realesrgan_ckp = 'experiments/pretrained_models/RealESRGAN_x2plus.pth'

    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=2)
    bg_upsampler = RealESRGANer(
        scale=2,
        # model_path='https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth',
        model_path=realesrgan_ckp,
        model=model,
        tile=400,
        tile_pad=10,
        pre_pad=0,
        half=True)

    model_path = os.path.join('experiments/pretrained_models', model_name + '.pth')
    restorer = GFPGANer(
        model_path=model_path,
        upscale=upscale,
        arch=arch,
        channel_multiplier=2,
        bg_upsampler=bg_upsampler)

    return restorer

# Image.PIL
def sr(lr_img, sr_model):
    import numpy as np
    import cv2
    from PIL import Image
    input_img = np.array(lr_img)
    input_img = cv2.cvtColor(input_img, cv2.COLOR_RGB2BGR)

    # restore faces and background if necessary
    cropped_faces, restored_faces, restored_img = sr_model.enhance(
        input_img,
        has_aligned=False,
        only_center_face=False,
        paste_back=True,
        weight=0.5)

    # cropped_faces restored_faces np.array can be
    #       basicsr.imwrite ( cv2.imwrite(file_path, img, params))

    # save restored img
    if restored_img is not None:
        img_np = cv2.cvtColor(restored_img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_np)
        return img_pil

    return None

def test():
    sr_model = get_sr_model(upscale=4)
    test_img_path="/mnt/nas/shengjie/datasets/reid_sysu30k/sysu_test_set_all/gallery/000028311/000028311_c1_1.jpg"
    from PIL import Image
    img_pil = Image.open(test_img_path)
    print(img_pil.size)
    output_pil = sr(img_pil, sr_model)
    print(output_pil.size)
    output_pil.save('tmp.jpg')


if __name__=='__main__':
    from util_for_argparse import get_cuda_args

    get_cuda_args()

    test()