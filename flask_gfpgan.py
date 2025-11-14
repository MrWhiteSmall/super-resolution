from util_for_argparse import get_cuda_port_args
args = get_cuda_port_args()

from flask import Flask, request, jsonify, send_file
from io import BytesIO
from PIL import Image
from demo_gfpgan import get_sr_model, sr

app = Flask(__name__)

# 初始化超分模型，只加载一次
sr_model = get_sr_model(upscale=4)

@app.route('/sr', methods=['POST'])
def super_resolution():
    """
    接收图片，通过GFPGAN进行超分辨率重建后返回图片
    """
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded.'}), 400

    img_file = request.files['image']
    try:
        img_pil = Image.open(img_file.stream).convert('RGB')
    except Exception as e:
        return jsonify({'error': f'Cannot open image: {str(e)}'}), 400

    sr_img_pil = sr(img_pil, sr_model)
    if sr_img_pil is None:
        return jsonify({'error': 'SR model failed to process image.'}), 500

    # 返回图片
    buf = BytesIO()
    sr_img_pil.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/')
def home():
    return '''
    <h3>GFPGAN 超分辨率 API</h3>
    <form method="POST" action="/super_resolution" enctype="multipart/form-data">
        <input type="file" name="image">
        <input type="submit" value="上传并超分">
    </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port)
