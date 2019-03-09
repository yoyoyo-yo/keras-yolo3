import os

PATH = '/home/usrs/nagayosi/Gotobun/Dataset/'

li = os.listdir(PATH + 'Images')
li.sort()

with open("train.txt", 'w') as f:
    for l in li:
        gt_path = PATH + 'Annotations/' + l[:-4] + '.txt'

        write_con = os.path.join(PATH, 'Images', l)
        with open(gt_path, 'r') as fgt:
            for line in fgt.readlines():
                line = line.strip()
                c = line.split(',')
                con = '{},{},{},{},{}'.format(c[1], c[2], c[3], c[4], c[0])
                write_con += (' ' + con)

        write_con += os.linesep
        f.write(write_con)
