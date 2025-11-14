# python inference_gfpgan.py -i inputs/whole_imgs -o results -v 1.3 -s 2
test_img_path="/mnt/nas/shengjie/datasets/reid_sysu30k/sysu_test_set_all/gallery/000028311/000028311_c1_1.jpg"

# (183, 605) ==> (366, 1210)
python inference_gfpgan.py -i $test_img_path -o results -v 1.3 -s 2 -c 4