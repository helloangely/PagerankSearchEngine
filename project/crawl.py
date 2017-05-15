import os
import sys
import subprocess
import errno


def main():
    ''' Take first 3 arguments and execute scrapy spider, url MUST BE IN FORM OF http://... '''
    # obtain current working directory from the path of this script
    cwd = os.path.dirname(os.path.realpath(__file__))

    # get commmand line arguments
    if len(sys.argv) < 4:
        print 'Not enough arguments!'
        return
    start_urls = sys.argv[1]
    num_page = sys.argv[2]
    dest_dir = sys.argv[3]

    # make sure destination directory exists
    try:
        os.makedirs(cwd + "\\" + dest_dir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    # call scrapy in cwd with specific arguments
    args = ' '.join(['scrapy', 'crawl', 'spider',
            '-a', 'num=%s' % num_page,
            '-a', 'directory=%s' % dest_dir,
            '-a', 'urls=%s' % start_urls])
    subprocess.call(args, cwd=cwd, shell=True)

if __name__ == '__main__':
    main()
