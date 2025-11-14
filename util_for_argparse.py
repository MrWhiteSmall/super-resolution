def get_cuda_args():
    import argparse,os
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cuda', type=str, default='2', help='CUDA device id')
    args, unknown = parser.parse_known_args()
    os.environ['CUDA_VISIBLE_DEVICES'] = args.cuda
    return args
    
def get_cuda_port_args():
    import argparse,os
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cuda', type=str, default='2', help='CUDA device id')
    parser.add_argument('-p', '--port', type=int, default=20070, help='port id')
    args, unknown = parser.parse_known_args()
    os.environ['CUDA_VISIBLE_DEVICES'] = args.cuda
    return args